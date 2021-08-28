import cv2
import numpy as np

img = cv2.imread("Resources/cards_1.jpg")
print(img.shape[:2])
width, height = 250, 350
pts1 = np.float32([[60,84], [251,67], [290,289], [75,312]])
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
# cv2.circle(img,(111,219),5,(255,0,0),-1)
# cv2.circle(img,(287,188),5,(0,255,0),-1)
# cv2.circle(img,(154, 482),5,(0,0,255),-11)
cv2.imshow("Image", img)
cv2.imshow("3 heart", imgOutput)
cv2.waitKey(0)