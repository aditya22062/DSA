import cv2 as cv
cap=cv.VideoCapture('video/dog.mp4')#use 0 for webcam 
while True:
    ret,frame = cap.read() #ret is boolean


    cv.imshow('Video',frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()