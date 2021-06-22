import cv2 

cam=cv2.VideoCapture(0)

if not (cam.isOpened()):
    print("Could not open video device")
while(True):    
    # Capture frame-by-frame    
    ret, frame = cam.read()      
    # Display the resulting frame    
    cv2.imshow('preview',frame)  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()

print("xxxxxxxx")