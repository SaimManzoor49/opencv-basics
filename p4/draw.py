import cv2 as cv 
import numpy as np

img = cv.imread('../images/img2.jpeg')

img = np.zeros((600,600,3),dtype='uint8') 

#  Drawing a square
# img[200:300,300:400] = 0,255,0 


# Drawing a Rectangle
# cv.rectangle(img,(0,0),(img.shape[0]//2,img.shape[1]//2),(0,255,0),thickness=cv.FILLED)


#  Drawing a circle
# cv.circle(img,(img.shape[0]//2,img.shape[1]//2),40, (0,0,255),thickness=3)


# Dwaring Line
# cv.line(img,(0,img.shape[1]//2),(img.shape[0]//2,img.shape[1]//2),(0,255,0),thickness=2)

# Writing Text

cv.putText(img,'Hello World',(img.shape[0]//2,img.shape[1]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,144,255),2)


cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()