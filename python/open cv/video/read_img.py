import cv2 as cv
img=cv.imread('photo/cat_large.jpg',0)# for gray image give flag as 0
cv.imshow('Cat',img)
#resize of the image
res=cv.resize(img,None,fx=0.25,fy=0.25,interpolation=cv.INTER_AREA)
cv.imshow('resize',res)
cv.waitKey(0)