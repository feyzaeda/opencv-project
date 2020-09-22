import cv2
import numpy as numpy

image = cv2.imread("lenna256.jpg")

cv2.imshow("Lenna",image)
print(image)#matris gorunumu 

print("sol ust koseden 230 piksel asagi ve 80 piksel sağındaki pikselin RGB degeri ",image[(230,80)])


cv2.waitKey(0)
cv2.destroyAllWindows()