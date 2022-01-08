from tkinter import filedialog, ttk
import tkinter as tk

from tkinter.scrolledtext import ScrolledText


class Texte(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, width=20, height=10,
                         bg="lightgrey", wrap='word')
        self.add_text('This is an exemple text')

    def add_text(self, txt: str):
        self.insert(tk.END, txt)

    def clean(self):
        self.delete('1.0', tk.END)

    def add_clean(self, txt: str):
        self.clean()
        self.add_text(txt)


class main_class:
    def __init__(self, root) -> None:
        self.root = root
        self.initiate()

    def initiate(self):
        self.createMenu(self, root)
        self.createNotebook(root)
        self.text_editor.pack(expand=True, fill='both')

    def createMenu(self, x, parent):
        self.menu_bar = tk.Menu(parent)

        # The 'File' contextual menu
        self.menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(
            label="New", command=lambda: self.new_file())
        self.menu_file.add_command(
            label="Open", command=lambda: self.open_file())
        self.menu_file.add_command(
            label="Save", command=lambda: self.save_file())

        self.menu_file.add_separator()
        self.menu_file.add_command(
            label="Exit", command=lambda: root.destroy())
        self.menu_bar.add_cascade(label="File", menu=self.menu_file)

        # The 'Run' contextual menu
        self.menu_run = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_run.add_command(
            label="Run 1 instruction", command=lambda: print("1"))
        self.menu_run.add_command(
            label="Run file", command=lambda: print("Whole file"))
        self.menu_bar.add_cascade(label="Run", menu=self.menu_run)

        # The 'Stop' button
        """self.menu_stop = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_stop.add_command(
            label="Stop execution", command=lambda: print("Stopped"))
        self.menu_bar.add_cascade(label="Stop", menu=self.menu_stop)"""
        self.menu_bar.add_command(
            label="Stop", command=lambda: print("Stopped"))

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(
            label="User manual", command=lambda: print("test"))
        self.menu_help.add_command(
            label="RAM instructions", command=lambda: print("test2"))
        self.menu_help.add_command(
            label="About", command=lambda: print("test3"))

        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        parent.config(menu=self.menu_bar)

    def new_file(self):
        self.acc += 1
        self.titles.append('Untitled'+str(self.acc))
        self.tab2 = tk.Frame()
        self.frame2 = tk.Frame(self.notebook)
        self.text_editor2 = Texte(self.frame2)
        self.notebook.add(self.frame2, text=self.titles[1])
        self.text_editor2.pack(expand=True, fill='both')
        self.text_editor2.clean()

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            title="Select File",
            filetypes=(("Text files",
                        "*.txt*"),
                       ("All files",
                        "*.*")))
        if self.filename != '':
            self.read_file(self.filename)

    def read_file(self, path):
        f = open(path, "r")
        self.text_editor.add_clean(f.read())
        f.close()

    def save_file(self):
        try:
            self.filename
        except AttributeError:
            file = filedialog.asksaveasfile(
                defaultextension='.txt', filetypes=(("Text files",
                                                    "*.txt*"),
                                                    ("All files",
                                                    "*.*")),
                initialfile='RAM.txt')
            if file != None:
                self.filename = file.name
            else:
                self.filename = ''

        program_text = self.text_editor.get('1.0', tk.END)
        if self.filename != '':
            f = open(self.filename, "w")
            f.write(program_text)
            f.close
            self.notebook.tab(0, text=self.filename.split('/')[-1])

    def createNotebook(self, parent):
        self.acc = 1
        self.notebook = ttk.Notebook(parent)
        self.tab = tk.Frame()
        self.frame = tk.Frame(self.notebook)
        self.text_editor = Texte(self.frame)
        self.titles = ["Untitled"+str(self.acc)]
        self.notebook.add(self.frame, text=self.titles[0])

        self.notebook.pack(fill=tk.BOTH, expand=1)


def main(root):
    #text_editor = Texte(root)
    main_class(root)
    #text_editor.pack(expand=True, fill='both')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")
    root.iconphoto(False, tk.PhotoImage(file='img/ramen.png'))
    root.geometry("640x480")

    main(root)

    root.mainloop()
