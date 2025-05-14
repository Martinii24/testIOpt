import cv2
import numpy as np

image=cv2.imread("logo.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)

cv2.imshow("Original",image)
cv2.waitKey()