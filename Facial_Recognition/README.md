# Facial Recognition

This project implements a facial recognition system using OpenCV for face detection and the LBPH (Local Binary Patterns Histograms) algorithm for face recognition. The project consists of two Python scripts: `encode_faces.py` for encoding faces and training the recognition model, and `faces.py` for real-time face recognition.

## Requirements

- Python 3.9
- OpenCV (`cv2`)
- `PIL` (Python Imaging Library)
- `numpy`

You can install the required libraries using pip:

```bash
pip install opencv-python Pillow numpy
```

## Project Structure

- `encode_faces.py`: Python script for encoding faces and training the recognition model.
- `faces.py`: Python script for real-time face recognition.

## Usage

- Ensure you have the necessary dependencies installed.
- Prepare your dataset by placing images of individuals in the `images` directory. Each subdirectory should be named after the - -- person and contain images of their face.
- Run the Python script `encode_faces.py` to encode the faces and train the recognition model. This script will create `encodings.pkl` containing the name-to-id mappings and `faces.yml` containing the trained recognition model.
- Run the Python script `faces.py` for real-time face recognition. The script will use the webcam to detect and recognize faces.

## Note

- The `encode_faces.py` script uses Haar cascades for face detection and the LBPH algorithm for face recognition.
- Adjust parameters such as scaleFactor and minNeighbors in the Haar cascade and conf threshold in face recognition for optimal performance.
- Ensure proper lighting conditions and camera positioning for accurate face detection and recognition.
- Experiment with different datasets and configurations to improve the accuracy and robustness of the facial recognition system.
