import cv2
import imutils

image=cv2.imread("../sadcat.jpg")
cv2.imshow("Before",image)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("After",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
