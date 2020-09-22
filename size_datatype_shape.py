import cv2
import numpy as np

image = cv2.imread("lenna256.jpg")
cv2.imshow("Lenna",image)
print(image.dtype) #veri tipini gosteririr
print(image.shape) #goruntunun  seklini(genislik,yukseklik,kanal sayisi) gosterir
print(image.size) #gountunun boyutunu (genislik*yukseklik*kanal sayisi) gosterir
#goruntu renkli oldugu icin kanal sayisi 3(RGB)tur

image2 = cv2.imread("lenna256.jpg",0)#tek kanal kullanilinca görüntü siyah beyaz oluyor
cv2.imshow("Lenna black white",image2)
print(image2.dtype)
print(image2.shape)#tek kanal kullanildigi icin (genislik,yukseklik) 
print(image2.size)#tek kanal kullanildigi icin (genislik*yukseklik)


cv2.waitKey(0)
cv2.destroyAllWindows()