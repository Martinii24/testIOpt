import cv2

image_gray=cv2.imread("sadcat.jpg",cv2.IMREAD_GRAYSCALE)

(h,w)=image_gray.shape

print("Channels: 1")
cv2.imshow("Image", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
