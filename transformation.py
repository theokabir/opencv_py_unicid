import cv2
import numpy as np
from screenObjects import ScreenObjects

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800


def cv_app(screenObjects: ScreenObjects):
    img = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), np.uint8)
    cv2.namedWindow('image')
    while True:
        cv2.imshow('image', img)
        for form in screenObjects.polygons:
            form.show(img)

        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break
