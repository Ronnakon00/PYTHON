import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Opencv/image/CoinNoise.png',0)
thresh , result = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)

titles  = ['original','thresh']
image = [img,result]

for i in range(len(image)):
    plt.subplot(1,2,i+1,xticks=[],yticks=[])
    plt.imshow(image[i],cmap='gray')
    plt.title(titles[i])

plt.show()