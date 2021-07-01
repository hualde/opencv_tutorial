import cv2
import numpy as np 

cam=cv2.VideoCapture(0)
cv2.namedWindow('tracks')

def cb(x):
    pass

cv2.createTrackbar('hueLow','tracks',15,179,cb)
cv2.createTrackbar('hueHigh','tracks',85,179,cb)
cv2.createTrackbar('satLow','tracks',141,255,cb)
cv2.createTrackbar('satHigh','tracks',248,255,cb)
cv2.createTrackbar('valLow','tracks',56,255,cb)
cv2.createTrackbar('valHigh','tracks',255,255,cb)

while(True):     
    ret, frame = cam.read()      
    #cv2.imshow('bgr',frame)  
    #print(frame.shape)

    imagen_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.imshow('hsv',imagen_hsv)
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

    #bit_not = cv2.bitwise_not(bit_and)
    #print(bit_not.shape)
    #cv2.imshow('bit_not',bit_not)

    contours,_= cv2.findContours(masked, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of Contours found = " + str(len(contours)))
    for cnt in contours:
        c_area = cv2.contourArea(cnt)
        if c_area > 50:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            
    cv2.imshow('bgr',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()