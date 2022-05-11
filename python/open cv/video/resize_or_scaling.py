import cv2 as cv
cap=cv.VideoCapture('video/dog.mp4')
def rescaleframe(frame,scale=0.75):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv.resize(frame , dimension ,interpolation=cv.INTER_AREA)

while True:
    ret,frame = cap.read() #ret is boolean

    frame_resized=rescaleframe(frame)
    cv.imshow('Video',frame)
    cv.imshow('Resized Video',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()