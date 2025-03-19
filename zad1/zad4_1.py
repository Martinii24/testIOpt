import cv2
import os

image_gray=cv2.imread("sadcat.jpg",cv2.IMREAD_GRAYSCALE)
directory="./testIOpt"
print("Before",os.listdir(directory))

cv2.imwrite("sadcat_gray.jpg",image_gray)
print("After",os.listdir(directory))

