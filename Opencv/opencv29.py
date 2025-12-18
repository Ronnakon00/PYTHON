import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Opencv/image/ant.jpg',0)

thresh_value = [50,100,130,200,230]

plt.subplot(2,3,1,xticks=[],yticks=[])
plt.title('original')
plt.imshow(img,cmap="gray")

for i in range(len(thresh_value)):
    thresh,result = cv2.threshold(img,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(2,3,2+i)
    plt.title('%d'%thresh_value[i])
    plt.imshow(result,cmap='gray')
    plt.xticks=([]),plt.yticks([])


plt.show()