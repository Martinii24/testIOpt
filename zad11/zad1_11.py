import cv2
import numpy as np
image=cv2.imread("osoba.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (200, 100), (600, 450), 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey()
cv2.destroyAllWindows()