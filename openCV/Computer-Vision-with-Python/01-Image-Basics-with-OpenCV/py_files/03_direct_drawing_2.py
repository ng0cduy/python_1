import cv2
# import matplotlib.pyplot as plt
import numpy as np
# true while mouse button down, false while mouse button up
ix,iy = -1,-1
drawing = False
def draw_rectangle(event,x,y,flags,param):
    '''
    add rectangle at the point it clicked and then expand
    '''
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),color = (0,0,255),thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)


img = np.zeros(shape=(512,512,3),dtype= np.uint8)

cv2.namedWindow('interact_draw')
cv2.setMouseCallback('interact_draw',draw_rectangle)

while True:
    cv2.imshow('interact_draw',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()