# Image Difference 

This Python script compares two images and highlights the differences between them by detecting changes in pixel values. It is useful for identifying changes in images over time, such as in surveillance or monitoring systems.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

You can install OpenCV using pip:

```bash
pip install opencv-python
```

## Project Structure
- `image_difference.py`: Python script for comparing two images and highlighting the differences.

## Usage
1. Ensure you have the necessary dependencies installed.
2. Replace 'Image_Path_1.jpg' and 'Image_Path_2.jpg' with the paths to the two images you want to compare.
3. Run the Python script `image_difference.py`.
4. The script will load the two images, compute the absolute difference between them, threshold the difference image to highlight significant changes, and draw a green outline around the detected differences.
5. Four windows will appear displaying the original images (`Image 1` and `Image 2`), the absolute difference between the images (`Absolute Difference`), the thresholded difference image (`Thresholded Difference`), and the result with green outlines (Result with Green Outline).
