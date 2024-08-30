from tkinter import *
from screenObjects import ScreenObjects
from polygonForm import PolygonForm


def mainForm(screenObject: ScreenObjects):
    root = Tk()
    root.title('programa de transformação geometrica 2d')
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(screenObject, root))
    root.geometry('400x150')

    value_inside = StringVar(root)
    value_inside.set("select an option")

    values = ['quadrado', 'triangulo', 'seta', 'estrela']

    question_menu = OptionMenu(root, value_inside, *values)
    question_menu.pack()

    button = Button(root, text='Criar', command=lambda: add(value_inside.get(), screenObject))
    button.pack()

    root.mainloop()


def add(value, screenObjs: ScreenObjects):
    if not value == 'select an option':
        PolygonForm(value, screenObjs)


def on_closing(screenObjs: ScreenObjects, root: Tk):
    screenObjs.closed = True
    root.destroy()

