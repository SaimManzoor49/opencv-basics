import cv2 as cv


# img = cv.imread('../images/img1.jpeg')

# img = cv.resize(img,(400,400))

# cv.imshow('myImg',img)

# cv.waitKey(0)

# cv.destroyAllWindows()


cap = cv.VideoCapture('../videos/preview-1014484-RzphVdNjsk-high.mp4')

while True:
    isTrue,frame = cap.read()
    cv.imshow('Video',frame)

    if isTrue == False:
        break

    if cv.waitKey(25) & 0xff == ord('p'):
        break

cap.release()
cv.destroyAllWindows()