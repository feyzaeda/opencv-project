import cv2
import numpy as numpy

image = cv2.imread("lenna256.jpg")

image[50,40] = [256,256,256]

for i in range(200):
    image[70,i] = [255,255,255]

cv2.imshow("Lenna",image)
cv2.imwrite("lenna-rgb.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()