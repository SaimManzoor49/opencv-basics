import cv2 as cv 
import numpy as np 

img = cv.imread('./images/img1.jpeg')


b,g,r = cv.split(img)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


img = cv.merge((b,g,r))


blank = np.zeros(img.shape[:2],dtype='uint8')


img = cv.merge([b,blank,blank])

cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()