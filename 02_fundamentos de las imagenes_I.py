import cv2 
import numpy as np

image = cv2.imread('img/logo_opencv.jpg')
imagen_reducida = cv2.resize(image, (640, 480))
while(True):    
    
    cv2.imshow('logo',image)


    ceros = np.zeros((480,320,3),dtype=np.uint8)
    
    print(ceros.shape)

    ceros[0:50,0:100] = 255
    cv2.imshow('ceros', ceros)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break

     

