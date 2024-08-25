import cv2 as cv
import numpy as np
from polygon import rect, polygon


def main():
    image = np.zeros((500, 500, 3), np.uint8)

    p1 = (100, 50)
    p3 = (200, 150)

    rect1 = rect(p1, p3)
    rect1.rotate(40)
    rect1.translate(50, 50)
    rect1.show(image, (0, 255, 0))
    rect1.scale(2)
    rect1.show(image, (255, 0, 0))

    cv.imshow('image', image)
    cv.waitKey(0)



if __name__ == "__main__":
    main()
