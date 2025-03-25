import imutils
import cv2

image=cv2.imread("sadcat.jpg")
for i in range(0,360,15):
    rotated = imutils.rotate(image, i)
    cv2.imshow("Rotated",rotated)
    cv2.waitKey(50)







