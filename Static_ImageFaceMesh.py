import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

FaceMesh = FaceMeshDetector(maxFaces=2,minDetectionCon=0.5,minTrackCon=0.5)
img = cv2.imread("women.png")
Image,faces = FaceMesh.findFaceMesh(img)

if faces:
    print(faces[0])


cv2.imshow("Image",Image)
cv2.imwrite("FaceMesh.jpg",Image)
cv2.waitKey(0)
cv2.destroyAllWindows()






