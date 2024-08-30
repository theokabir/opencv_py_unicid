from threading import Thread
from transformation import *
from screenObjects import ScreenObjects
from mainForm import mainForm


def main():
    objects = ScreenObjects()
    t1 = Thread(target=cv_app, args=[objects])
    t1.start()
    mainForm(objects)
    t1.join()


if __name__ == '__main__':
    main()
