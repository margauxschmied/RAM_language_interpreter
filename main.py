import tkinter.font as tkf
import src.preprocessing as pp
from tkinter import messagebox
from tkinter import filedialog, ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk


from antlr4 import InputStream, CommonTokenStream
from src.Antlr4.dist.MyGrammarLexer import MyGrammarLexer
from src.Antlr4.dist.MyGrammarParser import MyGrammarParser
from src.cantor_int import Int
from src.instruction.instruction import Instruction, RAM, RawInstruction
from src.decode_int import decode_int_instr, decode_int_program
from src.instruction.macro import Macro
from src.interpreter import Interpreter


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


class Frame:
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
        self.interpreters = []
        self.table_windows = []
        self.tables = []

        self.end_line = None
        self.choice_show_line_numbers = tk.IntVar(value=1)
        self.choice_automaticaly_go_to_next_line = tk.IntVar(value=1)

        self.create_menu(self.root)
        self.create_panel(self.root)
        self.create_notebook(self.root)
        self.create_output_terminal(self.root)
        self.create_popup(self.root)
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
            label="Exit", command=lambda: self.root.destroy())
        self.menu_bar.add_cascade(label="File", menu=self.menu_file)

        # The 'Run' contextual menu
        self.menu_run = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_run.add_command(
            label="Start/Run Next Instruction", command=self.execute_line)
        self.menu_run.add_command(
            label="Run File", command=self.execute_file)
        self.menu_bar.add_cascade(label="Run", menu=self.menu_run)

        # The 'Stop' button
        self.menu_bar.add_command(
            label="Stop", command=lambda: self.stop())

        # The 'Option' button
        self.menu_bar.add_command(
            label="Options", command=self.open_option)

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(
            label="Get Started", command=lambda: self.output.pretty_print("TODO: User Manual\n", 'blue'))
        self.menu_help.add_command(
            label="RAM Instructions", command=lambda: self.output.pretty_print("TODO: RAM\n", 'blue'))
        self.menu_help.add_command(
            label="About", command=lambda: self.output.pretty_print("TODO: About\n", 'blue'))

        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        parent.config(menu=self.menu_bar)

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
        text_editor.bind('<Button-3>', lambda e: self.popup(e))

        text_editor.tag_config(
            'default', foreground="black", background="lightgray")
        text_editor.tag_config('mark', foreground="white", background="blue")

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

        self.interpreters.append(None)

        table_window = tk.Toplevel(self.root)
        table_window.geometry('250x250')
        table_window.resizable(False, False)
        table_window.title("Memory")
        tree_scroll = tk.Scrollbar(table_window)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        table = ttk.Treeview(table_window, yscrollcommand=tree_scroll)
        tree_scroll.config(command=table.yview)
        table['columns'] = ('register', 'value')
        table.column("#0", width=0,  stretch=tk.NO)
        table.column("register", anchor=tk.CENTER, width=80)
        table.column("value", anchor=tk.CENTER, width=80)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("register", text="Register", anchor=tk.CENTER)
        table.heading("value", text="Value", anchor=tk.CENTER)

        table.pack(fill=tk.BOTH, expand=1)

        table_window.withdraw()
        table_window.protocol("WM_DELETE_WINDOW",
                              lambda: self.on_closing(table_window))
        self.table_windows.append(table_window)
        self.tables.append(table)

    def on_closing(self, table_window):
        table_window.withdraw()
        return 'break'

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

    def get_current_interpreter(self):
        return self.interpreters[int(self.get_current_tab())]

    def set_current_interpreter(self, interpreter):
        self.interpreters[int(self.get_current_tab())] = interpreter

    def get_current_table(self):
        return self.tables[int(self.get_current_tab())]

    def get_current_table_window(self):
        return self.table_windows[int(self.get_current_tab())]

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
            self.create_tab(Frame.path_to_filename(filenam))
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

        program_text = self.text_editors[tab_num].get('1.0', 'end-1c')
        f = open(self.filenames[tab_num][0], "w")
        f.write(program_text)
        f.close
        self.notebook.tab(
            tab_num, text=Frame.path_to_filename(self.filenames[tab_num][0]))

    def create_notebook(self, parent):
        """ Creation of tab's container. """

        self.notebook = ttk.Notebook(parent)
        self.create_tab("Untitled"+str(self.acc))
        self.filenames.append((self.titles[-1], True))

        self.create_intern_shortcut(self.text_editors[0])

        self.panel.add(self.notebook)

        self.notebook.bind("<<NotebookTabChanged>>",
                           lambda e: self.update_line(e, False))

    """
        Difference between extern and intern shorcut : first one is binding on the window whereas the intern
        is inside the text_editor.
    """

    def create_extern_shortcut(self, element):
        element.bind('<Control-s>', lambda e: self.save_file())
        element.bind('<Escape>', lambda e: self.show_message(
            "Do you want to quit?"))
        element.bind('<Control-x>', lambda e: self.execute_file())

    def create_intern_shortcut(self, element):
        element.bind('<Control-Return>', lambda e: self.execute_line())

    def create_output_terminal(self, parent):
        """ The result or error message will appear here. """
        self.frame = tk.Frame(parent)

        self.output = output_terminal(self.frame)

        # Choice between if we execute a RAM Program or Int Code
        vals = [0, 1]
        etiqs = ['RAM Program', 'Int Code']
        self.s_var = tk.StringVar()
        self.s_var.set(vals[0])

        self.radio_frame = tk.Frame(self.frame)
        self.radio_frame.pack()
        for i in range(2):
            radio = tk.Radiobutton(self.radio_frame, variable=self.s_var,
                                   text=etiqs[i], value=vals[i])
            radio.grid(row=0, column=i+3)

        self.output_label = tk.Label(self.frame, text="OUTPUT", bg='darkgray')
        self.default_font = tk.font.nametofont("TkDefaultFont")

        # The entry of the program (R0)
        self.entry = tk.Entry(self.radio_frame)
        self.entry.bind("<FocusIn>", lambda e: self.set_default(False))
        self.entry.bind("<FocusOut>", lambda e: self.set_default(True))
        self.entry.insert(0, "Enter the R0 value")
        self.entry.configure(font=(self.default_font.cget('family'),
                                   self.default_font.cget('size'), 'italic'))
        self.entry.config({"foreground": "Gray25"})

        self.entry.grid(row=0, column=2)

        self.output_label.pack(fill=tk.X)
        self.output.pack(fill=tk.BOTH, expand=True)

        self.panel.add(self.frame)
        self.input_label = tk.Label(self.radio_frame, text="R0 = ")
        self.input_label.grid(row=0, column=1)
        self.display_registers = tk.Button(
            self.radio_frame, text="Display Memory", command=lambda: self.open_registers())
        self.display_registers.grid(row=0, column=0)

    def open_registers(self):
        self.get_current_table_window().deiconify()

    def set_default(self, b):
        """ Display italic hint text 'Enter the R0' if entry field is empty and not selected """
        if b:
            if self.entry.get() == '':
                self.entry.delete(0, "end")
                self.entry.insert(0, "Enter the R0 value")
                self.entry.configure(font=(self.default_font.cget('family'),
                                           self.default_font.cget('size'), 'italic'))
                self.entry.config({"foreground": "Gray25"})
        else:
            if self.entry.get() == "Enter the R0 value" and self.get_current_font().cget('slant') == 'italic':
                self.entry.delete(0, "end")
                self.entry.insert(0, "")

            self.entry.configure(font=self.default_font)
            self.entry.config({"foreground": "Black"})

    def get_current_font(self):
        return tkf.Font(font=self.entry['font'])

    def create_panel(self, parent):
        """ Panel wich contain the text_editor of the current tab and the output_terminal (with the entry) which allows us
        to resize it. """
        self.panel = tk.PanedWindow(parent, orient=tk.VERTICAL)
        self.panel.pack(fill=tk.BOTH, expand=True)

    def show_message(self, s):
        res = messagebox.askokcancel("Quit", s)
        if res:
            self.root.destroy()

    def create_popup(self, parent):
        """ At the right-click on a line, this popup opens. """
        self.m = tk.Menu(parent, tearoff=0)
        # self.m.add_command(
        #     label="Run This Line", command=lambda: self.execute_mouse_line())
        self.m.add_command(
            label="Mark This Line as End", command=lambda: self.mark_line())
        self.m.add_command(
            label="Remove Line Mark", command=lambda: self.remove_mark())
        self.m.add_separator()
        self.m.add_command(
            label="Execute File", command=lambda: self.execute_file())

        self.m2 = tk.Menu(parent, tearoff=0)
        self.m2.add_command(
            label="Execute Int", command=lambda: self.execute_file())
        self.m2.add_separator()
        self.m2.add_command(
            label="Convert Into RAM in New File", command=lambda: self.convert_int_new_file())

    def convert_int_new_file(self):
        try:
            code_int = int(self.get_program())
            program = decode_int_program(code_int)
            self.new_file()
            self.text_editors[-1].insert('1.0', program)
        except ValueError:
            self.output.pretty_print(
                "Warning: Program is not an int\n", 'orange')
            pass

    def popup(self, event):
        try:
            if self.s_var.get() == '0':
                self.m.tk_popup(event.x_root, event.y_root)
            else:
                self.m2.tk_popup(event.x_root, event.y_root)
        finally:
            if self.s_var.get() == '0':
                self.m.grab_release()
            else:
                self.m2.grab_release()

    def open_option(self):
        """ New window for options is created and has the focus. """
        new_window = tk.Toplevel(self.panel)

        new_window.title("Options")
        new_window.grab_set()
        new_window.focus()
        new_window.geometry("300x80")
        new_window.resizable(False, False)
        check1 = tk.Checkbutton(new_window, text='Show Line Numbers',
                                variable=self.choice_show_line_numbers, onvalue=1, offvalue=0, command=lambda: self.manage_line_numbers(self.choice_show_line_numbers.get()))
        check1.grid(column=0, row=0, sticky='W')
        check2 = tk.Checkbutton(
            new_window, text='Automaticaly Go to Next Line', variable=self.choice_automaticaly_go_to_next_line, onvalue=1, offvalue=0)
        check2.grid(column=0, row=1, sticky='W')

        valid = tk.Button(new_window, text="OK",
                          command=lambda: new_window.destroy())
        valid.grid(column=0, row=2, sticky='E')

    def manage_line_numbers(self, b):
        """ Useful if we want to hide/show line numbers. """
        for l, t in zip(self.line_numbers, self.text_editors):
            if b == 1:
                t.pack_forget()
                l.pack(side=tk.LEFT, fill=tk.BOTH)
                t.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            else:
                l.pack_forget()

    def mark_line(self):
        """ At the rigth-click, we can mark a line. The line will be highlighting with blue background. """
        index = self.get_current_text_editor().index('insert')
        current_text_editor = self.get_current_text_editor()
        self.end_line = Frame.idx_to_nb(index)
        first = ('1.0', str(max(int(Frame.idx_to_nb(index)) - 1, 1)) + '.end')
        second = (Frame.idx_to_nb(index) + '.0',
                  Frame.idx_to_nb(index) + '.end')
        third = (second[1], 'end-1c')

        copy = pp.copy_text(current_text_editor, None)
        current_text_editor.clean()
        if Frame.idx_to_nb(index) != '1':
            current_text_editor.insert(
                tk.END, copy.get(first[0], first[1]) + '\n')
        current_text_editor.insert(
            tk.END, copy.get(second[0], second[1]), 'mark')
        current_text_editor.insert(tk.END, copy.get(third[0], third[1]))
        current_text_editor.mark_set("insert", index)

    def remove_mark(self):
        """ At the rigth-click, we can remove the mark if it exists. """
        index = self.get_current_text_editor().index('insert')
        current_text_editor = self.get_current_text_editor()
        copy = pp.copy_text(current_text_editor, None)
        current_text_editor.clean()
        current_text_editor.insert(tk.END, copy.get('1.0', 'end-1c'))
        current_text_editor.mark_set("insert", index)
        self.end_line = None

    def execute_line(self, line_index=None):
        """ Strat the sequencial execution or execute the next instruction if started. """

        if self.s_var.get() == '1':
            self.output.pretty_print(
                "Warning: Convert this Int program into RAM program to allow sequential execution.\n(Right-click -> Convert Into RAM in New File)\n", 'orange')
            return 'break'
        program = self.get_program(False)
        entry = self.get_entry()
        if entry == None:
            return 'break'

        if self.get_current_interpreter() == None:
            inter = self.parse_ram_program(program, entry)
            if inter == None:
                return 'break'
            self.set_current_interpreter(inter)
            self.output.pretty_print(
                "Sequential execution started ("+self.get_current_tabname()+").\n", 'blue')

        try:
            current_inst = self.get_current_interpreter().instr_list[self.get_current_interpreter(
            ).current_instr - 1]
            self.output.pretty_print(
                "Execution of: " + current_inst.__str__() + ' (' + str(self.get_current_interpreter().current_instr) + ')\n', 'blue')
            self.get_current_interpreter().treat_one_instr()
            self.clear_and_put(self.get_current_interpreter().memory)
        except IndexError:
            self.get_current_interpreter().treat_one_instr()

        if self.get_current_interpreter().end:
            self.output.pretty_print(
                "Sequential execution finished ("+self.get_current_tabname()+").\n", 'blue')
            self.output.pretty_print(
                "Result: " + str(self.get_current_interpreter().get_otput()) + '\n', 'blue')
            self.set_current_interpreter(None)

        return 'break'

    def clear(self):
        table = self.get_current_table()
        table.delete(*table.get_children())

    def clear_and_put(self, dict):
        table = self.get_current_table()
        self.clear()
        acc = 0
        for r, v in dict.items():
            table.insert(parent='', index='end',
                         iid=acc, text='', values=('R'+str(r), v))
            acc += 1

    def stop(self):
        if self.get_current_interpreter() != None:
            self.get_current_interpreter().treat_all_instr()
            self.output.pretty_print(
                "Sequential execution stopped ("+self.get_current_tabname()+").\nResult: " + str(self.get_current_interpreter().get_otput()) + '\n', 'blue')
            self.clear_and_put(self.get_current_interpreter().memory)
            self.set_current_interpreter(None)

    def execute_file(self):
        """ Execution of the whole file, we get the program, its type (RAM or Int) and its entry. """
        self.output.pretty_print(
            'Execution (' + self.get_current_tabname() + ')\n', 'blue')

        program = self.get_program()
        entry = self.get_entry()
        if entry == None:
            return

        # RAM = 0, Int = 1
        if self.s_var.get() == '0':
            self.output.pretty_print("RAM Programm\n", 'blue')

        else:
            self.output.pretty_print("Int Code\n", 'blue')
            try:
                code_int = int(program)
                program = decode_int_program(code_int)
            except ValueError:
                self.output.pretty_print(
                    "Warning: Program is not an int\n", 'orange')
                pass
        interp = self.parse_ram_program(program, entry)
        if interp != None:
            interp.treat_all_instr()
            output = interp.get_otput()
            self.output.pretty_print("Result: " + str(output) + '\n', 'blue')
            self.clear_and_put(interp.memory)

    def parse_ram_program(self, ram_program, entry):
        # data = InputStream(ram_program)
        # # lexer
        # lexer = MyGrammarLexer(data)
        # stream = CommonTokenStream(lexer)
        # # parser
        # parser = MyGrammarParser(stream)
        # tree = parser.program()
        # # evaluator
        # visitor = MyVisitor()
        # visitor.visit(tree)
        #
        # l_inst = listInstruction(tree)
        # try:
        #     interpr = Interpreter(l_inst, memory=RAM(entry))
        #     return interpr
        # except AttributeError:
        #     self.output.pretty_print(
        #         "Error: Program is wrong\n", 'red')
        #     return None
        return None

    def get_program(self, apply_preprocessing=True):
        """ Return the program in which we have do the preprocessing instructions (#define, #include). """
        if apply_preprocessing:
            program_includes = pp.file_includes(
                self.get_current_text_editor(), self.end_line, self.output)
            program_includes_defines = pp.user_defines(
                program_includes, self.output)
            program = program_includes_defines.get('1.0', 'end-1c')
        else:
            program = pp.delete_preprocessing(
                self.get_current_text_editor()).get('1.0', 'end-1c')
        return program

    def get_entry(self):
        """ Return the entry of the program. """
        if self.get_current_font().cget('slant') == 'italic':
            self.output.pretty_print("Error: Enter R0 value\n", 'red')
            return None
        else:
            entry = self.entry.get()
            try:
                entry = int(entry)
                return entry
            except ValueError:
                self.output.pretty_print("Error: Entry is not an int\n", 'red')
                return None

    @staticmethod
    def path_to_filename(path):
        return path.split('/')[-1]

    @staticmethod
    def idx_to_nb(index):
        return index.split('.')[0]


