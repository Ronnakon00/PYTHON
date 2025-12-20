import cv2

img = cv2.imread('Opencv/image/ant.jpg',0)

def display(value):
    print(value) 

cv2.namedWindow('output')
cv2.createTrackbar('value','output',128,255,display)

while True:
    val = cv2.getTrackbarPos('value','output')
    thresh , result = cv2.threshold(img,val,255,cv2.THRESH_BINARY)
    cv2.imshow('output',result)
    if cv2.waitKey(1) == ord('e'):
        break

cv2.destroyAllWindows()