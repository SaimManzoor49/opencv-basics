import cv2 as cv
import numpy as np

img = cv.imread('./images/img6.jpeg')
img = cv.resize(img,(500,500))

blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur,125,175)


# converting an image into binary

# ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,contours,-1,(0,0,255),thickness=1)
cv.imshow("contours_drawn",blank)

print(f'{len(contours)} contours found in the image')

cv.imshow('img',canny)



cv.waitKey(0)
cv.destroyAllWindows()