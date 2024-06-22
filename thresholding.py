import cv2 as cv 
import numpy as np

img = cv.imread('./images/img3.jpeg')
img = cv.resize(img,(400,400))

img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Simple Binary Thresholding
threshold,thresh=cv.threshold(img,150,255,cv.THRESH_BINARY)
cv.imshow("img",thresh)

# inverse thresh

# threshold,thresh_inv=cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
# cv.imshow("img",thresh_inv)


# Adaptive Thresholding
adpt_thresh = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,13,3)
cv.imshow('adpt_thresh',adpt_thresh)





cv.waitKey(0)