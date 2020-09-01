import cv2
import face_recognition

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    faces = detector(frame)

    print(faces)

    if ret:
        cv2.imshow("My screen", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
