import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Opencv/image/girl.jpg')
cv2.imshow('result',img)

img_cvt = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img_cvt)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
