import cv2

rotation=int(input("rotacja: "))

image=cv2.imread("sadcat.jpg")
cv2.imshow("Original",image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), rotation, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow(f"Rotated by {rotation} Degrees", rotated)
cv2.waitKey()



