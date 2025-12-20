import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Opencv/image/noise.png')
kernel = np.ones((3,3),np.float32)/9

filter2d = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
med = cv2.medianBlur(img,5)
gblur = cv2.GaussianBlur(img,(5,5),2)

list_im = [img,filter2d,blur,med,gblur]
list_title = ['original','filter2d','mean','med','gblur']

for i in range(len(list_im)):
    plt.subplot(2,3,1+i,xticks=[],yticks=[])
    plt.imshow(list_im[i])
    plt.title(list_title[i])

plt.show()