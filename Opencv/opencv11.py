import cv2

img = cv2.imread('Opencv/image/cat.jpg')
imgresize = cv2.resize(img,(700,700))

cv2.rectangle(imgresize,(0,0),(100,200),(0,0,255),5)#ใส่-1แทนตัวสุดท้ายจะละบายกล่องข้างในทั้งหมด

cv2.imshow('output',imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()