import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./images/img2.jpeg')
img = cv.resize(img,(400,400))

# creating mask
blank = np.zeros(img.shape[:2],dtype='uint8') 

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),10-0,255,-1)

# mask = cv.bitwise_and(img,img,mask=circle)

# creating histogram
colors = ('b','g','r')

plt.figure()
plt.title('Hist')
plt.xlabel('Bins')
plt.ylabel('Pxs')

for i,col in enumerate(colors): 
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()




cv.waitKey(0)


