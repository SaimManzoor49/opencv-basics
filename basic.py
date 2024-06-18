import cv2 as cv
img = cv.imread('./images/img3.jpeg')

img = cv.resize(img,(400,400))

#  Converting image to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Blur an image
img = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

# Edge Cascade / Detection
img = cv.Canny(img,125,175)

# Dilation / Expanding 
# img = cv.dilate(img,(7,7),iterations=3)

# Erading / shrinking
# img = cv.erode(img,(3,3),iterations=3)

# Resizing
# img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

# Cropping
img = img[50:200,200:400]

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()