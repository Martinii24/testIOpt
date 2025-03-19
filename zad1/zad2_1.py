import cv2

image=cv2.imread("sadcat.jpg")

(h,w,c)=image.shape[:3]

print(f"Height:{h} pixels",)
print(f"Width: {w} pixels",)
print("Channels: ",c)
