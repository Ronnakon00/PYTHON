import cv2
img = cv2.imread('Opencv/image/cat.jpg',0)
imgresize = cv2.resize(img,(400,400))

cv2.imwrite('out5.png',imgresize)