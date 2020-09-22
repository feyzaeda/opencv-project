import cv2
import numpy as np
#cok boyutlu diziler ve matrisler uzerinde daha hizli islem yaptirir.

image = cv2.imread("lenna256.jpg")
#goruntuyu okudu
image2 = cv2.imread("lenna256.jpg",0)
#okudugu goruntuyu siyah-beyaz olacak sekilde degistirdi

cv2.imshow("Lenna",image)
cv2.imshow("Lenna black-white",image2)
#goruntuleri gosterdi

cv2.imwrite("lenna-black-white.jpg",image2)
#siyah beyaz olan goruntuyu dosyaya yazdi

cv2.waitKey(0)
#kapanması icin bir tusa basilmasini bekler
cv2.destroyAllWindows()
#(x) basildiğinda acilan tum pencereleri kapatirs