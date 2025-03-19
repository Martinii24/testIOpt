import cv2

image = cv2.imread("image.jpg")

max_brightness = -1
max_coords = (0, 0)
r, g, b = 0, 0, 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        (b1, g1, r1) = image[i, j]


        brightness = (r1 + g1 + b1) / 3

        if brightness > max_brightness:
            max_brightness = brightness
            max_coords = (i, j)
            r, g, b = r1, g1, b1

print(f"The brightest pixel is at coordinates {max_coords} with Red: {r}, Green: {g}, Blue: {b}, Brightness: {max_brightness}")
