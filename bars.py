import cv2 

def cb(m):      #no hace nada
    pass

cam=cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('xval','image',0,640,cb)
cv2.createTrackbar('yval','image',0,480,cb)
cv2.createTrackbar('anchura_rectangulo','image',0,100,cb)
cv2.createTrackbar('altura_rectangulo','image',0,100,cb)

if not (cam.isOpened()):
    print("Could not open video device")

while(True):       
    ret, frame = cam.read()      
    valor_de_x = cv2.getTrackbarPos('xval','image')
    valor_de_y = cv2.getTrackbarPos('yval','image')
    valor_de_anchura = cv2.getTrackbarPos('anchura_rectangulo','image')
    valor_de_altura = cv2.getTrackbarPos('altura_rectangulo','image')
    cv2.rectangle(frame,(valor_de_x,valor_de_y),(valor_de_x+valor_de_anchura,valor_de_y+valor_de_altura),(0,255,0),2)

    cv2.imshow('image',frame)  
    cv2.moveWindow('image',0,0)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
cam.release()
cv2.destroyAllWindows()