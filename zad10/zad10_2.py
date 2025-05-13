import numpy as np
import cv2

image1 = cv2.imread("kot1.jpg")
image2 = cv2.imread("kot2.png")

min_height = min(image1.shape[0], image2.shape[0])
min_width = min(image1.shape[1], image2.shape[1])

image1_resized = cv2.resize(image1, (min_width, min_height))
image2_resized = cv2.resize(image2, (min_width, min_height))

bitwiseXor = cv2.bitwise_xor(image1_resized, image2_resized)

cv2.imshow("XOR", bitwiseXor)

cv2.waitKey(0)
cv2.destroyAllWindows()
