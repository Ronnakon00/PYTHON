import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 

result = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ref , fream = cap.read()
    if (ref == True):
        cv2.imshow('output',fream)
        result.write(fream)
        if (cv2.waitKey(1) & 0xFF == ord('e')):
            break
    else :
        break

result.release()
cap.release()
cv2.destroyAllWindows()