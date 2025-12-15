import cv2
cap = cv2.VideoCapture('Opencv/image/Video.mp4')

while(cap.isOpened()):
    ref , fream = cap.read()
    if (ref == True):
        cv2.imshow('output',fream)
        if (cv2.waitKey(1) & 0xFF == ord('e')):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()