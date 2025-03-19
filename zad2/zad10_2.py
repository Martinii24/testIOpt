import cv2
image = cv2.imread('image.jpg')

(b, g, r)=image[50,50]
(b1, g1, r1)=image[200,200]

b,g,r=int(b),int(g),int(r)
b1,g1,r1=int(b1),int(g1),int(r1)

br=abs(b-b1)
gr=abs(g-g1)
rr=abs(r-r1)

print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
print("Różnica - Red: {}, Green: {}, Blue: {}".format(rr, gr, br))

