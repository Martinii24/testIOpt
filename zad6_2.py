import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)
print(cX,cY)



image[cY-50:cY+50, cX-50:cX+50] = (0, 0, 255)
cv2.imshow("Updated", image)
cv2.waitKey(0)
