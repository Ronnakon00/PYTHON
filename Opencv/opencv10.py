import cv2

img = cv2.imread('Opencv/image/cat.jpg')
imgresize = cv2.resize(img,(700,700))

cv2.arrowedLine(imgresize,(0,0),(100,100),(255,0,0),5)

cv2.imshow('output',imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()