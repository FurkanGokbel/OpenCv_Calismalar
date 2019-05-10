# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan GÖKBEL
# @File : Threshold1.py
# @Software: PyCharm

# Eşik değeri belirleyip o değerin altını siyah yada beyaz olara ayarlayabiliyoruz.
import cv2
import numpy
from matplotlib import pyplot as plt


img = cv2.imread('gradient.jpg')
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)    # resimde 127 den 255 olan kısımları alıyoruz   255 beyaz 0 siyah
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

basliklar = ['orjinal','binary','binary_inv','trunc','tozero','tozero_inv']
resimler = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()





