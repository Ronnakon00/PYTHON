import cv2
img = cv2.imread('Opencv/image/cat.jpg')

cv2.imshow('cat',img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()
