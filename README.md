# Hand Feature Detection Using MediaPipe

This project utilizes **MediaPipe**, a cross-platform framework by Google, to perform real-time hand feature detection. The program captures live video from the webcam, detects hand landmarks, and visualizes the detected hand landmarks with the connections between the landmarks.

## Prerequisites

To run this project, you need the following dependencies:

- Python 3.x
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)

You can install these dependencies using the following pip commands:

```bash
pip install opencv-python
pip install mediapipe
```

## How It Works

1. **Webcam Feed**: The program uses `cv2.VideoCapture(0)` to capture the live video feed from your webcam.
2. **Hand Detection**: The MediaPipe **Hands** module processes each frame to detect hand landmarks.
3. **Landmarks Visualization**: If hands are detected, the program draws landmarks on the hands and visualizes the connections between those landmarks in real-time using the `mp.solutions.drawing_utils`.
4. **Exit**: To exit the program, simply press the **Esc** key.

## File Structure

```
.
├── hand_feature_detection.py           # Python script for hand feature detection using MediaPipe
└── README.md                          # Project description
```

## Usage

1. Ensure that you have the required dependencies installed.
2. Run the Python script:

```bash
python hand_feature_detection.py
```

3. The webcam feed will open, and you should see landmarks drawn on your hand as you move it in front of the camera.
4. Press **Esc** to close the window and stop the detection.

## Code Explanation

- **Mediapipe Hands Module**: This is the core of the hand feature detection, where `mp_hands.Hands()` is used to detect and track hands.
- **Landmark Detection**: `hands.process(rgb_frame)` detects hand landmarks in the provided frame. These landmarks are represented as 3D coordinates (x, y, z).
- **Drawing Landmarks**: `mp_draw.draw_landmarks()` is used to draw the detected landmarks and their connections in real-time on the frame.
- **Exit Condition**: The program listens for the **Esc** key to exit the loop and release the webcam.

