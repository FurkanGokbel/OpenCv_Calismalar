# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan Gökbel
# @File : Bulanıklastırma.py
# @Software: PyCharm
import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (1):
    ret, frame = kamera.read()
    # Renk filitrelemede HSV uzayında calısmak daha kolaylık sağlayacaktır.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dusuk_beyaz = np.array([0, 0,140])  # girilen renk icin alt üst renk aralığı tanımlanıp sadece o renk değerini geçirme işlemi yapılıyor
    ust_beyaz = np.array([256, 60, 256])

    mask = cv2.inRange(hsv, dusuk_beyaz, ust_beyaz)
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)


    kernel = np.ones((15,15),np.float32) / 225       # resmi 15x15 pixel aralıklarla bulanıklastırcaz
    smoothed = cv2.filter2D(son_resim,-1,kernel)
    blur = cv2.GaussianBlur(son_resim,(15,15),0)
    median = cv2.medianBlur(son_resim,(15))
    biliteral = cv2.bilateralFilter(son_resim,15,75,75)


    cv2.imshow('orjinal', frame)
    cv2.imshow('son', son_resim)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('biliteral',biliteral)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()










