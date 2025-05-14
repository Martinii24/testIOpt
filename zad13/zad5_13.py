import cv2

image = cv2.imread("logo.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel_shapes = {
    "Kwadrat": cv2.MORPH_RECT,
    "Krzyż": cv2.MORPH_CROSS,
    "Elipsa": cv2.MORPH_ELLIPSE
}

kernel_size = (5, 5)

for name, shape in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape, kernel_size)

    erosion = cv2.erode(binary, kernel, iterations=1)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow(f"{name} - Erozja", erosion)
    cv2.imshow(f"{name} - Dylatacja", dilation)
    cv2.imshow(f"{name} - Otwarcie", opening)
    cv2.imshow(f"{name} - Zamknięcie", closing)
    cv2.imshow(f"{name} - Gradient", gradient)

cv2.imshow("Oryginalny", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
