import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Opencv/image/CoinNoise.png',0)
thresh , result = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)

dilation = cv2.dilate(result,kernel,iterations=5)
Erode = cv2.erode(result,kernel,iterations=5)
opening = cv2.morphologyEx(result,cv2.MORPH_OPEN,kernel,iterations=2)
closeing = cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel,iterations=5)

titles  = ['original','thresh','dilation','erode','opening','closeing']
image = [img,result,dilation,Erode,opening,closeing]

for i in range(len(image)):
    plt.subplot(2,3,i+1,xticks=[],yticks=[])
    plt.imshow(image[i],cmap='gray')
    plt.title(titles[i])

plt.show()