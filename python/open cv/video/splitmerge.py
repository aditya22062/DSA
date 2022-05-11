import cv2 as cv
import numpy as np

img= cv.imread('photo/park.jpg')
cv.imshow('Color',img)
#split
b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('red',r)
cv.imshow('green',g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

#merge
merge=cv.merge([b,g,r])
cv.imshow('merge',merge)

#to display the image in blue red green 
#first we create blank 
blank=np.zeros(img.shape[:2],dtype=np.uint8)
cv.imshow('blank',blank)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('red',red)
cv.imshow('green',green)
cv.waitKey(0)