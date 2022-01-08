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


class main_class:
    def __init__(self, root) -> None:
        self.root = root
        self.initiate()

    def initiate(self):
        self.createMenu(self, root)

    def createMenu(self, x, parent):
        self.menu_bar = tk.Menu(parent)

        # The 'File' contextual menu
        self.menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(label="New", command=lambda: print("New"))
        self.menu_file.add_command(label="Open", command=lambda: print("Open"))
        self.menu_file.add_command(label="Save", command=lambda: print("Save"))

        self.menu_file.add_separator()
        self.menu_file.add_command(label="Exit", command=lambda: print("Exit"))
        self.menu_bar.add_cascade(label="File", menu=self.menu_file)

        # The 'Run' contextual menu
        self.menu_run = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_run.add_command(
            label="Run 1 instruction", command=lambda: print("1"))
        self.menu_run.add_command(
            label="Run file", command=lambda: print("Whole file"))
        self.menu_bar.add_cascade(label="Run", menu=self.menu_run)

        # The 'Stop' contextual menu
        self.menu_stop = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_stop.add_command(
            label="Stop execution", command=lambda: print("Stopped"))
        self.menu_bar.add_cascade(label="Stop", menu=self.menu_stop)

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(
            label="User manual", command=lambda: print("test"))
        self.menu_help.add_command(
            label="About", command=lambda: print("test2"))

        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        parent.config(menu=self.menu_bar)


def main(root):
    main_class(root)
    Texte(root)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")
    root.iconphoto(False, tk.PhotoImage(file='img/ramen.png'))
    # root.geometry("640x480")

    main(root)

    root.mainloop()
