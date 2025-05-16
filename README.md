# 🎙️ Voice-Activated Cartesian Bot (VOABT)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![GRBL](https://img.shields.io/badge/GRBL-Compatible-green.svg)](https://github.com/gnea/grbl)
[![Whisper](https://img.shields.io/badge/Whisper-AI-orange.svg)](https://openai.com/research/whisper)

## 📖 Overview

The Voice-Activated Cartesian Bot (VOABT) is an innovative assistive technology designed to empower individuals with upper limb disabilities to write independently through voice commands. By seamlessly integrating AI-powered speech recognition with precision CNC motion control, this system transforms spoken words into handwritten text on paper.

> **Accessibility. Affordability. Autonomy.**

Developed as an accessible mini-project, VOABT prioritizes cost-effectiveness while delivering meaningful independence to users.

---

## ✨ Key Features

- 🎙️ **Real-Time Speech Recognition** powered by Whisper AI
- ✍️ **Natural Handwriting Simulation** with customizable fonts
- 🛠️ **Precision GRBL-Based Motion Control** for accurate plotting
- 🚀 **Simple Voice Operation** for intuitive user experience
- 💰 **Budget-Friendly DIY Design** using standard CNC components
- 💻 **Laptop-Driven Processing** (no specialized microcontrollers needed)
- 🔌 **Plug-and-Play Setup** with minimal configuration

---

## 🎬 Live Demonstration

![Voice-Activated Cartesian Bot in Action](images/demo.gif)

**[▶️ Watch the Full Demo on YouTube](https://youtu.be/OoTsanXN-Rg)**

---

## 🔧 Hardware Components

| Component | Description | Purpose |
|-----------|-------------|---------|
| Arduino UNO + CNC Shield | Control board | Core motion controller |
| NEMA 17 Stepper Motors | With A4988/DRV8825 drivers | X/Y axis movement |
| Servo Motor | SG90 or equivalent | Pen up/down mechanism |
| 2-Axis Frame | Custom Cartesian design | Structural foundation |
| Power Supply | 12V 4A | System power |
| Laptop | With microphone | Speech processing |
| Limit Switches | Optional | Homing and safety |

> 📑 Complete wiring diagrams and assembly instructions available in `report.pdf`

---

## 💾 Software Requirements

- Python 3.8+
- Key libraries:
  - `torch` and `whisper` for speech recognition
  - `pyserial` for Arduino communication
  - `freetype-py` for font rendering
  - `speech_recognition` for audio input

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/jebarson-caleb/Voice-Activated-Cartesian-Bot-VOABT-.git
cd Voice-Activated-Cartesian-Bot-VOABT-

# Set up virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Hardware Setup

1. Assemble the CNC frame according to the diagrams in `report.pdf`
2. Connect the Arduino to your laptop via USB
3. Wire the stepper motors to the CNC shield
4. Attach the servo for pen control
5. Connect the power supply

### Running the System

```bash
python main.py
```

---

## ⚙️ How It Works

1. **Voice Input**: System continuously monitors for speech via the laptop microphone
2. **Speech Recognition**: Whisper AI converts spoken words to text with high accuracy
3. **Text Processing**: Input is formatted and prepared for writing
4. **G-code Generation**: Text is converted to machine instructions with font styling
5. **Motion Control**: Arduino executes the G-code, moving the pen to write text
6. **Output**: Natural-looking handwritten text appears on paper

---

## 📁 Project Structure

```
Voice-Activated-Cartesian-Bot-VOABT-/
├── main.py                 # Primary control script
├── report.pdf              # Detailed documentation
├── requirements.txt        # Dependencies
├── README.md               # This file
├── LICENSE                 # MIT License
├── fonts/                  # TrueType fonts for handwriting styles
├── images/                 # Documentation images and demo GIFs
│   └── demo.gif
├── mechanical_design/      # 3D printable files
│   └── STL files
└── grbl/                   # GRBL configuration
```

---

## 🔮 Future Development Roadmap

| Feature | Status | Description |
|---------|--------|-------------|
| Limit Switch Integration | ✅ Implemented | Safety boundaries and auto-homing |
| Paper Clamping System | 🔄 In Progress | Secure paper positioning |
| Voice Control Commands | 🔄 In Progress | System control via verbal instructions |
| Multilingual Support | 📝 Planned | Recognition of multiple languages |
| User-Friendly GUI | 📝 Planned | Graphical interface for settings |
| Handwriting Style Selection | 📝 Planned | Choose between different fonts |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Jebarson Caleb D**
- 📧 Email: jebarsoncalebd@gmail.com
- 🔗 GitHub: [jebarson-caleb](https://github.com/jebarson-caleb)
- 🌐 LinkedIn: [jebarson-caleb](https://linkedin.com/in/jebarson-caleb)

---

<p align="center">
  <sub>Built with ❤️ for accessibility and independence</sub>
</p>
