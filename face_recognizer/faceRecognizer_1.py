import face_recognition
import cv2
print(cv2.__version__)

image = face_recognition.load_image_file('/home/hualde-jetson/p_m_w/opencv_tutorial/face_recognizer/demoImages/unknown/u13.jpg')

face_locations = face_recognition.face_locations(image)
print (face_locations)

while(True):
    cv2.namedWindow('ventana')
    rgb = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

    for (row1,col1,row2,col2) in face_locations:
        cv2.rectangle(rgb,(col1,row1),(col2,row2),(0,0,255), 3)
        resized = cv2.resize(rgb, (320,240), interpolation = cv2.INTER_AREA)
        cv2.imshow('ventana',resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        cv2.destroyAllWindows()
        break
    