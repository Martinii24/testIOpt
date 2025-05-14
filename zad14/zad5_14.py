import cv2
import numpy as np

image = cv2.imread('logo.png')

noise = np.zeros_like(image, dtype=np.int16)
cv2.randn(noise, 0, 30)
noisy_image = image.astype(np.int16) + noise
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

blurred = cv2.blur(image, (9, 9))
blurred1 = cv2.GaussianBlur(image, (9, 9), 0)
blurred2 = cv2.medianBlur(image, 9)
blurred3 = cv2.bilateralFilter(image, 11, 41, 21)
cv2.imshow("Median {}".format(9), blurred2)
cv2.imshow("Average ({}, {})".format(9, 9), blurred)
cv2.imshow("Gaussian ({}, {})".format(9, 9), blurred1)
cv2.imshow("Bilateral", blurred3)

cv2.imshow("Original", image)
cv2.imshow("Gaussian Noise", noisy_image)
cv2.waitKey(0)

