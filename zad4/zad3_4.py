import cv2
import numpy as np

image=cv2.imread("../sadcat.jpg")
cv2.imshow("Before",image)

height, width, channels = image.shape
print(f"Wysokość: {height} pikseli")
print(f"Szerokość: {width} pikseli")

M=np.float32([[1,0,150],[0,1,180]])
shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("After",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()

