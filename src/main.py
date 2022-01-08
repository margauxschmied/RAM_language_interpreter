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

    def createTab(self, tab_name):
        self.titles.append(tab_name)
        self.tabs.append(tk.Frame())
        self.frames.append(tk.Frame(self.notebook))
        self.text_editors.append(Texte(self.frames[-1]))

        self.notebook.add(self.frames[-1], text=self.titles[-1])
        self.text_editors[-1].pack(expand=True, fill='both')
        self.text_editors[-1].clean()

    def new_file(self):
        self.acc += 1
        title = 'Untitled'+str(self.acc)
        self.createTab(title)
        self.filenames.append((title, True))

    def open_file(self):
        filenam = filedialog.askopenfilename(
            title="Select File",
            filetypes=(("Text files",
                        "*.txt*"),
                       ("All files",
                        "*.*")))
        if filenam != '':
            self.createTab(self.path_to_filename(filenam))
            self.read_file(filenam, len(self.text_editors) - 1)
            self.filenames.append((filenam, False))

    def read_file(self, path, tab_num):
        f = open(path, "r")
        self.text_editors[tab_num].add_clean(f.read())
        f.close()

    def save_file(self):
        tab_num = self.notebook.index(self.notebook.select())
        if self.filenames[tab_num][1]:
            file = filedialog.asksaveasfile(
                defaultextension='.txt', filetypes=(("Text files",
                                                    "*.txt*"),
                                                    ("All files",
                                                    "*.*")),
                initialfile='RAM'+str(self.acc)+'.txt')
            if file != None:
                self.filenames[tab_num] = (file.name, False)
            else:
                return

        program_text = self.text_editors[tab_num].get('1.0', tk.END)
        f = open(self.filenames[tab_num][0], "w")
        f.write(program_text)
        f.close
        self.notebook.tab(
            tab_num, text=self.path_to_filename(self.filenames[tab_num][0]))

    def path_to_filename(self, path):
        return path.split('/')[-1]

    def createNotebook(self, parent):
        self.acc = 1
        self.filenames = []
        self.notebook = ttk.Notebook(parent)
        self.tabs = [tk.Frame()]
        self.frames = [tk.Frame(self.notebook)]
        self.text_editors = [Texte(self.frames[0])]
        self.titles = ["Untitled"+str(self.acc)]
        self.filenames.append((self.titles[0], True))
        self.notebook.add(self.frames[0], text=self.titles[0])

        self.notebook.pack(fill=tk.BOTH, expand=1)
        self.text_editors[0].pack(expand=True, fill='both')


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
