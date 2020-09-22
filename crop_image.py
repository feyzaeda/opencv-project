import cv2
import numpy as np

image = cv2.imread("lenna256.jpg")
cv2.imshow("Lenna",image)

cropped_image = image[100:200,100:200] #belirtilen alani kirpar
cv2.imshow("cropped lenna",cropped_image)
cv2.imwrite("cropped_lenna.jpg",cropped_image)

new_image = cv2.imread("lenna256.jpg")
new_image[0:100,0:100] = cropped_image #belirtilen alana kirpilmis goruntuyu ekler
cv2.imshow("new lenna",new_image)
cv2.imwrite("new_lenna.jpg",new_image)


cv2.waitKey(0)
cv2.destroyAllWindows()