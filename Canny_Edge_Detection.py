# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan GÖKBEL
# @File : Canny_Edge_Detection.py
# @Software: PyCharm

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)    # Dahili Kamera çağırılıyor

while (1):
    ret,frame = kamera.read()
    # Renk filitrelemede HSV uzayında calısmak daha kolaylık sağlayacaktır.
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dusuk_beyaz = np.array([0,0,140])       # girilen renk icin alt üst renk aralığı tanımlanıp sadece o renk değerini geçirme işlemi yapılıyor
    ust_beyaz = np.array([256, 60, 256])


    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    kenarlar = cv2.Canny(frame,50,100)

    mask = cv2.inRange(hsv,dusuk_beyaz,ust_beyaz)
    son_resim = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('orjinal', frame)
    cv2.imshow('Canny', kenarlar)
    # cv2.imshow('Laplacian', laplacian)
    # cv2.imshow('sobelX',sobelx)
    # cv2.imshow('sobelY', sobely)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()


























