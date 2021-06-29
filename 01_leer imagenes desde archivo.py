import cv2 

image = cv2.imread('img/alo.jpg')

while(True):    
    
    cv2.imshow('Alonso en Alpine',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break

     

