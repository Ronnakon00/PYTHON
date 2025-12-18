import cv2
img = cv2.imread('Opencv/image/cat.jpg')
imgresize = cv2.resize(img,(400,400))

def clickpos(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        text = str(blue)+","+str(green)+","+str(red)
        cv2.putText(imgresize,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),cv2.LINE_4)
        cv2.imshow('output',imgresize)

cv2.imshow('output',imgresize)
cv2.setMouseCallback('output',clickpos)

cv2.waitKey(0)
cv2.destroyAllWindows()