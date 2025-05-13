import speech_recognition as sr
import torch
import whisper
import serial
import time
import freetype
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# Constants
A4_WIDTH = 210  # mm
A4_HEIGHT = 297  # mm
TEXT_MARGIN = 10  # mm margin from edges
FEED_RATE = 1000  # Movement speed (mm/min)
CHARACTER_HEIGHT = 10  # mm
CHARACTER_SPACING = 5  # mm
LINE_SPACING = 15  # mm

# Servo Configuration
PEN_UP_ANGLE = 90  # Servo angle when pen is lifted (adjust as needed)
PEN_DOWN_ANGLE = 10  # Servo angle when pen is lowered
SERVO_DELAY = 0.3  # seconds to wait for servo movement

# CNC Configuration
CNC_PORT = "COM12"  # Change to your CNC port
BAUD_RATE = 115200  # Standard GRBL baud rate

# Initialize Whisper model
try:
    logging.info("Loading Whisper model...")
    model = whisper.load_model("small")
except Exception as e:
    logging.error(f"Failed to load Whisper model: {e}")
    sys.exit(1)

# Initialize CNC connection
def initialize_cnc():
    try:
        cnc = serial.Serial(CNC_PORT, BAUD_RATE)
        time.sleep(2)  # GRBL initialization delay
        logging.info("CNC connected successfully.")
        # Wake up GRBL
        cnc.write(b"\r\n\r\n")
        time.sleep(2)
        cnc.flushInput()
        return cnc
    except Exception as e:
        logging.error(f"CNC connection failed: {e}")
        return None

cnc = initialize_cnc()

def transcribe_live():
    """Transcribe live speech into text using Whisper."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Calibrating microphone...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Speak now (5 second limit)...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        with open("temp_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe("temp_audio.wav")
        return result["text"]
    except sr.WaitTimeoutError:
        logging.warning("No speech detected.")
        return None
    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        return None

def text_to_gcode(text, font_path=r"fonts/ARIALNI.TTF"):
    """Convert text into G-code for CNC drawing."""
    try:
        face = freetype.Face(font_path)
        face.set_char_size(CHARACTER_HEIGHT * 64)  # Set size in 1/64th points
    except Exception as e:
        logging.error(f"Failed to load font: {e}")
        return None

    gcode = [
        "G21",        # mm units
        "G90",        # absolute positioning
        "G17",        # XY plane selection
        f"M03 S{PEN_UP_ANGLE}",  # pen up
        f"G4 P{SERVO_DELAY}",    # servo delay
        f"G0 X{TEXT_MARGIN} Y{TEXT_MARGIN} F{FEED_RATE}"  # start position
    ]

    x, y = TEXT_MARGIN, TEXT_MARGIN  # Start at top-left corner

    for char in text:
        if char == "\n":  # Handle newlines
            y += LINE_SPACING
            x = TEXT_MARGIN
            continue
            
        if char == " ":   # Handle spaces
            x += CHARACTER_SPACING
            continue

        # Get character metrics
        try:
            face.load_char(char)
            metrics = face.glyph.metrics
            char_width = metrics.horiAdvance / 64  # Convert to mm
        except Exception as e:
            logging.warning(f"Failed to load character '{char}': {e}")
            continue
        
        # Pen down
        gcode.append(f"M03 S{PEN_DOWN_ANGLE}")
        gcode.append(f"G4 P{SERVO_DELAY}")

        # Draw character contours
        outline = face.glyph.outline
        points = list(outline.points)
        start_idx = 0
        
        for end_idx in outline.contours:
            contour = points[start_idx:end_idx+1]
            for i, (px, py) in enumerate(contour):
                gx = x + (px / 64)
                gy = y + (py / 64)  # Y increases downward
                cmd = "G0" if i == 0 else "G1"
                gcode.append(f"{cmd} X{gx:.2f} Y{gy:.2f} F{FEED_RATE}")
            start_idx = end_idx + 1

        # Pen up
        gcode.append(f"M03 S{PEN_UP_ANGLE}")
        gcode.append(f"G4 P{SERVO_DELAY}")

        # Move to next character position (X-axis only)
        x += max(char_width, CHARACTER_SPACING)

    # End of program
    gcode.extend([
        f"M03 S{PEN_UP_ANGLE}",
        "G0 X0 Y0",  # Return to home
        "M30"        # Program end
    ])
    
    return "\n".join(gcode)

def send_gcode_to_cnc(gcode):
    """Send G-code to the CNC machine."""
    if not cnc:
        logging.error("CNC not connected.")
        return False

    logging.info("Sending G-code...")
    
    # Send a wake-up call first
    cnc.write(b"\r\n\r\n")
    time.sleep(2)
    cnc.flushInput()

    for line in gcode.split("\n"):
        clean_line = line.strip()
        if not clean_line:
            continue
            
        logging.info(f"[CNC] {clean_line}")
        
        try:
            # Send the command
            cnc.write(f"{clean_line}\n".encode())
            
            # Wait for response with timeout
            start_time = time.time()
            while True:
                if time.time() - start_time > 5:  # 5 second timeout
                    logging.warning("Timeout waiting for response.")
                    break
                    
                if cnc.in_waiting > 0:
                    try:
                        grbl_out = cnc.readline().decode('ascii', errors='ignore').strip()
                        if "ok" in grbl_out.lower():
                            break
                        elif "error" in grbl_out.lower():
                            logging.error(f"CNC Error: {grbl_out}")
                            return False
                    except UnicodeDecodeError:
                        # Skip non-decodable data
                        continue
        
        except Exception as e:
            logging.error(f"Communication failed: {e}")
            return False
    
    logging.info("G-code execution complete.")
    return True

if __name__ == "__main__":
    try:
        while True:
            cmd = input("Press Enter to record or type 'exit': ").lower()
            if cmd == "exit":
                break

            text = transcribe_live()
            if text:
                logging.info(f"Transcription: {text}")
                gcode = text_to_gcode(text)
                if gcode:
                    # Save G-code to a file
                    gcode_file_path = "output.gcode"
                    with open(gcode_file_path, "w") as gcode_file:
                        gcode_file.write(gcode)
                    logging.info(f"G-code saved to {gcode_file_path}.")

                    logging.info("G-code ready.")
                    if not send_gcode_to_cnc(gcode):
                        logging.warning("There were CNC errors.")
    except KeyboardInterrupt:
        logging.info("Shutting down...")
    finally:
        if cnc:
            # Ensure pen is up before exiting
            cnc.write(f"M03 S{PEN_UP_ANGLE}\n".encode())
            time.sleep(1)
            cnc.close()
            logging.info("CNC connection closed.")