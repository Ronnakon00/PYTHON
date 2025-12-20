import cv2
img = cv2.imread('Opencv/image/map.jpg',0)

thresh , rh1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
rh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
rh3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow('result1',rh1)
cv2.imshow('result2',rh2)
cv2.imshow('result3e',rh3)

cv2.waitKey(0)
cv2.destroyAllWindows()