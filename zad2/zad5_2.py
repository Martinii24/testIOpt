import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]

image[0:cY, 0:cX] = (255, 0, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)