# Использование потока .jpg видео с веб-камеры Android IP (проверено) в Python2 OpenCV3

import urllib
import urllib.request
import cv2
import numpy as np
import time

# Замените URL на свой собственный IPwebcam shot.jpg IP:порт
# url = 'http://172.20.211.16:8080/shot.jpg'
url = 'http://172.20.201.169:8080/shot.jpg'

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    # Numpy для преобразования в массив
    imgResp = urllib.request.urlopen(url)

    # Наконец, декодируйте массив в пригодный для использования формат OpenCV ;)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

    # поместить изображение на экран
    img = cv2.imdecode(imgNp, -1)

    # put the image on screen
    cv2.imshow('IPWebcam', img)

    # Чтобы меньше нагружать процессор
    # время.сна(0.1)

    # Выйти, если нажата q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# # Numpy для преобразования в массив
# imgResp = urllib.request.urlopen(url)
#
# # Наконец, декодируйте массив в пригодный для использования формат OpenCV ;)
# imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
#
# # # поместить изображение на экран
# img = cv2.imdecode(imgNp, -1)
#
# # put the image on screen
# cv2.imshow('IPWebcam', img)
#
# # Чтобы меньше нагружать процессор
# # время.сна(0.1)
#
# # Выйти, если нажата q
