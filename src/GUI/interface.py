import tkinter.font as tkf
import src.GUI.preprocessing as pp
import src.GUI.widgets.options as so
import src.GUI.widgets.output_terminal as ot
import src.GUI.widgets.texte as tx
import src.GUI.widgets.menu as menu
import src.GUI.widgets.popup as pop
import src.GUI.widgets.toolbar as tb
import src.GUI.widgets.windows as wi

from tkinter import messagebox
from tkinter import filedialog, ttk
import tkinter as tk

from src.interpreter.cantor_int import *
from src.interpreter.instruction import *
from src.interpreter.decode_int import *
from src.interpreter.interpreter import *
from src.parser.parser import myLex, myYacc, macros
from src.pars_to_interp import *


class MyGUI:
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
        self.code_windows = []
        self.codes = []

        self.end_line = None
        self.set_choices()

        self.create_menu(self.root)
        self.create_toolbar(self.root)
        self.create_panel(self.root)
        self.create_notebook(self.root)
        self.create_output_terminal(self.root)
        self.create_popup(self.root)
        self.create_extern_shortcut(self.root)

    def set_choices(self):
        user_options = so.read()
        self.choice_show_line_numbers = tk.IntVar(
            value=int(user_options['show_line']))
        self.choice_automaticaly_code = tk.IntVar(
            value=int(user_options['open_code']))
        self.choice_automaticaly_memory = tk.IntVar(
            value=int(user_options['open_memory']))

    def create_menu(self, parent):
        """ Function wich creates the bar menu. """
        self.menu_bar = menu.menu_bar(parent, self)
        parent.config(menu=self.menu_bar)

    def create_toolbar(self, parent):
        self.toolbar = tb.toolbar(parent, self)

    def create_tab(self, tab_name):
        """ We create a new tab when : we open a file, we create new file. """

        self.titles.append(tab_name)
        self.frames.append(ttk.Frame(self.notebook))

        # text editor when we create or open file
        text_editor = tx.texte(self.frames[-1])

        # line number of the text editor
        line_number = tx.texte(self.frames[-1])
        line_number.config(bg='white')
        self.line_numbers.append(line_number)
        self.create_intern_shortcut(text_editor)
        self.text_editors.append(text_editor)

        # show line number only if the settings allow it
        if so.read()['show_line'] == '1':
            line_number.pack(side=tk.LEFT, fill=tk.BOTH)
        text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # listener over text editor
        text_editor.bind('<Button-3>', lambda e: self.popup(e))

        text_editor.bind('<KeyRelease>', lambda e: self.update_line())

        text_editor.tag_config(
            'default', foreground="black", background="lightgray")
        text_editor.tag_config('mark', foreground="white", background="blue")

        line_number.insert(1.0, '1')
        line_number.configure(width=1)
        line_number.configure(state='disabled')
        text_editor.clean()

        self.notebook.add(self.frames[-1], text=self.titles[-1])

        scrollbar = ttk.Scrollbar(self.frames[-1])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbars.append(scrollbar)

        # for simultaneous scroll between line_number and text_editor
        scrollbar['command'] = self.on_scrollbar
        text_editor['yscrollcommand'] = self.on_textscroll
        line_number['yscrollcommand'] = self.on_textscroll

        self.interpreters.append(None)

        # creation of the two window (final code and registers)
        wi.create_code_window(self)
        wi.create_memory_window(self)

    def on_closing(self, table_window):
        table_window.withdraw()
        return 'break'

    def update_line(self):
        """ We update the nmber of line of the current text editor when the user type a key. """
        number_lines = int(self.get_current_text_editor().index(
            tk.END).split('.')[0]) - 1
        number_lines = str(number_lines)
        width = len(number_lines)
        line_numbers_string = "\n".join(str(i+1).rjust(width)
                                        for i in range(int(number_lines)))

        self.get_current_line_number().configure(state='normal', width=width)
        self.get_current_line_number().delete(1.0, tk.END)
        self.get_current_line_number().insert(1.0, line_numbers_string)
        self.get_current_line_number().yview(
            'moveto', str(self.get_current_text_editor().yview()[0]))
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

    def get_current_code(self):
        return self.codes[int(self.get_current_tab())]

    def get_current_code_window(self):
        return self.code_windows[int(self.get_current_tab())]

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
            self.create_tab(MyGUI.path_to_filename(filenam))
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
            tab_num, text=MyGUI.path_to_filename(self.filenames[tab_num][0]))

    def create_notebook(self, parent):
        """ Creation of tab's container. """

        self.notebook = ttk.Notebook(parent)
        self.create_tab("Untitled"+str(self.acc))
        self.filenames.append((self.titles[-1], True))

        self.create_intern_shortcut(self.text_editors[0])

        self.panel.add(self.notebook)

        self.notebook.bind("<<NotebookTabChanged>>",
                           lambda e: self.update_line_menu())

    """
        Difference between extern and intern shorcut : first one is binding on the window whereas the intern
        is inside the text_editor.
    """

    def update_line_menu(self):
        self.update_line()
        self.update_menu()

    def update_menu(self):
        sta1 = 'normal'
        sta2 = 'disabled'
        inter = self.get_current_interpreter() == None

        self.menu_bar.menu_run.entryconfig(0, state=(sta1 if inter else sta2))
        self.menu_bar.menu_run.entryconfig(1, state=(sta2 if inter else sta1))
        self.menu_bar.entryconfig(3, state=(sta2 if inter else sta1))

    def create_extern_shortcut(self, element):
        element.bind('<Control-s>', lambda e: self.save_file())
        element.bind('<Escape>', lambda e: self.show_message(
            "Do you want to quit?"))

    def create_intern_shortcut(self, element):
        element.bind('<Control-Return>', lambda e: self.execute_line())
        element.bind('<Control-Shift-Return>',
                     lambda e: self.execute_file())

    def create_output_terminal(self, parent):
        """ The result or error message will appear here. """
        self.frame = ttk.Frame(parent)

        self.output = ot.output_terminal(self.frame)

        # Choice between if we execute a RAM Program or Int Code
        vals = [0, 1]
        etiqs = ['RAM Program', 'Int Code']
        self.s_var = tk.StringVar()
        self.s_var.set(vals[0])

        self.radio_frame = ttk.Frame(self.frame)
        self.radio_frame.pack()
        for i in range(2):
            radio = ttk.Radiobutton(self.radio_frame, variable=self.s_var,
                                    text=etiqs[i], value=vals[i])
            radio.grid(row=0, column=i+4)

        self.output_label = ttk.Label(
            self.frame, text="OUTPUT", background='darkgray')
        self.default_font = tk.font.nametofont("TkDefaultFont")

        # The entry of the program (R0)
        self.entry = ttk.Entry(self.radio_frame)
        self.entry.bind("<FocusIn>", lambda e: self.set_default(False))
        self.entry.bind("<FocusOut>", lambda e: self.set_default(True))
        self.entry.insert(0, "Enter the R0 value")
        self.entry.configure(font=(self.default_font.cget('family'),
                                   self.default_font.cget('size'), 'italic'))
        self.entry.config({"foreground": "Gray25"})

        self.entry.grid(row=0, column=3)

        self.output_label.pack()
        self.output.pack(fill=tk.BOTH, expand=True)

        self.panel.add(self.frame)
        self.input_label = ttk.Label(self.radio_frame, text="R0 = ")
        self.input_label.grid(row=0, column=2)
        self.display_ram_code = ttk.Button(
            self.radio_frame, text="Display Executed Code", command=lambda: self.open_executed_code())
        self.display_ram_code.grid(row=0, column=0)
        self.display_registers = ttk.Button(
            self.radio_frame, text="Display Memory", command=lambda: self.open_registers())
        self.display_registers.grid(row=0, column=1)

    def open_executed_code(self):
        self.get_current_code_window().deiconify()

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
        self.panel = ttk.PanedWindow(parent, orient=tk.VERTICAL)
        self.panel.pack(fill=tk.BOTH, expand=True)

    def show_message(self, s):
        res = messagebox.askokcancel("Quit", s)
        if res:
            self.root.destroy()

    def create_popup(self, parent):
        """ At the right-click on a line, this popup opens. """
        self.m = pop.popup1(parent, self)
        self.m2 = pop.popup2(parent, self)

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
        so.option_window(self.panel, self)

    def save_destroy(self, window):
        so.save({'show_line': str(self.choice_show_line_numbers.get()), 'open_code': str(
            self.choice_automaticaly_code.get()), 'open_memory': str(self.choice_automaticaly_memory.get())})
        self.manage_line_numbers(self.choice_show_line_numbers.get())
        window.destroy()

    def reset_destroy(self, window):
        self.set_choices()
        window.destroy()

    def manage_line_numbers(self, b):
        """ Useful if we want to hide/show line numbers. """
        for l, t in zip(self.line_numbers, self.text_editors):
            if b == 1:
                t.pack_forget()
                l.pack(side=tk.LEFT, fill=tk.BOTH)
                t.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            else:
                l.pack_forget()

    def mark_line(self, current_text_editor, index, program=False):
        """ At the rigth-click, we can mark a line. The line will be highlighting with blue background. """

        if program:
            self.end_line = MyGUI.idx_to_nb(index)
        first = ('1.0', str(max(int(MyGUI.idx_to_nb(index)) - 1, 1)) + '.end')
        second = (MyGUI.idx_to_nb(index) + '.0',
                  MyGUI.idx_to_nb(index) + '.end')
        third = (second[1], 'end-1c')

        copy = pp.copy_text(current_text_editor, None)

        if not program:
            current_text_editor.configure(state='normal')

        current_text_editor.delete('1.0', tk.END)
        if MyGUI.idx_to_nb(index) != '1':
            current_text_editor.insert(
                tk.END, copy.get(first[0], first[1]) + '\n')
        current_text_editor.insert(
            tk.END, copy.get(second[0], second[1]), 'mark')
        current_text_editor.insert(tk.END, copy.get(third[0], third[1]))
        if program:
            current_text_editor.mark_set("insert", index)
        else:
            current_text_editor.configure(state='disabled')

    def remove_mark(self, current_text_editor, index=None, program=False):
        """ At the rigth-click, we can remove the mark if it exists. """

        copy = pp.copy_text(current_text_editor, None)
        if not program:
            current_text_editor.configure(state='normal')
        current_text_editor.delete('1.0', tk.END)
        current_text_editor.insert(tk.END, copy.get('1.0', 'end-1c'))
        if program:
            current_text_editor.mark_set("insert", index)
            self.end_line = None
        else:
            current_text_editor.configure(state='disabled')

    def execute_line(self):
        """ Start the sequencial execution or execute the next instruction if started. """

        if self.s_var.get() == '1':
            self.output.pretty_print(
                "Warning: Convert this Int program into RAM program to allow sequential execution.\n(Right-click -> Convert Into RAM in New File)\n", 'orange')
            return 'break'
        program = self.get_program()
        entry = self.get_entry()
        if entry == None:
            return 'break'

        if self.get_current_interpreter() == None:
            inter = self.parse_ram_program(program, entry)
            if inter == None:
                return 'break'
            self.set_current_interpreter(inter)
            self.get_current_code().configure(state='normal')
            self.get_current_code().delete('1.0', tk.END)
            self.get_current_code().insert(tk.END, str(inter))
            self.get_current_code().configure(state='disabled')
            self.update_menu()
            if self.choice_automaticaly_code.get() == 1:
                self.get_current_code_window().deiconify()
            if self.choice_automaticaly_memory.get() == 1:
                self.get_current_table_window().deiconify()
            self.output.pretty_print(
                "Sequential execution started ("+self.get_current_tabname()+").\n", 'green')

        try:
            current_inst = self.get_current_interpreter().instr_list[self.get_current_interpreter(
            ).current_instr - 1]
            self.output.pretty_print(
                "Execution of: " + current_inst.__str__() + ' (' + str(self.get_current_interpreter().current_instr) + ')\n', 'blue')

            self.highlight_line(self.get_current_code(),
                                self.get_current_interpreter().current_instr)
            self.get_current_interpreter().treat_one_instr()
            self.clear_and_put(self.get_current_interpreter().memory)
        except IndexError:
            self.get_current_interpreter().treat_one_instr()

        if self.get_current_interpreter().end:
            self.output.pretty_print(
                "Sequential execution finished ("+self.get_current_tabname()+").\n", 'green')
            self.output.pretty_print(
                "Result: " + str(self.get_current_interpreter().get_output()) + '\n', 'blue')
            self.set_current_interpreter(None)
            self.remove_mark(self.get_current_code())
            self.update_menu()

        return 'break'

    def highlight_line(self, current_code, line):
        self.mark_line(current_code, line)

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
                "Sequential execution stopped ("+self.get_current_tabname()+").", 'red')
            self.output.pretty_print(
                "\nResult: " + str(self.get_current_interpreter().get_output()) + '\n', 'blue')
            self.clear_and_put(self.get_current_interpreter().memory)
            self.remove_mark(self.get_current_code())
            self.set_current_interpreter(None)
            self.update_menu()

    def execute_file(self):
        """ Execution of the whole file, we get the program, its type (RAM or Int) and its entry. """
        self.output.pretty_print(
            'Execution (' + self.get_current_tabname() + ')\n', 'blue')

        program = self.get_program()
        entry = self.get_entry()
        if entry == None:
            return 'break'

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
            self.get_current_code().configure(state='normal')
            self.get_current_code().delete('1.0', tk.END)
            self.get_current_code().insert(tk.END, str(interp))
            self.get_current_code().configure(state='disabled')
            interp.treat_all_instr()
            output = interp.get_output()
            self.output.pretty_print("Result: " + str(output) + '\n', 'blue')
            self.clear_and_put(interp.memory)
        return 'break'

    def parse_ram_program(self, ram_program, entry):
        lexer = myLex()
        lexer.input(ram_program)
        parser = myYacc()
        result = parser.parse(ram_program)
        interp = make_interpreter(result)
        interp.reset(entry)
        return interp

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

    @ staticmethod
    def path_to_filename(path):
        return path.split('/')[-1]

    @ staticmethod
    def idx_to_nb(index):
        if type(index) == int:
            return str(index)
        return index.split('.')[0]


def run_GUI():
    root = tk.Tk()
    root.title("RAM_language_interpreter")
    root.iconphoto(False, tk.PhotoImage(file='./ressources/img/ramen.png'))
    # root.geometry("640x480")
    root.update()
    root.minsize(540, 350)
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    MyGUI(root)

    root.mainloop()
