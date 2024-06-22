import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Face_Trained.yml')

img = cv.imread('./anyImgPath.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

# Detect Face
people = ['list of people']
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label,confidance = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidance of {confidance}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)