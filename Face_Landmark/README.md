# Face_Landmark 

This project demonstrates face landmark detection using the MediaPipe library. Two Python scripts are provided for processing images (`face_landmarks_image.py`) and videos (`face_landmarks_vid.py`) to detect and visualize facial landmarks.

## Requirements

- Python 3.10
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe

```

## Project Structure

- `face_landmarks_image.py`: Python script for detecting and visualizing facial landmarks in an image.
- `face_landmarks_vid.py`: Python script for detecting and visualizing facial landmarks in a video.

## Usage

1. Ensure you have the necessary dependencies installed.
2. Place your images or videos in the appropriate directories (`images` for images and `video` for videos).
3. Run the respective Python script (`face_landmarks_image.py` for images and `face_landmarks_vid.py` for videos).
4. The script will process the media, detect facial landmarks, and display the output with landmarks visualized.

## Note

- The MediaPipe library provides robust facial landmark detection capabilities, allowing you to detect key points on the face such as eyes, nose, mouth, etc.
- You can customize the visualization of facial landmarks by adjusting parameters such as circle size, color, etc. in the Python scripts.
- Experiment with different images and videos to explore the accuracy and performance of the face landmark detection.
- For more advanced usage or integration into larger projects, refer to the MediaPipe documentation for additional features and functionalities.
