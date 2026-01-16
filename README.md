# Gesture Presentation Control 🎯✋

A real-time **gesture-controlled presentation system** built using **Python, OpenCV, MediaPipe, and PyAutoGUI**.  
This project allows users to control presentation slides using hand gestures captured via a webcam.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe
- Gesture-based slide navigation
- Stable gesture detection with cooldown & frame history
- Works with PowerPoint, PDF viewers, and browser presentations
- No IoT or external hardware required

---

## ✋ Gesture Controls

| Gesture | Action |
|------|-------|
| 1 finger up | Next slide |
| 2 fingers up | Previous slide |
| ESC | Exit application |

---

## 🛠️ Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

---

## 📦 Installation & Setup

```bash
# Clone repository
git clone https://github.com/pallasanjaynishanth/Gesture_Presentation_Control.git

# Navigate into folder
cd Gesture_Presentation_Control

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install opencv-python mediapipe pyautogui numpy

# Run project
python gesture_control.py
