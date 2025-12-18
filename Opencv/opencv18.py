import cv2
import numpy

img = numpy.zeros([400,400,3])
point = list()

def clickpos(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),10,(0,0,255),5)
        point.append((x,y))
        print(point)
        if(len(point) >= 2):
            cv2.line(img,point[-2],point[-1],(0,255,0),4)
        cv2.imshow('output',img)
        
cv2.imshow('output',img)
cv2.setMouseCallback('output',clickpos)

cv2.waitKey(0)
cv2.destroyAllWindows()