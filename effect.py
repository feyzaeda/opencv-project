import cv2
import numpy as np

image = cv2.imread("lenna256.jpg")
image_blue = cv2.imread("lenna256.jpg")
image_green = cv2.imread("lenna256.jpg")
image_red = cv2.imread("lenna256.jpg")
image_purple = cv2.imread("lenna256.jpg")
image_effect = cv2.imread("lenna256.jpg")

cv2.imshow("Lenna",image)

# 0-->Blue
# 1-->Green
# 2-->Red

image_purple[:,:,0] = 200 #goruntuye blue değeri verir
image_purple[:,:,1] = 80 #goruntuye green degeri verir
image_purple[:,:,0] = 150 #goruntuye red degeri verir
cv2.imshow("Lenna purple effect",image_purple)
cv2.imwrite("lenna_purple.jpg",image_purple)

image_blue[:,:,0] = 255 #goruntuye mavi efekt verir
cv2.imshow("Lenna blue effect",image_blue)

image_green[:,:,1] = 255 #goruntuye yesil efekt verir
cv2.imshow("Lenna green effect",image_green)

image_red[:,:,2] = 255 #goruntuye kirmizi efekt verir
cv2.imshow("Lenna red effect",image_red)

image_effect[120:145,115:185,0]=200 #belirtilen alana verilen blue degerini uygular
image_effect[120:145,115:185,1]=80 #belirtilen alana verilen green degerini uygular
cv2.imshow("Lenna effect",image_effect)
cv2.imwrite("lenna_effect.jpg",image_effect)


cv2.waitKey(0)
cv2.destroyAllWindows()