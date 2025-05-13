
import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")

pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(triangle, circle)
bitwiseOr = cv2.bitwise_or(triangle, circle)
bitwiseXor = cv2.bitwise_xor(triangle, circle)
bitwiseNot = cv2.bitwise_not(circle)

cv2.imshow("NOT", bitwiseNot)
cv2.imshow("XOR", bitwiseXor)
cv2.imshow("AND", bitwiseAnd)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
cv2.destroyAllWindows()