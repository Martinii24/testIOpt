import cv2

image1=cv2.imread("sadcat_gray.jpg")
image2=cv2.imread("sadcat.jpg")
cv2.imshow("Image",image1)
cv2.imshow("Image1",image2)

cv2.waitKey()


