import cv2 as cv

img=cv.imread('photo/cat.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)#Converted in gray scale
#Blur
img1=cv.imread('photo/park.jpg')
cv.imshow('Original',img1)
blur=cv.GaussianBlur(img1,(3,3),cv.BORDER_DEFAULT)#(3,3) is kernel size and increasing this will increase the blur and this should be odd
cv.imshow('Blur',blur)
#edge in the image
canny=cv.Canny(blur,125,175)
cv.imshow('Edge',canny)
#Crop
cropped=img1[100:200,200:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)