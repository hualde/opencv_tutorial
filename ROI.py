import cv2 

cam=cv2.VideoCapture(0)

if not (cam.isOpened()):
    print("Could not open video device")
while(True):      
    ret, frame = cam.read()
    cv2.imshow('preview',frame)      
    ROI = frame[50:190,140:300].copy()
    cv2.imshow('roi',ROI)
    gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gris',gris)  
    
    ROI_gris = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)
    cv2.imshow('roi_gris',ROI_gris)
    ROI_color = cv2.cvtColor(ROI_gris,cv2.COLOR_GRAY2BGR) #es necesaria esta conversion(no convierte, 
    cv2.imshow('roi_color',ROI_color)                     #colores eliminados) para insertarla en el frame 
    frame[50:190,140:300] = ROI_color
    cv2.imshow('preview2',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()