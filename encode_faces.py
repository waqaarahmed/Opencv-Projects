from PIL import Image
import cv2
import pickle
import numpy as np
import os

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(SRC_DIR, 'images')

cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
cur_id = 0
name_id = {}
names = []
faces = []

for root, dirs, files in os.walk(IMG_DIR):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            name = os.path.basename(root).replace(' ', '-').lower()

            if not name in name_id:
                name_id[name] = cur_id
                cur_id +=1

            id = name_id[name]

            pil_img = Image.open(path)
            #convert to grayscale
            pil_gray = pil_img.convert("L")
            size = (550, 550)
            final_img = pil_gray.resize(size, Image.ANTIALIAS)
            #converting to numpy array
            img_array = np.array(final_img, 'uint8')
            face = cascade.detectMultiScale(img_array, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in face:
                roi = img_array[y:y+h, x:x+w]
                faces.append(roi)
                names.append(id)


with open("encodings.pkl", 'wb') as f:
    pickle.dump(name_id, f)
recognizer.train(faces, np.array(names))
recognizer.save('faces.yml')