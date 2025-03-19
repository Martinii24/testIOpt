import cv2
while(True):
    try:

        height= int(input("Wysokosc: "))
        if(height>=524 or height<0):
            print("Błędna wart")
            continue
        width=int(input("Szerokosc: "))
        if (width >= 799 or width<0):
            print("Błędna wart")
            continue

        else:
             break
    except ValueError:
        print("Value error")


image = cv2.imread('image.jpg')
image[height,width] = (0, 0, 0)
(b, g, r) = image[height,width]
print("Pixel: - Red: {}, Green: {}, Blue: {}".format(r, g, b))
cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()