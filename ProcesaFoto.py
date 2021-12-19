import cv2
import numpy as np

def procesaFoto(foto):


    frame = cv2.imread(foto,0)
    size = frame.shape
    print(size)

    pFrame = frame[340:582, ::]
    frame = frame[340:582, ::]


   #_, pFrame = cv2.threshold(pFrame, calculaLimite(), 255, cv2.THRESH_BINARY)
    pFrame = cv2.adaptiveThreshold(pFrame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,5,6)

    # Creating kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
    kernelAlbertosubnormal = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8,8))

    #Using cv2.erode() method 
    pFrame = cv2.erode(pFrame, kernel) 
    pFrame = cv2.dilate(pFrame, kernel2, iterations = 1) 
    #pFrame = cv2.erode(pFrame, kernelAlbertosubnormal) 

    
    cv2.imshow('frame',cv2.add(frame, pFrame))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def calculaLimite():
    return 200


procesaFoto("Prueba2.JPG")