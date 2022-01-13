import cv2
import numpy as np
import math


def seleccionaCarretera(imagen):
    grayscale = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    ret, binarizado = cv2.threshold(grayscale, 175, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(binarizado, 100, 200)
    lines = cv2.HoughLines(canny, 1, np.pi / 180, 150, None, 0, 0)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(imagen, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    cv2.imshow("binarizado", imagen)
    return binarizado

video = cv2.VideoCapture('video_autovia_corto.mp4')
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        frameP = seleccionaCarretera(frame)
        cv2.imshow('Frame100', frameP)
        

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()

cv2.destroyAllWindows()