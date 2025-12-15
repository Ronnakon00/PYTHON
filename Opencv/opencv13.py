import cv2

img = cv2.imread('Opencv/image/cat.jpg')
imgresize = cv2.resize(img,(700,700))

cv2.putText(imgresize,"Ronny",(200,200),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,255),cv2.LINE_AA)

cv2.imshow('output',imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()