import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('Opencv/image/currency.jpg',0)
sobelx = cv2.Sobel(img,-1,1,0)
sobely = cv2.Sobel(img,-1,0,1)
sobelxy = cv2.bitwise_or(sobelx,sobely)
sobelxy2 = cv2.Sobel(img,-1,1,1)
lap = cv2.Laplacian(img,-1)

list_img = [img,sobelx,sobely,sobelxy,sobelxy2,lap] 
list_title = ['original','sobelx','sobely','sobelxy','sobelxy2','laplacian']

for i in range(len(list_img)):
    plt.subplot(2,3,1+i,xticks=[],yticks=[])
    plt.imshow(list_img[i],cmap='gray')
    plt.title(list_title[i])
plt.show()

