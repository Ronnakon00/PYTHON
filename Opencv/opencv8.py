import cv2
cap = cv2.VideoCapture('Opencv/image/Video.mp4')

while(cap.isOpened()):
    ref , fream = cap.read()
    if (ref == True):
        gray = cv2.cvtColor(fream,cv2.COLOR_BGR2GRAY)
        cv2.imshow('output',gray)
        if (cv2.waitKey(1) & 0xFF == ord('e')):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()