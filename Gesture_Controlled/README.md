# Gesture Controlled Project

This Python script implements a gesture-controlled system using the MediaPipe library for hand tracking. The script tracks hand movements in real-time and draws landmarks on the detected hand.

## Requirements

- Python 3.11
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe
```
## Project Structure

- `hand_tracker.py`: Python script for real-time hand tracking and gesture recognition.

## Usage

1. Ensure you have the necessary dependencies installed.
2. Place your video file containing hand movements in the `videos` directory. Alternatively, you can use a webcam for real-time tracking.
3. Run the Python script `hand_tracker.py`.
4. The script will track hand movements in the video or webcam feed and draw landmarks on the detected hand.
5. Perform various hand gestures, and the system will recognize and display them in real-time.

## Note

- The  `hand_tracker.py` script uses the MediaPipe library for hand tracking and landmark detection.
- Adjust parameters and thresholds in the script for optimal hand tracking performance.
- Experiment with different hand gestures and movements to control various applications or systems.
- Ensure proper lighting conditions and camera positioning for accurate hand tracking and gesture recognition.
