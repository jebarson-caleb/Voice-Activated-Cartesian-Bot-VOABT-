
# 🗣️ Voice-Activated Cartesian Bot (VOABT)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

The Voice-Activated Cartesian Bot (VOABT) is a cost-effective assistive robotic system designed to help individuals with upper limb disabilities write independently using voice commands. By integrating AI-powered speech recognition with GRBL-based CNC motion control, spoken input is transcribed and plotted as handwritten text on paper.

Developed as a mini-project this solution prioritizes autonomy, affordability, and accessibility.

## Key Features
- 🎙️ **Live Speech Recognition** using Whisper AI.
- ✍️ **Text-to-G-code Conversion** for handwritten plotting.
- 🛠️ **GRBL-Compatible CNC Movement** for precision.
- 🧠 **Python Modular Script** controls the entire process.
- 🧾 **TrueType Font Support** for personalized handwriting.
- 💻 **Laptop-Powered** (No microcontroller for speech).
- 🧰 **Low-Cost, DIY Design** using common CNC components.

## 🎬 Demo

![Live Writing Demo](images/demo.gif)

👉 Watch the demo here: [YouTube Link](https://youtu.be/OoTsanXN-Rg)

> 📎 See `report.pdf` for the complete wiring diagram.

## Hardware Components
- Arduino UNO + CNC Shield
- Stepper Motors (NEMA 17) with A4988/DRV8825 Drivers
- Servo Motor (Pen up/down)
- Custom 2-axis Cartesian Frame
- 12V 4A Power Supply
- USB-connected Laptop (with microphone)
- (Optional) Limit Switches

## Software Requirements
- Python 3.x
- `speech_recognition`, `torch`, `whisper`, `pyserial`, `freetype-py`

## Setup Instructions
```bash
# Step 1: Clone the repo
git clone https://github.com/jebarson-caleb/Voice-Activated-Cartesian-Bot-VOABT-.git
cd Voice-Activated-Cartesian-Bot-VOABT-

# Step 2: Install dependencies
pip install -r requirements.txt
# For Whisper & Torch (may vary based on your system):
pip install torch whisper

# Step 3: Connect hardware (see COA report.pdf)
```

## Running the Bot
```bash
python main.py  # Replace with actual filename
```

## How It Works
1. The script records your voice.
2. Whisper transcribes speech into text.
3. Text is converted into G-code with font styling.
4. G-code is sent to the CNC bot.
5. Bot writes the message using pen control and motion.

## Folder Structure
```
Voice-Activated-Cartesian-Bot-VOABT-/
├── report.pdf
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
├── fonts/
├── images/
│   └── demo.gif
└── mechanical_design/
│   └── STL files
├── grbl/
│   └──
```

## Future Improvements
- ✅ Limit switch logic integration
- 📐 Paper clamping mechanism
- 🎛️ Voice commands for bot control
- 🌐 Multilingual support
- 🖥️ GUI for simplified user interaction

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
**Jebarson Caleb D**  
Email: jebarsoncalebd@gmail.com
