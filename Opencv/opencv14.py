import cv2
import datetime

cap = cv2.VideoCapture('Opencv/image/Video.mp4')
while(cap.isOpened):
    ref , fream = cap.read()
    if(ref == True):
        current = str(datetime.datetime.now())
        cv2.putText(fream,current,(5,25),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0))
        cv2.imshow('output',fream)
        if(cv2.waitKey(1) == ord('e')):
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()