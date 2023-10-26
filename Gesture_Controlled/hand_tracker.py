import os
import cv2 as cv
import mediapipe as mp

#Drawing lines in between the landmarks
drawing = mp.solutions.drawing_utils

#Tracking the hand in real time
hand = mp.solutions.hands

#loading video
cap = cv.VideoCapture(os.path.join('videos', 'hand.mp4'))

hands = hand.Hands()
while True:
    i, frame = cap.read()
    if i is not True:
        break
    #flip the image if you are using webcam, otherwise just convert the color from BGR to RGB
    #cap_image = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #storing the result
    output = hands.process(frame)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    if output.multi_hand_landmarks:
        for hand_landmarks in output.multi_hand_landmarks:
            drawing.draw_landmarks(frame, hand_landmarks, hand.HAND_CONNECTIONS)
    cv.imshow('hand_tracker', frame)
    cv.waitKey(1)




