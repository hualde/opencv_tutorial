import cv2 

flag = 0

def mouse_click(event, x, y, flags, param):
    global x1,y1,x2,y2
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
       
    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        flag=1

cam=cv2.VideoCapture(0)
cv2.namedWindow('image')                    #importante, si no no va
cv2.setMouseCallback('image', mouse_click)

cv2.namedWindow('roi')  

while(True):       
    ret, frame = cam.read()
    #cv2.imshow('image',frame)        
    if flag == 1:
        cv2.rectangle (frame,(x1,y1),(x2,y2),(255,0,0),2)
        roi = frame[y1:y2,x1:x2]
        cv2.imshow('roi', roi) 
    cv2.imshow('image',frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cam.release()
cv2.destroyAllWindows()