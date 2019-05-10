# -*- coding: utf-8 -*-

# @Author : Muhammed Furkan GÖKBEL
# @File : Canny_Edge_Detection_2.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('messi.jpg',0)   # 0 parametresi ile görüntüyü direk gray scale almıs oluyoruz
esik1 = 50
esik2 = 80
edge = cv2.Canny(image,esik1,esik2)     # 100 200 eşik değerleridir.



plt.subplot(121),plt.imshow(image,cmap='gray')
plt.title('orjinal'),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(edge,cmap='gray')
plt.title('Canny Edge'),plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()















