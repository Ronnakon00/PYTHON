import cv2

cap = cv2.VideoCapture('Opencv/image/Mark.mp4')
eye_cascade = cv2.CascadeClassifier('Opencv/detect/haarcascade_eye_tree_eyeglasses.xml')

while(cap.isOpened):
    ref , fream = cap.read()
    if(ref == True):
        gray_fream = cv2.cvtColor(fream,cv2.COLOR_BGR2GRAY)
        eye_detect = eye_cascade.detectMultiScale(gray_fream,1.3,4)
        for (x,y,w,h) in eye_detect:
            cv2.rectangle(fream,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.imshow('output',fream)

        if(cv2.waitKey(1) == ord('e')):
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()