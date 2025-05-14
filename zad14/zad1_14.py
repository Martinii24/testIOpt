import cv2

image=cv2.imread("sadcat.jpg")

blurred = cv2.blur(image, (9, 9))
blurred1 = cv2.GaussianBlur(image, (9, 9), 0)
blurred2 = cv2.medianBlur(image, 9)
blurred3 = cv2.bilateralFilter(image, 11, 41, 21)
cv2.imshow("Median {}".format(9), blurred2)
cv2.imshow("Average ({}, {})".format(9, 9), blurred)
cv2.imshow("Gaussian ({}, {})".format(9, 9), blurred1)
cv2.imshow("Bilateral", blurred3)
cv2.waitKey()