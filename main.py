from threading import Thread, Event
from tkinter import *
from transformation import *
from screenObjects import ScreenObjects
from polygon import rect
import random


def main():
    objects = ScreenObjects()
    t1 = Thread(target=cv_app, args=[objects])
    t1.start()
    root = Tk()
    root.title('programa de transformação geometrica 2d')

    button = Button(root, text='Enviar', command=lambda: add(objects))
    button.pack()

    root.mainloop()
    t1.join()


def add(screenObjs: ScreenObjects):
    size = random.randrange(150, 400)
    new_poly = rect((0, 0), (size, size))
    new_poly.translate(random.randrange(SCREEN_WIDTH-size), random.randrange(SCREEN_HEIGHT-size))
    color = (random.randrange(100,255),random.randrange(100,255),random.randrange(100,255))
    new_poly.color = color
    screenObjs.polygons.append(new_poly)


if __name__ == '__main__':
    main()
