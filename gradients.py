import cv2 as cv
import numpy as np

img = cv.imread('./images/img1.jpeg')
img = cv.resize(img,(400,400))


img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(img,cv.CV_64F)
lap = np.uint8(np.absolute(lap))


# Sobel
sobelx = cv.Sobel(img,cv.CV_64F,1,0)
sobely = cv.Sobel(img,cv.CV_64F,0,1)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
# combined Sobel
sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel',sobel)

# Canny
canny = cv.Canny(img,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)