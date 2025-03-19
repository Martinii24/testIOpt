import cv2
import numpy as np

canvas=np.zeros((300,300,3),dtype="uint8")
red=(0,0,255)
cv2.rectangle(canvas,(100,100),(200,200),red)
cv2.circle(canvas,(150,150),30,red)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)