import cv2
import numpy as np

img = np.zeros((200,200,3),np.uint8)
cv2.namedWindow('Color Trackbar')

def display(value):
    print(value)

cv2.createTrackbar('B','Color Trackbar',0,255,display)
cv2.createTrackbar('G','Color Trackbar',0,255,display)
cv2.createTrackbar('R','Color Trackbar',0,255,display)

while(True):
    cv2.imshow("Show color",img) 

    blue = cv2.getTrackbarPos('B','Color Trackbar')
    green = cv2.getTrackbarPos('G','Color Trackbar')
    red = cv2.getTrackbarPos('R','Color Trackbar')

    img[:]=[blue,green,red]

    if(cv2.waitKey(1) == ord('e')):
        break

cv2.destroyAllWindows()