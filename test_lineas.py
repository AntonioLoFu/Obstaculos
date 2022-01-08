import cv2
import numpy as np


def determinaROI(imagen):
    imagen = imagen[int(imagen.shape[0] / 5):int(imagen.shape[0]) , ::]
    #ELEGIMOS LOS PUNTOSA ADECUADOS PARA LA PERSPECTIVA DE LA IMAGEN
    left_bottom_point = (0,int(4*imagen.shape[0]/5))
    right_bottom_point = (imagen.shape[1],int(4*imagen.shape[0]/5))
    left_top_point = (0,1*int(imagen.shape[0] /5))
    right_top_point = (imagen.shape[1],1*int(imagen.shape[0] /5))
    #AÑADIMOS ADEMAS EL LOS PÍXELES DEL BORDE DE LA IMAGEN
    points = [left_top_point,left_bottom_point, (0,imagen.shape[0]), (imagen.shape[1],imagen.shape[0]),right_bottom_point, right_top_point]

    #CREAMOS UNA MÁSCARA QUE SELECCIONE EL POLÍGONO ANTERIOR
    mascara = np.zeros((imagen.shape[0], imagen.shape[1]))
    cv2.fillConvexPoly(mascara, np.array([points]), 1)
    mascara = mascara.astype(np.bool)
    resultado = np.zeros_like(imagen)
    resultado[mascara] = imagen[mascara]
    return resultado
 


def detectaObstaculos(frame1, imagen):
    #CONVERTIMOS LA IMAGEN EN HSV PARA PODER REALIZAR UN MEJOR TRATAMIENTO
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    blurry = cv2.blur(s, (5,5))

    #BINARIZAMOS CON UN UMBRAL DE 100 QUE ES EL QUE NOS HA DADO MEJOR RESULTADO
    _, binarizado = cv2.threshold(blurry, 100, 255, cv2.THRESH_BINARY)

    #DILATAMOS LA IMAGEN CON UNA ELIPSE PARA PODER RELLENAR LOS ESPACIOS NEGROS
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    dilatado = cv2.dilate(binarizado, kernel, iterations = 3)
    #INVERTIMOS LA MÁSCARA
    dilatado = cv2.bitwise_not(dilatado)
    
    #EXTRAEMOS LOS CONTORNOS
    contours, _ = cv2.findContours(dilatado,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imagen, contours, -1, (0,255,0), 3)

    #FILTRAMOS LOS CONTORNOS POR TAMAÑO Y CREAMOS UN RECTÁNGULO MÍNIMO QUE LOS CONTENGA
    for cnt in contours:
        if 300 < cv2.contourArea(cnt) < 2000:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),3)

    return (imagen, binarizado) #DEVOLVEMOS LA IMAGEN TRAS EL PROCESADO Y EL BINARIZADO QUE NOS SERVIRÁ PARA MOSTRARLO EN LA INTERFAZ

#ESTA FUNCIÓN RECIBE UN FRAME DE UN VIDEO, LO PROCESA Y LO DEVUELVE
def procesaFrame(frame):
    frameP = determinaROI(frame)[int(frame.shape[0]/3):frame.shape[0] , ::]
    resultado = detectaObstaculos(frameP, frameP)[0]
    frame[frame.shape[0] - frameP.shape[0] : frame.shape[0], ::] = resultado
    return frame
        