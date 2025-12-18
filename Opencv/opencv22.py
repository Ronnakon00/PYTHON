import cv2

img = cv2.imread('Opencv/image/girl.jpg')
eye_cascade = cv2.CascadeClassifier('Opencv/detect/haarcascade_eye_tree_eyeglasses.xml')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eye_detect = eye_cascade.detectMultiScale(gray_img)

for(x,y,w,h) in eye_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)

cv2.imshow('wdasd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()