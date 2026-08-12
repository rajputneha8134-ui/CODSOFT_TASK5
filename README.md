# CODSOFT_TASK5

# 👤 Face Detection System

## Task 5 – Face Detection and Recognition

A real-time **Face Detection System** built using Python and OpenCV. The application uses a pretrained **Haar Cascade classifier** to detect human faces through a webcam.

When a face is detected, the application draws a bounding box around it and displays the number of detected faces.

## 🚀 Features

* 👤 Real-time face detection
* 📷 Webcam support
* 🧠 Pre-trained Haar Cascade model
* 🟩 Bounding box around detected faces
* 🔢 Face count
* ⚡ Real-time processing
* ❌ Camera error handling
* 💻 Simple OpenCV interface

## 🛠️ Technologies Used

* Python 3
* OpenCV
* Haar Cascade Classifier
* Computer Vision

## 📂 Project Structure

```text
TASK-5-FACE-DETECTION/
│
├── face_detection.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 How It Works

The application follows this process:

```text
             Webcam
                │
                ▼
          Capture Frame
                │
                ▼
       Convert to Grayscale
                │
                ▼
       Haar Cascade Detector
                │
                ▼
        Detect Human Faces
                │
                ▼
       Draw Bounding Boxes
                │
                ▼
          Display Result
```

## 🔍 Face Detection Process

### 1. Capture Video

OpenCV accesses the computer's webcam and continuously captures frames.

### 2. Convert to Grayscale

The captured frame is converted from BGR/RGB representation to grayscale.

```python
gray_frame = cv2.cvtColor(
    frame,
    cv2.COLOR_BGR2GRAY
)
```

Grayscale images simplify the detection process.

### 3. Detect Faces

The Haar Cascade classifier searches the image for patterns that resemble human faces.

```python
faces = face_cascade.detectMultiScale(
    gray_frame,
    scaleFactor=1.1,
    minNeighbors=5
)
```

### 4. Draw Bounding Boxes

When a face is detected, the application draws a rectangle around it.

```text
┌──────────────────────┐
│                      │
│       FACE           │
│       DETECTED       │
│                      │
└──────────────────────┘
```

### 5. Display Result

The processed video is displayed in real time.

Press **Q** to close the application.

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/TASK-5-FACE-DETECTION.git
```

Open the project:

```bash
cd TASK-5-FACE-DETECTION
```

Install the required library:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python face_detection.py
```

Your webcam should open automatically.

You should see a window similar to:

```text
Face Detection - Press Q to Exit

        ┌───────────────┐
        │ Face Detected │
        │               │
        │      👤       │
        │               │
        └───────────────┘

Faces: 1
```

Press:

```text
Q
```

to exit.

## 🧠 Haar Cascade

Haar Cascade is a traditional computer vision technique used for object detection.

OpenCV provides pretrained Haar Cascade classifiers that can detect objects such as:

* Faces
* Eyes
* Smiles
* Upper body

This project uses:

```text
haarcascade_frontalface_default.xml
```

for frontal face detection.

## 🎯 Learning Objectives

This project demonstrates:

* Computer Vision
* Image processing
* Real-time video processing
* Face detection
* OpenCV
* Pretrained models
* Haar Cascade classifiers
* Webcam integration
* Bounding box detection

## 🔮 Future Improvements

The project can be extended with:

* 👤 Face recognition
* 🧑‍🤝‍🧑 Multiple-person recognition
* 📸 Image-based face detection
* 🎥 Video file processing
* 🗂️ Face database
* 🔐 Authentication system
* 🧠 Deep-learning face detector
* ArcFace-based recognition
* Face embeddings
* Attendance management system
* Flask web interface

## ⚠️ Important Note

This project performs **face detection**, not identity recognition.

Face detection answers:

> "Where is a face?"

Face recognition answers:

> "Whose face is this?"

Recognition can be added as a separate advanced feature using face embeddings and a suitable recognition model.

## 📌 Internship Task

**Task:** Task 5 – Face Detection and Recognition

**Objective:** Develop an AI application capable of detecting faces in images or videos using pretrained face detection models such as Haar Cascades or deep-learning-based detectors.

## 👨‍💻 Author

neha rajput
