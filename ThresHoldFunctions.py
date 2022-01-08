import cv2
import numpy as np

def calculaThreshMedia(frame):
    return int(np.mean(frame))


def calculaThreshCarretera(frame):
    return np.mean(frame[280:320, 30:70]) + 50

