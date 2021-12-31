import cv2
import numpy as np
import math



def seleccionaCarretera(imagen, umbral):
    
    imagen = imagen[int(imagen.shape[0] / 3):int(imagen.shape[0]) , ::]
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    _,binarizado_v = cv2.threshold(v, 200, 255, cv2.THRESH_BINARY)
    _,binarizado_s = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY_INV)
    mascara_and_no_dilatado= cv2.bitwise_and(binarizado_v, binarizado_s)
    lineas = cv2.HoughLinesP(mascara_and_no_dilatado, 10, np.pi/180, 100, minLineLength=20, maxLineGap=50)
    for line in lineas:
        x1, y1, x2, y2 = line[0]
        if not (abs(x1 - x2) > 100):
            cv2.line(imagen, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv2.imshow("mascara_and_no_dilatado", mascara_and_no_dilatado)
    cv2.imshow("lineas", imagen)
    return mascara_and_no_dilatado

video = cv2.VideoCapture('video_autovia_corto.mp4')
size = (int(video.get(3)), int(video.get(4)))
resultado = cv2.VideoWriter('mascara_autovia.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        
        frameP = seleccionaCarretera(frame, 100)
        resultado.write(frameP)
        cv2.imshow('mascara', frameP)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
resultado.release()
cv2.destroyAllWindows()