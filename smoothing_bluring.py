import cv2 as cv
import numpy as np


img = cv.imread('./images/img2.jpeg')
img = cv.resize(img,(400,400))

# Averaging
# img = cv.blur(img,(3,3))

# GaussianBlur
# img = cv.GaussianBlur(img,(7,7),0)

# MedianBlur
# img = cv.medianBlur(img,3)



cv.imshow('img',img)



cv.waitKey(0)
cv.destroyAllWindows()