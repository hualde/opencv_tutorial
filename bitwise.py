import cv2 
import numpy as np

cam=cv2.VideoCapture(0)
if not (cam.isOpened()):
    print("Could not open video device")

img1 = np.zeros((480,640,1),np.uint8)           #"1" ya q va a ser en escala de grises, en color sería 3
img1[0:480,0:320] = (255)                       #le damos color blanco 
                       
img2 = np.zeros((480,640,1),np.uint8)
img2[190:290,290:370] =(255)

bitAND=cv2.bitwise_and(img1,img2)

bitOR=cv2.bitwise_or(img1,img2)

bitXOR=cv2.bitwise_xor(img1,img2)
while(True):       
    ret, frame = cam.read()        
    
    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    cv2.imshow('bitAND',bitAND)
    cv2.imshow('bitOR',bitOR)
    cv2.imshow('bitXOR',bitXOR)
    masked = cv2.bitwise_and(frame,frame,mask=img2)
    cv2.imshow('preview',masked)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()