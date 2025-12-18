import cv2
import numpy as np

img = cv2.imread('Opencv/image/ball2d.jpg')
imgresize = cv2.resize(img,(400,400))

lower = np.array([5,111,10])
upper = np.array([124,255,133])

mask1 = cv2.inRange(imgresize,lower,upper)

result = cv2.bitwise_and(imgresize,imgresize,mask=mask1)

cv2.imshow('original',imgresize)
cv2.imshow('mark',mask1)
cv2.imshow('result',result)

cv2.waitKey(0) 
cv2.destroyAllWindows()