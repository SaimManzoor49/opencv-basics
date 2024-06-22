import cv2 as cv

cap = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

while True:
    isTrue,frame = cap.read()
    if isTrue:
        frame = cv.resize(frame,(400,400))
        face_rects = haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=9)
        for (x,y,w,h) in face_rects:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.imshow('Camera',frame)
        if cv.waitKey(25) & 0xff == ord('p'):
            break
    else:
        break





cv.destroyAllWindows()