import numpy as np
import cv2
import pickle


cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('faces.yml')
encodings = {}
with open("encodings.pkl", 'rb') as f:
   od_encodings = pickle.load(f)
   encodings = {v:k for k,v in od_encodings.items()}


capture = cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()
    #converting to gray scale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(grayscale, scaleFactor=1.5, minNeighbors=5)
    for(x, y, w, h) in face:
        print(x, y, w, h)
        gray = grayscale[y:y+h, x:x+w]
        color = frame[y:y + h, x:x + w]

        id, conf = recognizer.predict(gray)
        if conf >= 45 and conf <= 85:
            print(id)
            print(encodings[id])
            font = cv2.FONT_HERSHEY_PLAIN
            tag = encodings[id]
            color = (255, 0, 255)
            f_stroke = 2
            cv2.putText(frame, tag, (x, y), font, 1, color, f_stroke, cv2.LINE_AA)

        img_item = 'my_image.png'
        cv2.imwrite(img_item, gray)

        rec_color = (255, 255, 255)
        stroke = 2
        width = x+w
        height = y+h
        cv2.rectangle(frame, (x, y), (width, height), rec_color, stroke)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
