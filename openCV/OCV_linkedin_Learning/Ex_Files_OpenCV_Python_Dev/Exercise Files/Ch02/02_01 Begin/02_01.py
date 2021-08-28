import numpy
import cv2
import os
root_path = os.getcwd()
print(root_path)
img = cv2.imread(f"{root_path}/opencv-logo.png")
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imwrite('output_img',img)
# print(img)