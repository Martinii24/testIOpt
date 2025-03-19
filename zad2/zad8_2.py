import cv2
image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w , h )

cv2.imshow("Before", image)
image[99:100,0:cY,]=(0,255,0)


cv2.imshow("After", image)


cv2.waitKey()
