import cv2
import numpy as np

image=cv2.imread("sadcat.jpg")

brightened = image + 150
brightened = np.clip(brightened, 0, 255).astype(np.uint8)

cv2.imshow("Original",image)
cv2.imshow("Brightened Image (NumPy)", brightened)
cv2.waitKey()