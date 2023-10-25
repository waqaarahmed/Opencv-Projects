import os
import cv2 as cv
import mediapipe as mp

# creating face mesh
mp_mesh = mp.solutions.face_mesh
face_mesh = mp_mesh.FaceMesh()

#loading video
capture = cv.VideoCapture(os.path.join('video', 'face.mp4'))

while True:
# Loading media
    i, frame = capture.read()
    if i is not True:
        break
    h, w, _ = frame.shape
    c_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    face = face_mesh.process(c_image)

    for facial_landmark in face.multi_face_landmarks:
        for x in range(0, 468):
            p1 = facial_landmark.landmark[x]
            x = int(p1.x * w)
            y = int(p1.y * h)
            cv.circle(frame, (x, y), 1, (255, 255, 255), -1)  # --> Drawing circle on image

    # displaying media
    cv.imshow('Image', frame)
    cv.waitKey(1)