import cv2

image = cv2.imread("sadcat.jpg")
kernelSizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    blurred1 = cv2.GaussianBlur(image, (kX, kY), 0)
    blurred2 = cv2.medianBlur(image, kX)
    cv2.imshow("Median {}".format(9), blurred2)
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred1)
cv2.waitKey(0)