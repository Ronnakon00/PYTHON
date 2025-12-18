import cv2
img = cv2.imread('Opencv/image/boy.jpg')

cv2.imshow('original',img)

face_cascade = cv2.CascadeClassifier('Opencv/detect/haarcascade_frontalface_default.xml')


cv2.waitKey(0)
cv2.destroyAllWindows()