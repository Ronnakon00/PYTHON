import cv2
cap = cv2.VideoCapture('Opencv/image/Walking.mp4')

check1 , fream1 = cap.read()
check2 , fream2 = cap.read()
while cap.isOpened() :
    if check1 == True :
        motion = cv2.absdiff(fream1,fream2)
        gray_fream = cv2.cvtColor(motion,cv2.COLOR_BGR2GRAY)
        thresh , result = cv2.threshold(gray_fream,10,255,cv2.THRESH_BINARY)
        contour , hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        
        for contours in contour:
            (x,y,w,h) = cv2.boundingRect(contours)
            if cv2.contourArea(contours) < 888 :
                continue
            else:
                cv2.rectangle(fream1,(x,y),(x+w,y+h),(0,0,255),4)

        cv2.imshow('result',fream1)

        fream1 = fream2
        check2 , fream2 = cap.read()
        if (cv2.waitKey(1) == ord('e')):
            break

    else :
        break

cap.release()
cv2.destroyAllWindows()