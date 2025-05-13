import cv2
import numpy as np

image=cv2.imread("sadcat.jpg")

M = np.ones(image.shape, dtype="uint8") - 80
subtracted = cv2.subtract(image, M)

cv2.imshow("Darker", subtracted)
cv2.imshow("Original",image)
cv2.waitKey()