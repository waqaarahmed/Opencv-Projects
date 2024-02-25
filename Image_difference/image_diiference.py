import cv2
import numpy as np

# Load two images
image1 = cv2.imread('Image_Path_1.jpg')
image2 = cv2.imread('Image_Path_2.jpg')

# Resize images to a common size (adjust the dimensions as needed)
image1 = cv2.resize(image1, (640, 480))
image2 = cv2.resize(image2, (640, 480))

# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Ensure images have the same size
min_rows, min_cols = min(gray1.shape[0], gray2.shape[0]), min(gray1.shape[1], gray2.shape[1])
gray1 = gray1[:min_rows, :min_cols]
gray2 = gray2[:min_rows, :min_cols]

# Compute the absolute difference between the two images
abs_diff = cv2.absdiff(gray1, gray2)

# Threshold the difference image to highlight significant changes
_, threshold_diff = cv2.threshold(abs_diff, 30, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded difference image
contours, _ = cv2.findContours(threshold_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw a green outline around the detected differences
result = image1.copy()
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

# Display the images
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Absolute Difference', abs_diff)
cv2.imshow('Thresholded Difference', threshold_diff)
cv2.imshow('Result with Green Outline', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
