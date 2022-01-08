import cv2
import numpy as np
import math


def seleccionaCarretera(imagen, umbral):
    
    imagen = imagen[int(imagen.shape[0] / 3):int(imagen.shape[0]) , ::]
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    b,g,r = cv2.split(imagen)
    h,s,v = cv2.split(hsv)
    blurry_s = cv2.blur(s, (7,7))
    blurry_v = cv2.blur(v, (7,7))
    _, binarizado_s = cv2.threshold(s, 50, 255, cv2.THRESH_BINARY_INV)
    return binarizado_s
    

video = cv2.VideoCapture('video_autovia_corto.mp4')
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        frameP = seleccionaCarretera(frame, 100)
        cv2.imshow('Frame100', frameP)
        

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()

cv2.destroyAllWindows()