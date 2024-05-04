# Computer Vision Projects Repository

This repository contains Python scripts for various computer vision projects. Each project focuses on different aspects of computer vision, from detecting facial landmarks to recognizing gestures and highlighting differences between images.

## Projects Included

### 1. Face Landmark

The Face Landmark project focuses on detecting facial landmarks using the Mediapipe library. It identifies key points on a person's face, such as the eyes, nose, and mouth, allowing for various applications like face alignment, emotion recognition, and virtual makeup.

- **File**: `face_landmarks.py`
- **Description**: Python script for detecting and visualizing facial landmarks in images.

### 2. Facial Recognition

The Facial Recognition project involves recognizing faces in images or videos and associating them with known identities. It uses LBPH (Local Binary Patterns Histograms) for face recognition and can be used for applications like access control, surveillance, and personalized user experiences.

- **File**: `facial_recognition.py`
- **Description**: Python script for recognizing faces in images or videos and associating them with known identities.

### 3. Gesture Controlled

The Gesture Controlled project enables interaction with a computer system or application using hand gestures captured through a camera. It uses the Mediapipe library to track hand movements in real-time and translates them into commands or actions.

- **File**: `gesture_controlled.py`
- **Description**: Python script for enabling gesture control of a computer system or application using hand movements.

### 4. Image Difference

The Image Difference project compares two images and highlights the differences between them by detecting changes in pixel values. It is useful for identifying changes in images over time, such as in surveillance or monitoring systems.

- **File**: `image_difference.py`
- **Description**: Python script for comparing two images and highlighting the differences.

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the project directory containing the desired script.
3. Install the necessary dependencies if not already installed.
4. Run the Python script corresponding to the project.
5. Follow the instructions provided in the script's README or comments for specific usage guidelines.

## Dependencies

- OpenCV (`cv2`)
- Mediapipe (for Face Landmark and Gesture Controlled projects)

You can install the required dependencies using pip:

```bash
pip install opencv-python mediapipe
```

## Note

- Ensure you have a compatible camera device connected and properly configured for projects involving real-time video processing.
- Adjust parameters and configurations as needed based on your specific use case and environment.
