import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('Opencv/image/map.jpg',0)

size = [3,5,9,17,33]

plt.subplot(2,3,1,xticks=[],yticks=[])
plt.imshow(img,cmap='gray')

for i in range(len(size)):
    result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1) 
    plt.subplot(2,3,2+i,xticks=[],yticks=[])
    plt.imshow(result,cmap='gray')
plt.show() 