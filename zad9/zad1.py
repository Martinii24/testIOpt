import cv2
import numpy as np

image=cv2.imread("sadcat.jpg")

M = np.ones(image.shape, dtype="uint8") * 50
added = cv2.add(image, M)

cv2.imshow("Original", image)
cv2.imshow("Lighter", added)
cv2.waitKey()