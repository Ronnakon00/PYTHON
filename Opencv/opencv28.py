import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('Opencv/image/gradient.png')

thresh,result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh,result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh,result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh,result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh,result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

# cv2.imshow('Original',gray_img)
# cv2.imshow('Binary',result1)
# cv2.imshow('Binary inv',result2)
# cv2.imshow('Trunc',result3)
# cv2.imshow('Tozero',result4)
# cv2.imshow('Tozero inv',result5)
images = [gray_img,result1,result2,result3,result4,result5]
title = ['origin','binary','binary inv','trunc','tozero','tozero inv']

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()