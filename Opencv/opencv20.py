import cv2
img = cv2.imread('Opencv/image/boy.jpg')

face_cascade = cv2.CascadeClassifier('Opencv/detect/haarcascade_frontalface_default.xml')

gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_detect = face_cascade.detectMultiScale(gray_img)

for (x,y,w,h) in face_detect :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow('original',img)
cv2.imshow('gray',gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()