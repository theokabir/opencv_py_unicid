import cv2 as cv
import numpy as np
from screenObjects import ScreenObjects
from constants import *


def cv_app(screenObjects: ScreenObjects):
    cv.namedWindow('image')
    while True:
        img = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), np.uint8)
        for form in screenObjects.polygons:
            form.show(img)

        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('q') or screenObjects.closed:
            cv.destroyAllWindows()
            break
