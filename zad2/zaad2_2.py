import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

image[524, 799] = (0, 0, 255)
(b, g, r) = image[524, 799]

cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()