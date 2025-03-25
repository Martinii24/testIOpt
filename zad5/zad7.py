import imutils
import cv2

image=cv2.imread("sadcat.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotatedWr = cv2.warpAffine(image, M, (w, h))

rotatedIm = imutils.rotate(image, 60)
cv2.imshow("ImmultisRotate", rotatedIm)
cv2.imshow("WrapAffine", rotatedWr)

cv2.waitKey()



