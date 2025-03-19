import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)
#print(cX,cY)
(b, g, r) = image[400, 262]
print("Pixel at the middle(400, 262) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

