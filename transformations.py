import cv2 as cv 
import numpy as np
img = cv.imread('./images/img5.jpeg')

# Translation / shifting an image in x axis or y axis
def translate(img,x,y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMatrix,dimensions)

# translated = translate(img,100,100)

# cv.imshow('translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if(rotPoint == None):
            rotPoint = (width//2,height//2)

    rotMatrix = cv.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMatrix,dimensions)

# rotated = rotate(img,90)
# cv.imshow('rotated',rotated)


# Flipping
# fliped = cv.flip(img,0)
# fliped_1 = cv.flip(img,1)
# fliped_2 = cv.flip(img,-1)

# cv.imshow('fliped',fliped)
# cv.imshow('fliped_1',fliped_1)
# cv.imshow('fliped_2',fliped_2)

# Cropping
img = cv.resize(img,(600,600))
croppedImg = img[200:400,300:400]

cv.imshow("cropped",croppedImg)



cv.waitKey(0)
cv.destroyAllWindows()