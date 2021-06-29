import cv2 
import numpy as np

cam = cv2.VideoCapture(0)

if not (cam.isOpened()):
    print("Could not open video device")

mi_logo = cv2.imread('logo.jpg')


mi_logo_reducido = cv2.resize(mi_logo, (90,60)) 
mi_logo_reducido_gris = cv2.cvtColor(mi_logo_reducido,cv2.COLOR_BGR2GRAY)
x,BG_Mask = cv2.threshold(mi_logo_reducido_gris,235,255,cv2.THRESH_BINARY)
FG_Mask = cv2.bitwise_not(BG_Mask)
FG=cv2.bitwise_and(mi_logo_reducido,mi_logo_reducido,mask=FG_Mask)


BW=90
BH=60
Xpos = 10
Ypos = 10
dX = 1
dY = 1 

while(True):    
    ret, frame = cam.read()      
    ROI = frame[Ypos:Ypos +BH, Xpos:Xpos+BW]
    ROI_BG = cv2.bitwise_and(ROI,ROI,mask=BG_Mask)
    new_ROI = cv2.add(FG,ROI_BG)
    
    frame[Ypos:Ypos+BH,Xpos:Xpos+BW] = new_ROI
    cv2.imshow('preview',frame)  

    Xpos = Xpos +dX
    Ypos = Ypos +dY
    if Xpos <= 0 or Xpos+BW>=640:
        dX=dX*(-1)
    if Ypos <= 0 or Ypos+BH>=480:
        dY=dY*(-1)


    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()