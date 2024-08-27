import cv2 as cv
import numpy as np
from polygon import rect, polygon, REFLECTION_AXIS


def main():
    image = np.zeros((800, 1500, 3), np.uint8)

    p1 = (100, 50)
    p2 = (200, 150)

    rect1 = rect(p1, p2)
    rect1.rotate(40)
    rect1.translate(50, 50)
    rect1.scale(4)
    rect1.show(image, (255, 0, 0))

    n_form = np.array([
        (0, 0),
        (200, 0),
        (100, 100),
        (200, 200),
        (0, 200)
    ])

    n_poly = polygon(n_form)
    n_poly.translate(500, 300)
    n_poly.reflextion(REFLECTION_AXIS.DOWN)
    n_poly.show(image, color=(255, 255, 0))

    cv.imshow('image', image)
    cv.waitKey(0)



if __name__ == "__main__":
    main()
