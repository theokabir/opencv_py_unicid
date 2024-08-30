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
            case 'quadrado': n_form = square(300)
            case 'triangulo': n_form = triangle(300)
            case 'seta': n_form = arrow(300)
            case 'estrela': n_form = star(300)
            case 'gama': n_form = gama(300)

        if n_form is None:
            self.destroy()

        n_form.color = randColor()
        screenObjects.polygons.append(n_form)

        Label(self, text=f'criando um {form}').pack()

        # scale function
        scale_value = DoubleVar()
        scale_value.set(1)
        Scale(self, from_=.1, to=4.0,
              resolution=0.1,
              variable=scale_value,
              orient=HORIZONTAL,
              length=300).pack()

        def scale():
            n_form.scale(float(scale_value.get()))
            scale_value.set(1)

        Button(self, text='scale', command=scale).pack()

        # translate
        x_translate_value = IntVar()
        x_translate_value.set(0)
        y_translate_value = IntVar()
        y_translate_value.set(0)

        Scale(self, from_=-600, to=600,
              resolution=1,
              variable=x_translate_value,
              orient=HORIZONTAL,
              length=300).pack()

        Scale(self, from_=-600, to=600,
              resolution=1,
              variable=y_translate_value,
              orient=HORIZONTAL,
              length=300).pack()

        def transform():
            n_form.translate(int(x_translate_value.get()), int(y_translate_value.get()))
            x_translate_value.set(0)
            y_translate_value.set(0)

        Button(self, text='translate', command=transform).pack()

        # rotate
        rotate_value = IntVar()
        rotate_value.set(0)
        Scale(self, from_=-360, to=360,
              resolution=1,
              variable=rotate_value,
              orient=HORIZONTAL,
              length=300).pack()

        def rotate():
            n_form.rotate(rotate_value.get())
            rotate_value.set(0)

        Button(self, text='rotate', command=rotate).pack()

        value_inside = StringVar(self)
        value_inside.set("select an option")

        values = ['X', 'Y', 'Opposite']

        question_menu = OptionMenu(self, value_inside, *values)
        question_menu.pack()

        def mirror():
            n_form.reflextion(value_inside.get())

        Button(self, text='reflect', command=mirror).pack()


def randColor():
    return randrange(100, 255), randrange(100, 255), randrange(100, 255)
