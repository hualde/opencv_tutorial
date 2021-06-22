import cv2
import numpy as np

coord=[]
evento =-1
img = np.zeros((150,150,3),dtype=np.uint8)
def mouse_click(event, x, y, flags, param): #event devuelve 1 al hacer LBUTTON_DOWN
    global puntos
    global evento
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos = (x,y)
        evento = event
        coord.append(puntos)
        print(coord) 

    if event == cv2.EVENT_RBUTTONDOWN:
        azul = frame[y,x,0]     #row,column,color--->frame
        verde = frame[y,x,1]
        rojo = frame[y,x,2]
        img[:]=[azul,verde,rojo]

        
        font =cv2.FONT_HERSHEY_PLAIN
        texto = str(azul)+','+ str(verde)+','+ str(rojo)
        cv2.putText(img, texto,(10,10),font,1,(0,255,0))
        cv2.imshow('color_picker',img)

cam=cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_click)

if not (cam.isOpened()):
    print("Could not open video device")

while(True):      
    ret, frame = cam.read()
    for coords in coord:
        cv2.circle(frame, coords, 10,(255,0,0),4) 
    cv2.imshow('image',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    if cv2.waitKey(1) & 0xFF == ord('c'):    
        coord=[]
cam.release()
cv2.destroyAllWindows()