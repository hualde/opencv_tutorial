import cv2
print(cv2.__version__)
import numpy as np
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)

pan=0
tilt=30
kit.servo[0].angle=pan
kit.servo[1].angle=tilt

def nothing(x):
    pass

cam=cv2.VideoCapture(0)
width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('width:',width,'height:',height)
face_cascade = cv2.CascadeClassifier('cascades/face.xml')
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        objX=x+w/2
        objY=y+h/2
        errorPan=objX-width/2
        errorTilt=objY-height/2
        if abs(errorPan)>15:
            pan=pan-errorPan/75
        if abs(errorTilt)>15:
            tilt=tilt+errorTilt/75


        if pan>180:
            pan=180
            print("Pan Out of  Range")   
        if pan<0:
            pan=0
            print("Pan Out of  Range") 
        if tilt>180:
            tilt=180
            print("Tilt Out of  Range") 
        if tilt<0:
            tilt=0
            print("Tilt Out of  Range")                 

        kit.servo[0].angle=pan
        kit.servo[1].angle=tilt 
        break        

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()