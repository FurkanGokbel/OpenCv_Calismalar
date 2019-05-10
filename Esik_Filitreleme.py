# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan Gökbel
# @File : Esik_Filitreleme.py
# @Software: PyCharm
import cv2
import numpy as np


img = cv2.imread('sayfa.jpg')
ret,th1 = cv2.threshold(img,25,255,cv2.THRESH_BINARY)   # 0 siyah 255 beyaz 55 değerinin altındaki tüm değerleri 0 ladı siyah yaptı
cv2.imwrite('th1.jpg',th1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     # görüntüyü gray scale yapıyoruz
ret,th2 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)  # best
ret,otsu = cv2.threshold(gray,12,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow('orjinal',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('gauss',gauss)
cv2.imshow('otsu',otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()























