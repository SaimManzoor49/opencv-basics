import cv2 as cv

img = cv.imread('./images/img1.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'Number of faces in image is {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),255,thickness=2)

cv.imshow('asd',img)

cv.waitKey(0)
