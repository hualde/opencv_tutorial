import cv2 

image = cv2.imread('img/alo.jpg')

while(True):    
    
    #cv2.imshow('Alonso en Alpine',image)

    print(image.shape)
    gris = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Alonso en Alpine_gris',gris)
    print(gris.shape)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('Alonso en Alpine_hsv',hsv)
    print(hsv.shape)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break