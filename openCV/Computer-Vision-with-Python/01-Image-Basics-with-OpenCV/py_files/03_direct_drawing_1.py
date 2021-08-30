import cv2
import matplotlib.pyplot as plt
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),10,(255,0,255),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
    

cv2.namedWindow('interact_draw')
cv2.setMouseCallback('interact_draw',draw_circle)

img = np.zeros(shape=(512,512,3),dtype= np.uint8)
winname_ = 'interact_draw'
while True:
    cv2.imshow(winname_,img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
