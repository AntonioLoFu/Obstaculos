import cv2
import numpy as np
import math

def calculaUmbral(value):
    
    p1 = int(value.shape[1]/2)
    p2 = value.shape[0] - int(value.shape[0]/10)
    area_carretera = value[p1-20:p1, p2:p2 + 20]
    min = np.min(area_carretera)
    print(min)

    return min + 10

def seleccionaCarretera(imagen, umbral):
    
    #imagen = imagen[340:582, ::]
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    b,g,r = cv2.split(imagen)
    h,s,v = cv2.split(hsv)
    #sInverted = cv2.bitwise_not(s)
    blurry = cv2.blur(s, (5,5))
    #binarizado = cv2.adaptiveThreshold(blurry,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,5,6)
    umbral = calculaUmbral(s)

    ret, binarizado = cv2.threshold(blurry, 100, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.imshow("binarizado", binarizado)
    cv2.imshow("value", v)
    dilatado = cv2.dilate(binarizado, kernel, iterations = 2)
    dilatado = cv2.bitwise_not(dilatado)
    h_mascara = cv2.bitwise_and(b, dilatado)
    s_mascara = cv2.bitwise_and(g, dilatado)
    v_mascara = cv2.bitwise_and(r, dilatado)
    mascara = cv2.merge([h_mascara,s_mascara,v_mascara])
    return mascara

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