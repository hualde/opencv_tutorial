import face_recognition
import cv2
print(cv2.__version__)

seema_image = face_recognition.load_image_file('/home/hualde-jetson/p_m_w/opencv_tutorial/face_recognizer/demoImages/known/Seema Verma.jpg')
#ahora hay que aprenderla, encodear
seema_encoding = face_recognition.face_encodings(seema_image)[0]

donald_image = face_recognition.load_image_file('/home/hualde-jetson/p_m_w/opencv_tutorial/face_recognizer/demoImages/known/Donald Trump.jpg')
#ahora hay que aprenderla, encodear
donald_encoding = face_recognition.face_encodings(donald_image)[0]

Encoding = [seema_encoding, donald_encoding]
Names = ['Seema', 'Donald Trampas']

font = cv2.FONT_HERSHEY_SIMPLEX
test_image = face_recognition.load_image_file('/home/hualde-jetson/p_m_w/opencv_tutorial/face_recognizer/demoImages/unknown/u10.jpg')
facePositions = face_recognition.face_locations(test_image)
allEncodings = face_recognition.face_encodings(test_image, facePositions)

test_image = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)

while(True):
    

    for (top, right, bottom, left), face_encoding in zip(facePositions, allEncodings):
        name = 'Unknow Person'
        matches = face_recognition.compare_faces(Encoding, face_encoding)
        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]
        cv2.rectangle(test_image,(left,top),(right,bottom),(0,0,255),4)
        cv2.putText(test_image,name,(left,top-6),font,2,(255,0,255),3)
        resized = cv2.resize(test_image, (640,480), interpolation = cv2.INTER_AREA)
        cv2.imshow('window', resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        cv2.destroyAllWindows()
        break
    