from tkinter import *
from typing import Dict
from src.interpreter.cantor_int import *


def create_line(self, text):
    pw = PanedWindow(self)
    label = Label(pw, text=text, justify='center')
    entry = Entry(pw, justify='center')
    pw.pack()
    label.pack()
    entry.pack()
    return entry


class Panel_Cantor_Encode(PanedWindow):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.values: Dict[str, Entry] = dict()
        self.e1 = create_line(self, 'Enter first int :')
        self.e2 = create_line(self, 'Enter second int :')
        self.send_button()
        self.res_lab = self.result()

    def create_line(self, text):
        pw = PanedWindow(self)
        label = Label(pw, text=text, justify='center')
        entry = Entry(pw, justify='center')
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


class Panel_Cantor_Decode(PanedWindow):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.values: Dict[str, Entry] = dict()
        self.e1 = create_line(self, 'Enter int to decode')
        self.send_button()
        self.res_lab = self.result()

    def send_button(self):
        def send():
            self.res_lab['text'] = f"Result = <{Int(self.e1.get()).left()}, {Int(self.e1.get()).right()}>"
            return
        b = Button(self, text='Send', command=send)
        b.pack()

    def result(self):
        l = Label(self)
        l.pack()
        return l


def create_cantor_panel(parent, is_encode):
    t = Toplevel(parent)
    t.title("Encode" if is_encode else "Decode")
    Panel_Cantor_Encode(
        t).pack() if is_encode else Panel_Cantor_Decode(t).pack()
    t.mainloop()