class output_terminal(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, bg="white", wrap='word')

        self.configure(state='disabled')
        self.tag_config('blue', foreground="blue")
        self.tag_config('red', foreground="red")
        self.tag_config('orange', foreground="orange")
        self.tag_config('gray', foreground="gray30")
        self.tag_config('black', foreground="black")

    def pretty_print(self, s, fg='black'):
        self.configure(state='normal')
        self.insert('end', s, fg)
        self.yview_moveto(1)
        self.configure(state='disabled')


def main(root):
    Frame(root)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")
    root.iconphoto(False, tk.PhotoImage(file='./ressources/img/ramen.png'))
    root.geometry("640x480")

    main(root)

    root.mainloop()

    MACROS = {
        'add':  Macro('add', ['kappa'], [
            RawInstruction(1, 'kappa')
        ])
    }

    N = 100
    i = Interpreter(
        [RawInstruction('add', [5], is_macro=True)], MACROS, RAM(N))

    print(f"\n  Starting instructions \n{i}")

    program_int = i.encode_list_instr()

    print(f"\n  Program int \n{program_int}")

#    program_decoded = decode_int_program(str(i))

    # print(f"\n  Instruction in RAM \n{program_decoded}")

    data = InputStream("""R0 = R0 + 1
R0 = R0 - 1
R0 = R0 + 1
R0 = R0 - 1
R1000 = R1000 + 1
IF R0 != 0 then gotob 2
R1000 = R1000 - 1
R0 = R0 + 1
R100 = R100 + 1
IF R1000 != 0 then gotob 3
R0 = R0 - 1
R100 = R100 - 1
R100 = R100 + 1
R1 = R1 + 1
R100 = R100 - 1
IF R100 != 0 then gotob 2
R1 = R1 - 1
IF R0 != 0 then gotob 16   
""")

    # # lexer
    # lexer = MyGrammarLexer(data)
    # stream = CommonTokenStream(lexer)
    #
    # # parser
    # parser = MyGrammarParser(stream)
    # tree = parser.program()
    #
    # # evaluator
    # visitor = MyVisitor()
    # output = visitor.visit(tree)
    #
    # l_inst = listInstruction(tree)
    #
    # print(f"\n  List instr after parsing \n{l_inst}")
    #
    # print(f"\n  Program to int instr \n{decode_int_program(l_inst)}")
    #
    # # interpreter
    # interp = Interpreter(l_inst, memory=RAM(N))
    # interp.treat_all_instr()
    # print("\n  Program output =", interp.get_otput())
