import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('./images/img1.jpeg')
img = cv.resize(img,(400,400))


img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Grayscale Histogram

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(img,img,mask=circle)

img = cv.calcHist([img],[0],mask,[256],[0,256])



plt.figure()
plt.title("Hist")
plt.xlabel('bins')
plt.ylabel('# of px')
plt.plot(img)
plt.xlim([0,256])
plt.show()


# cv.imshow("img",img)


cv.waitKey(0)
