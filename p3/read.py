import cv2 as cv


# img = cv.imread('../images/img1.jpeg')

# img = cv.resize(img,(400,400))

# cv.imshow('myImg',img)

# cv.waitKey(0)

# cv.destroyAllWindows()

def rescaleFrame(frame,scale=0.35):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width,height)
    # return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    return cv.resize(frame,dimensions)


    


cap = cv.VideoCapture('../videos/preview-1014484-RzphVdNjsk-high.mp4')

def changeVideoRes(width,height):
# only works for live video
    cap.set(3,width)
    cap.set(4,height)


while True:
    isTrue,frame = cap.read()

    # frame = cv.resize(frame,(400,400))
    frame = rescaleFrame(frame)

    cv.imshow('Video',frame)

    if isTrue == False:
        break

    if cv.waitKey(65) & 0xff == ord('p'):
        break

cap.release()
cv.destroyAllWindows()