import tkinter as tk


class texte(tk.Text):
    """ This class is for the text entry. """

    def __init__(self, parent):
        super().__init__(parent, width=20, height=10,
                         bg="lightgrey", wrap='word', fg='#000')

    def add_text(self, txt: str):
        self.insert(tk.END, txt)

    def clean(self):
        self.delete('1.0', tk.END)

    def add_clean(self, txt: str):
        self.clean()
        self.add_text(txt)
