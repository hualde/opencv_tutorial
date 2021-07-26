import cv2 

image = cv2.imread('img/opencv.jpg')

while(True):    
    
    cv2.imshow('logo',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break

     

