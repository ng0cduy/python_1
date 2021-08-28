import cv2
import os

from getdir import *
# LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/Doraemon.png"
# )
# # DISPLAY
# cv2.imshow("Resources/Doraemon",img)
# cv2.waitKey(0)

# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#          break

# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)    #width
# cap.set(4, frameHeight)   #height
# cap.set(10,100)   #brightness
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break
