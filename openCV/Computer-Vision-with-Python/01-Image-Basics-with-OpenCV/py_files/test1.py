import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


img = cv2.imread("D:/Git_WS/python_1/openCV/Computer-Vision-with-Python/DATA/dog_backpack.jpg")
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
flip_img = cv2.flip(img_fix,0)
rec_img = cv2.rectangle(img_fix,(200,380),(600,720),(255,0,0),10)
poly_pts = np.array([[400,400],[170,700],[600,700]],np.int32)
poly_img = cv2.polylines(img=img_fix,pts=[poly_pts],color=(0,0,255),isClosed=True,thickness=10)
plt.imshow(img_fix)
plt.show()
