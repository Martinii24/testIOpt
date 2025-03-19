
import cv2
image=cv2.imread("sadcat.jpg",0)
cv2.namedWindow("Display",cv2.WINDOW_AUTOSIZE)
cv2.imshow('Display',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
