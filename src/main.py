from tkinter import messagebox
from tkinter import filedialog, ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import sys as sys


class Texte(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, width=20, height=10,
                         bg="lightgrey", wrap='word')

    def add_text(self, txt: str):
        self.insert(tk.END, txt)

    def clean(self):
        self.delete('1.0', tk.END)

    def add_clean(self, txt: str):
        self.clean()
        self.add_text(txt)


class main_class:
    """ This class aims to manage all frames. Here we create the menu bar, the file tabs or the shortcuts. """

    def __init__(self, root) -> None:
        self.root = root
        self.initiate()

    def initiate(self):
        """ We create useful variables :
                acc : newly-created files' counter
                filenames : couple's list of this kind (filenames, Boolean) which
                            filenames is the path and Boolean represent if the file correspoding has already been saved
                frames : list which contain text_editor
                text_editors : text_editor's list in which we write our code/program
                line_numbers : displayer's list of line number by according  the respecting text_editor
                titles : tabname's list
        """

        self.acc = 1
        self.filenames = []
        self.frames = []
        self.scrollbars = []
        self.text_editors = []
        self.line_numbers = []
        self.titles = []

        self.choice1 = tk.IntVar(value=1)
        self.choice2 = tk.IntVar(value=1)

        self.create_menu(self.root)
        self.create_panel(self.root)
        self.create_notebook(self.root)
        self.create_output_terminal(self.root)
        self.create_extern_shortcut(self.root)

    def create_menu(self, parent):
        """ Function wich creates the bar menu. """

        self.menu_bar = tk.Menu(parent)

        # The 'File' contextual menu
        self.menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(
            label="New File", command=lambda: self.new_file())
        self.menu_file.add_command(
            label="Open File", command=lambda: self.open_file())
        self.menu_file.add_command(
            label="Save", command=lambda: self.save_file())

        self.menu_file.add_separator()
        self.menu_file.add_command(
            label="Exit", command=lambda: root.destroy())
        self.menu_bar.add_cascade(label="File", menu=self.menu_file)

        # The 'Run' contextual menu
        self.menu_run = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_run.add_command(
            label="Run Selected Line", command=self.execute_line)
        self.menu_run.add_command(
            label="Run File", command=self.execute_file)
        self.menu_bar.add_cascade(label="Run", menu=self.menu_run)

        # The 'Stop' button
        """self.menu_stop = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_stop.add_command(
            label="Stop execution", command=lambda: print("Stopped"))
        self.menu_bar.add_cascade(label="Stop", menu=self.menu_stop)"""
        self.menu_bar.add_command(
            label="Stop", command=lambda: self.pretty_print("TODO: Stop\n", 'blue'))

        # The 'Option' button
        self.menu_bar.add_command(
            label="Options", command=self.open_option)

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(
            label="User manual", command=lambda: self.pretty_print("TODO: User Manual\n", 'blue'))
        self.menu_help.add_command(
            label="RAM instructions", command=lambda: self.pretty_print("TODO: RAM\n", 'blue'))
        self.menu_help.add_command(
            label="About", command=lambda: self.pretty_print("TODO: About\n", 'blue'))

        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        parent.config(menu=self.menu_bar)

    def manage_line_numbers(self, b):
        for l, t in zip(self.line_numbers, self.text_editors):
            if b == 1:
                t.pack_forget()
                l.pack(side=tk.LEFT, fill=tk.BOTH)
                t.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            else:
                l.pack_forget()

    def open_option(self):
        new_window = tk.Toplevel(self.panel)

        new_window.title("Options")
        new_window.grab_set()
        new_window.focus()
        new_window.geometry("300x80")
        new_window.resizable(False, False)
        check1 = tk.Checkbutton(new_window, text='Show Line Numbers',
                                variable=self.choice1, onvalue=1, offvalue=0, command=lambda: self.manage_line_numbers(self.choice1.get()))
        check1.grid(column=0, row=0, sticky='W')
        check2 = tk.Checkbutton(
            new_window, text='Automaticaly Go to Next Line', variable=self.choice2, onvalue=1, offvalue=0)
        check2.grid(column=0, row=1, sticky='W')

        valid = tk.Button(new_window, text="OK",
                          command=lambda: new_window.destroy())
        valid.grid(column=0, row=2, sticky='E')

    def create_tab(self, tab_name):
        """ We create a new tab when : we open a file, we create new file. """

        self.titles.append(tab_name)
        self.frames.append(tk.Frame(self.notebook))
        text_editor = Texte(self.frames[-1])
        line_number = Texte(self.frames[-1])
        line_number.config(bg='white')
        self.line_numbers.append(line_number)
        self.create_intern_shortcut(text_editor)
        self.text_editors.append(text_editor)

        line_number.pack(side=tk.LEFT, fill=tk.BOTH)
        text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_editor.bind('<Return>', lambda e: self.update_line(e))
        text_editor.bind('<BackSpace>', lambda e: self.update_line(e))

        line_number.insert(1.0, '1')
        line_number.configure(width=1)
        line_number.configure(state='disabled')
        text_editor.clean()

        self.notebook.add(self.frames[-1], text=self.titles[-1])

        scrollbar = tk.Scrollbar(self.frames[-1])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbars.append(scrollbar)

        scrollbar['command'] = self.on_scrollbar
        text_editor['yscrollcommand'] = self.on_textscroll

    def update_line(self, event=None, correct_line_count=True):
        """ Update line number function's according to the current tab (selected one). """

        number_lines = str(
            self.get_current_text_editor().index(tk.END)).split('.')[0]
        if not correct_line_count:
            number_lines = str(int(number_lines) - 1)

        line_numbers_string = "\n".join(str(i+1).rjust(len(number_lines))
                                        for i in range(int(number_lines)))
        width = len(str(number_lines))

        self.get_current_line_number().configure(state='normal', width=width)
        self.get_current_line_number().delete(1.0, tk.END)
        self.get_current_line_number().insert(1.0, line_numbers_string)
        self.get_current_line_number().configure(state='disabled')

    def on_scrollbar(self, *args):
        """ The scrollbar affect both the text_editor AND the line number widgets. """

        self.get_current_text_editor().yview(*args)
        self.get_current_line_number().yview(*args)

    def on_textscroll(self, *args):
        """ Simultaneous scrolling of line number line when we scroll on the text_editor with mousewheel. """

        self.get_current_scrollbar().set(*args)
        self.on_scrollbar('moveto', args[0])

    def get_current_tab(self):
        return self.notebook.index(self.notebook.select())

    def get_current_tabname(self):
        return self.notebook.tab(self.notebook.select(), 'text')

    def get_current_text_editor(self):
        return self.text_editors[int(self.get_current_tab())]

    def get_current_line_number(self):
        return self.line_numbers[int(self.get_current_tab())]

    def get_current_scrollbar(self):
        return self.scrollbars[int(self.get_current_tab())]

    def new_file(self):
        """ Default name of newly-created file is Untitled+[acc] """

        self.acc += 1
        title = 'Untitled'+str(self.acc)
        self.create_tab(title)
        self.filenames.append((title, True))
        self.notebook.select(self.notebook.index('end')-1)

    def open_file(self):
        """ We ask user to choose file by file browser, then we read it and create corresponding tab. """

        filenam = filedialog.askopenfilename(
            title="Select File",
            filetypes=(("Text files",
                        "*.txt*"),
                       ("All files",
                        "*.*")))
        if filenam != '':
            self.create_tab(self.path_to_filename(filenam))
            self.read_file(filenam, len(self.text_editors) - 1)
            self.filenames.append((filenam, False))
            self.notebook.select(self.notebook.index('end')-1)

    def read_file(self, path, tab_num):
        """ Writing of file's content into text_editor. """

        f = open(path, "r")
        self.text_editors[tab_num].add_clean(f.read())
        f.close()

    def save_file(self):
        """ We ask user to choose a filename if he saves the file for the first time. """

        tab_num = self.notebook.index(self.notebook.select())
        if self.filenames[tab_num][1]:
            file = filedialog.asksaveasfile(
                defaultextension='.txt', filetypes=(("Text files",
                                                    "*.txt*"),
                                                    ("All files",
                                                    "*.*")),
                initialfile=self.notebook.tab(self.notebook.select(), "text") + '.txt')
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

    def create_notebook(self, parent):
        """ Creation of tab's container. """

        self.notebook = ttk.Notebook(parent)
        self.create_tab("Untitled"+str(self.acc))
        self.filenames.append((self.titles[-1], True))

        self.create_intern_shortcut(self.text_editors[0])

        self.notebook.pack(fill=tk.BOTH, expand=1)
        self.panel.add(self.notebook)

        self.notebook.bind("<<NotebookTabChanged>>",
                           lambda e: self.update_line(e, False))

    """
        Difference between extern and intern shorcut : first one is binding on the window whereas the intern
        is inside the text_editor
    """

    def create_extern_shortcut(self, element):
        element.bind('<Control-s>', lambda e: self.save_file())
        element.bind('<Escape>', lambda e: self.show_message(
            "Do you want to quit?"))

    def create_intern_shortcut(self, element):
        element.bind('<Control-Return>', lambda e: self.execute_line())

    def execute_line(self):
        """ The selected line is where the insertion cursor is. """

        line_index = self.get_current_text_editor().index('insert')
        line_number = line_index.split('.')[0]
        res = 'Execution (line ' + line_index.split('.')[0] + ', file ' + self.get_current_tabname(
        ) + '): '
        self.pretty_print("TODO: Run line\n", 'blue')
        self.pretty_print(res)
        self.pretty_print(self.text_editors[self.get_current_tab()].get(
            line_number + '.0', line_number + '.end') + '\n', 'gray')

        if self.choice2.get() == 1:
            self.get_current_text_editor().mark_set(
                "insert", str(int(line_number) + 1) + '.end')

        return 'break'

    def execute_file(self):
        program = self.get_current_text_editor().get('1.0', 'end')
        res = 'Execution (' + self.get_current_tabname() + ')\n'
        self.pretty_print("TODO: Run file\n", 'blue')
        self.pretty_print(res)

    def create_output_terminal(self, parent):
        self.output = ScrolledText(
            parent, bg="white", wrap='word')
        self.output.pack(fill=tk.X, expand=1)
        self.output.configure(state='disabled')
        self.output.tag_config('blue', foreground="blue")
        self.output.tag_config('gray', foreground="gray30")
        self.output.tag_config('black', foreground="black")

        self.panel.add(self.output)

    def create_panel(self, parent):
        self.panel = tk.PanedWindow(parent, orient=tk.VERTICAL)
        self.panel.pack(fill=tk.BOTH, expand=True)

    def show_message(self, s):
        res = messagebox.askokcancel("Quit", s)
        if res:
            self.root.destroy()

    def pretty_print(self, s, fg='black'):
        self.output.configure(state='normal')
        self.output.insert('end', s, fg)
        self.output.yview_moveto(1)
        self.output.configure(state='disabled')


def main(root):
    main_class(root)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")
    root.iconphoto(False, tk.PhotoImage(file='img/ramen.png'))
    root.geometry("640x480")

    main(root)

    root.mainloop()
