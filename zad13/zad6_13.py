import cv2

image = cv2.imread("skan.webp", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
cleaned = cv2.bitwise_not(closed)

cv2.imshow("Oryginalny", image)
cv2.imshow("Po otwarciu", cv2.bitwise_not(opened))
cv2.imshow("Po zamknięciu", cleaned)

cv2.waitKey(0)
cv2.destroyAllWindows()
