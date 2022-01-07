import tkinter as tk

from tkinter.scrolledtext import ScrolledText

class Texte(tk.Text):
    def __init__(self, parent):
        # self = tk.Text(root)

        self = ScrolledText(parent, width=20, height=10, bg="lightgrey", wrap="none")


        self.grid(row=0, column=0, sticky="nsew")
        self.insert(tk.END, 'This is an example text.')
        self.pack(expand=True, fill='both')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")

    root.iconphoto(False, tk.PhotoImage(file='../ressources/img/ramen.png'))
    root.geometry("640x480")

    Texte(root)

    root.mainloop()

