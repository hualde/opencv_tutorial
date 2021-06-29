import cv2 
import numpy as np

image = cv2.imread('img/alo.jpg')
imagen_reducida = cv2.resize(image, (640, 480))
while(True):    
    
    cv2.imshow('Alonso en Alpine',image)
    #print(image.shape)
    #cv2.imshow('Alonso en Alpine_reducida',imagen_reducida)
    #print(imagen_reducida.shape)

    ceros = np.zeros((480,320,3),dtype=np.uint8)
    cv2.imshow('ceros', ceros)
    print(ceros.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break

     

