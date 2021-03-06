# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan GÖKBEL
# @File : adaptif_treshold.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('sudoku.jpg',0)    # 0 görüntüyü gray scale yapıyor
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)       # 127 den alt tonlar 0 siyah üst değerler 1 beyaz olcak
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

basliklar = ["orjinal","THRESH_BINARY","ADAPTIVE_THRESH_MEAN_C","ADAPTIVE_THRESH_GAUSSIAN_C"]
resimler = [img,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()













