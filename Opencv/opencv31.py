import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('Opencv/detect/haarcascade_frontalface_default.xml')

while(True):
    ref , fream = cap.read()
    fream_gray = cv2.cvtColor(fream,cv2.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(fream_gray,1.3,5)
    
    for (x,y,w,h) in face_detect :
        cv2.rectangle(fream,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('original',fream)

    if (cv2.waitKey(1) == ord('e')):
        break

cap.release()
cv2.destroyAllWindows()