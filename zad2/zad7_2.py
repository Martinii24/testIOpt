import cv2
image = cv2.imread('image.jpg')


(h, w) = image.shape[:2]
(cX, cY) = (w // 3, h // 3)
center = image[cX:2*cX, cY:2*cY]
cv2.imshow("Center", center)

cv2.waitKey()