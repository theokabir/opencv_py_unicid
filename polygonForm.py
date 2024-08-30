from tkinter import *
from screenObjects import ScreenObjects
from polygon import *
from random import randrange


class PolygonForm(Toplevel):
    def __init__(self, form: str, screenObjects: ScreenObjects):
        super().__init__()
        self.title(f"new {form}")
        self.geometry('500x500')

        # criar forma
        n_form = None
        match form:
            case 'quadrado':
                n_form = square(300)
            case 'triangulo':
                n_form = triangle(300)

        if n_form is None:
            self.destroy()

        n_form.color = randColor()
        screenObjects.polygons.append(n_form)

        Label(self, text=f'criando um {form}').pack()

        # scale function
        scale_value = DoubleVar()
        scale_value.set(1)
        scale_label = Label(self, text=f'{scale_value.get()}')
        Scale(self, from_=-4.0, to=4.0,
              resolution=0.1,
              variable=scale_value,
              command=lambda x: scale_label.config(text=scale_value.get()),
              orient=HORIZONTAL).pack()
        scale_label.pack()
        Button(self, text='scale',
               command=lambda: screenObjects.polygons[screenObjects.getFormIndex(n_form.id)]
               .scale(float(scale_value.get()))).pack()


def randColor():
    return randrange(100, 255), randrange(100, 255), randrange(100, 255)
