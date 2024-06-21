import cv2 as cv
import numpy as np

img = cv.imread('./images/img1.jpeg')
img = cv.resize(img,(400,400))

# Masking // focus on speafic parts of an image; size of mask should be same as images size 

blank = np.zeros(img.shape[:2],dtype='uint8')

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)


cv.imshow('mask',masked)



cv.waitKey(0)