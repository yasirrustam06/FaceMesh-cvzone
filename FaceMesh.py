import cv2
import cvzone
import time

from cvzone.FaceMeshModule import FaceMeshDetector
face_mesh = FaceMeshDetector(maxFaces=2,minDetectionCon=0.5,minTrackCon=0.5)

cap = cv2.VideoCapture(0)


while True:
    ret,img = cap.read()

    Image , faceMesh =  face_mesh.findFaceMesh(img)

    if faceMesh:
        print(faceMesh[0])
    cv2.imshow("Image",Image)
    if cv2.waitKey(1) & 0xFF == ord("B"):
        break


cap.releas()
cap.destroyAllWindows()
