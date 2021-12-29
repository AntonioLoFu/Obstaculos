import cv2
import numpy as np
import math


def seleccionaCarretera(imagen, umbral):
    
    #imagen = imagen[340:582, ::]
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    b,g,r = cv2.split(imagen)
    h,s,v = cv2.split(hsv)
    #sInverted = cv2.bitwise_not(s)
    blurry = cv2.blur(s, (5,5))
    #binarizado = cv2.adaptiveThreshold(blurry,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,5,6)
    ret, binarizado = cv2.threshold(blurry, umbral, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.imshow("binarizado", binarizado)
    dilatado = cv2.dilate(binarizado, kernel, iterations = 4)
    dilatado = cv2.bitwise_not(dilatado)
    h_mascara = cv2.bitwise_and(b, dilatado)
    s_mascara = cv2.bitwise_and(g, dilatado)
    v_mascara = cv2.bitwise_and(r, dilatado)
    mascara = cv2.merge([h_mascara,s_mascara,v_mascara])
    return mascara

video = cv2.VideoCapture('switzerland.mp4')
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        frameP = seleccionaCarretera(frame, 100)
        frameP2 = seleccionaCarretera(frame, 125)
        frameP3 = seleccionaCarretera(frame, 150)
        frameP4 = seleccionaCarretera(frame, 175)
        frameP5 = seleccionaCarretera(frame, 200)
        cv2.imshow('Frame100', frameP)
        cv2.imshow('Frame125', frameP2)
        cv2.imshow('Frame150', frameP3)
        cv2.imshow('Frame175', frameP4)
        cv2.imshow('Frame200', frameP5)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()

cv2.destroyAllWindows()