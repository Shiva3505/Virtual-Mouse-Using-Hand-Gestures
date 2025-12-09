# 🖱️ Virtual Mouse Using Hand Gesture Recognition

This project implements a **Virtual Mouse System** that uses **hand gestures captured from a webcam** to control mouse actions such as movement, clicking, scrolling, dragging, and taking screenshots.
It uses **MediaPipe Hands**, **OpenCV**, **PyAutoGUI**, and **pynput** to deliver a smooth, real-time gesture-controlled mouse experience.

---

## 🚀 Features

### 🎯 Core Functionalities

* **Mouse Movement** using index finger position
* **Left Click, Right Click, Double Click**
* **Scrolling** using four-finger gesture
* **Dragging** via pinch-and-hold gesture
* **Screenshot Capture** with a simple pinch
* **Gesture Debouncing** for avoiding accidental actions
* **Smooth Cursor Motion** using Exponential Moving Average (EMA)

### 🧠 Technologies Used

* MediaPipe Hands (gesture detection)
* OpenCV (webcam processing)
* PyAutoGUI & Pynput (mouse control)
* Python (main logic)

---

## 📂 Project Structure

```
├── main.py                # Main application loop (webcam + gesture handling)
├── gestures.py            # Gesture detection & mouse action logic
├── utils.py               # Helper functions (angles, distance, filenames)
├── smoothing.py           # EMA-based cursor smoothing
├── config.py              # All configuration constants
├── requirements.txt       # Dependencies
└── Screenshots/           # Auto-created folder for saved screenshots
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/virtual-mouse-gesture.git
cd virtual-mouse-gesture
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

Press **Q** anytime to exit.

---

## ✋ Gesture Controls (Summary)

| Gesture                      | Description  |
| ---------------------------- | ------------ |
| **Three Fingers Up**         | Move mouse   |
| **Four Fingers Up**          | Scroll       |
| **Index angle < threshold**  | Left Click   |
| **Middle angle < threshold** | Right Click  |
| **Both angles < 50°**        | Double Click |
| **Pinch (<0.05 distance)**   | Screenshot   |
| **Pinch & Hold (<0.06)**     | Drag Start   |
| **Release (>0.06)**          | Drag End     |

All parameters can be modified in **config.py**.
✔ Examples:

* ANGLE_THRESHOLD_CLICK
* THUMB_INDEX_DIST_CLICK
* SMOOTHING_ALPHA
* SCREENSHOT directory


---

## 🧩 Code Overview

### main.py

Handles webcam, MediaPipe processing, drawing, and gesture output.


### gestures.py

Maps detected gestures to mouse actions (click, drag, scroll, screenshot).


### smoothing.py

Applies **EMA smoothing** for stable cursor motion.


### utils.py

Contains helpful math functions (angle calculation, Euclidean distance).


---

## 📸 Screenshots Folder

Screenshots automatically save inside:

```
Screenshots/
```

Your project creates this folder if it doesn't exist.


---

## ⚙️ Requirements

See `requirements.txt`


---

## 🤖 Future Enhancements

* Add custom GUI for settings
* Support multi-hand interactions
* Add gesture-based zooming
* Add left-handed mode
* Introduce machine learning–based gesture classification

---

## 🏁 Conclusion

This Virtual Mouse project demonstrates how **computer vision + gesture recognition** can be used to interact with a computer without physical hardware.
With accurate landmark detection, gesture rules, and smooth cursor tracking, the system provides an intuitive hands-free mouse experience.

---
Developed by G Shiva Ram Reddy

