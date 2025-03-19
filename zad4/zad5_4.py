import cv2
import imutils

tX=int(input("Przesuniecie tX: "))
tY=int(input("Przesuniecie tY: "))

image=cv2.imread("../sadcat.jpg")

shifted=imutils.translate(image,tX,tY)
cv2.imshow("Before",image)
cv2.imshow("After",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
