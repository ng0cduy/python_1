import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img[:170,:] = 0,0,0
img[171:340,:] = 0,0,255
img[341:,:] = 0,255,255
cv2.line(img,(0,0),(512,512),(255,255,255),4)
cv2.rectangle(img,(0,0),(100,50),(128,128,128),-1) #thickness = -1 : filled
cv2.circle(img,(350,100),50,(255,0,0),-1)
cv2.putText(img,"test1",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
cv2.imshow("Image",img)
cv2.waitKey(0)