import tkinter as tk

from tkinter.scrolledtext import ScrolledText


class Texte(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, width=20, height=10,
                         bg="lightgrey", wrap='word')
        self.pack(expand=True, fill='both')
        self.add_text('This is an exemple text')

    def add_text(self, txt: str):
        self.insert(tk.END, txt)

    def clean(self):
        self.delete(0, tk.END)

    def add_clean(self, txt: str):
        self.clean()
        self.add_text(txt)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")

    root.iconphoto(False, tk.PhotoImage(file='../ressources/img/ramen.png'))
    root.geometry("640x480")

    Texte(root)

    root.mainloop()
