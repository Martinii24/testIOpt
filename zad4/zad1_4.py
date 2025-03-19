import cv2
import numpy as np

image=cv2.imread("../sadcat.jpg")
cv2.imshow("Original",image)

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
