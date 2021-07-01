import cv2
import numpy as np 

cam=cv2.VideoCapture(0)
cv2.namedWindow('tracks')

def cb(x):
    pass

cv2.createTrackbar('hueLow','tracks',20,179,cb)
cv2.createTrackbar('hueHigh','tracks',150,179,cb)
cv2.createTrackbar('satLow','tracks',20,255,cb)
cv2.createTrackbar('satHigh','tracks',220,255,cb)
cv2.createTrackbar('valLow','tracks',30,255,cb)
cv2.createTrackbar('valHigh','tracks',235,255,cb)

while(True):     
    ret, frame = cam.read()      
    #cv2.imshow('bgr',frame)  
    #print(frame.shape)

    imagen_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.moveWindow('hsv',0,0)
    cv2.imshow('hsv',frame)
    #print(imagen_hsv.shape) 

    hl = cv2.getTrackbarPos('hueLow','tracks')
    hH = cv2.getTrackbarPos('hueHigh','tracks')
    sl = cv2.getTrackbarPos('satLow','tracks')
    sH = cv2.getTrackbarPos('satHigh','tracks')
    vl = cv2.getTrackbarPos('valLow','tracks')
    vH = cv2.getTrackbarPos('valHigh','tracks')

    lb=np.array([hl,sl,vl])
    ub=np.array([hH,sH,vH])

    masked = cv2.inRange(imagen_hsv,lb,ub)
    cv2.imshow('masked',masked)
    #print(imagen_hsv.shape)

    bit_and = cv2.bitwise_and(frame, frame, mask=masked)
    cv2.imshow('bit_and',bit_and)


    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()