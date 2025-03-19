import cv2
import numpy as np

image=cv2.imread("photo.jpg")
red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)
height, width, channels = image.shape

print(f"Wysokość: {height} pikseli")
print(f"Szerokość: {width} pikseli")


cv2.circle(image,(225,115),20,red,-1)
cv2.circle(image,(285,115),20,red,-1)
cv2.rectangle(image,(220,165),(295,185),green,-1)
cv2.circle(image,(255,120),100,blue,3)

cv2.imshow("Image",image)
cv2.waitKey(0)