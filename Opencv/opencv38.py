import cv2

img = cv2.imread('Opencv/image/currency.jpg',0)

cannyim = cv2.Canny(img,50,200)

cv2.imshow('result',img)
cv2.imshow('canny',cannyim )

cv2.waitKey(0)
cv2.destroyAllWindows()