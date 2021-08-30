import cv2 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)
# plt.imshow(blank_img)
cv2.rectangle(blank_img,pt1=(10,100),pt2=(110,200),color=(0,255,0),thickness=-1) # 2 edge in diagonal, thickness = -1 means fill
cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,255,0),thickness = 10) # drawing a square
cv2.circle(blank_img,center=(100,400),radius=50,color = (150,150,150),thickness=5)
cv2.line(blank_img,pt1=(0,0),pt2=(500,500),color=(0,0,255),thickness=5)
# add text with fonts
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,"openCV",org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)
#polygons demo
blank_img_1 = np.zeros(shape=(550,550,3),dtype=np.uint16)
plt.imshow(blank_img_1)
plt.show()