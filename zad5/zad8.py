import imutils
import cv2

image=cv2.imread("sadcat.jpg")
rotated=image
for i in range(3):
    rotated = imutils.rotate(rotated, 30)
rotated1 = imutils.rotate_bound(image, 90)

cv2.imshow("Sekwencyjny", rotated)
cv2.imshow("Rotated by 90 Degrees", rotated1)

cv2.waitKey()



