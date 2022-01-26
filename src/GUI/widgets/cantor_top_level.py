from tkinter import *
from typing import Dict
from src.interpreter.cantor_int import *


class Panel_Cantor(PanedWindow):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.values: Dict[str, Entry] = dict()
        self.e1 = self.create_line('Enter first int :')
        self.e2 = self.create_line('Enter second int :')
        self.send_button()
        self.res_lab = self.result()

    def create_line(self, text):
        pw = PanedWindow(self)
        label = Label(pw, text=text, justify='center')
        entry = Entry(pw)
        pw.pack()
        label.pack()
        entry.pack()
        return entry

    def send_button(self):
        def send():
            self.res_lab['text'] = f"Result = {Int.cantor(self.e1.get(), self.e2.get())}"
            return
        b = Button(self, text='Send', command=send)
        b.pack()

    def result(self):
        l = Label(self)
        l.pack()
        return l


def create_cantor_panel(parent):
    t = Toplevel(parent)
    Panel_Cantor(t).pack()
    t.mainloop()
