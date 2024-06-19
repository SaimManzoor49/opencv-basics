import cv2 as cv

img = cv.imread('./images/img3.jpeg')
img = cv.resize(img,(500,500))


# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# BGR to Hue Seturation value (what humans see)

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)


# BGR to L*a*b

# img = cv.cvtColor(img,cv.COLOR_BGR2LAB)


# BGR to RGB 

img = cv.cvtColor(img,cv.COLOR_BGR2RGB) 
# Here by above line opencv will show inverted image as it uses BGR color formate

cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()
