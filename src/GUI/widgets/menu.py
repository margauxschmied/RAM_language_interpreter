import tkinter as tk

from src.GUI.widgets.cantor_top_level import create_cantor_panel


class menu_bar(tk.Menu):
    """ This class represents the bar menu (File, Run, Stop, etc.). """

    def __init__(self, parent, my_gui):
        super().__init__(parent)
        self.parent = parent
        self.my_gui = my_gui
        self.initialize()

    def initialize(self):

        # The 'File' contextual menu
        self.menu_file = tk.Menu(self, tearoff=0)
        self.menu_file.add_command(
            label="New File", command=lambda: self.my_gui.new_file(), accelerator="Ctrl+N")
        self.menu_file.add_command(
            label="Open File", command=lambda: self.my_gui.open_file())
        self.menu_file.add_command(
            label="Save", command=lambda: self.my_gui.save_file(), accelerator="Ctrl+S")

        self.menu_file.add_separator()
        self.menu_file.add_command(
            label="Exit", command=lambda: self.my_gui.root.destroy(), accelerator="Esc")

        self.menu_file.add_command(
            label='Cantor calculator', command=lambda: create_cantor_panel(self.master))
        self.add_cascade(label="File", menu=self.menu_file)

        # The 'Run' contextual menu
        self.menu_run = tk.Menu(self, tearoff=0)
        self.menu_run.add_command(
            label="Start", command=self.my_gui.execute_line, accelerator="Ctrl+Enter")
        self.menu_run.add_command(
            label="Run Next Instruction", command=self.my_gui.execute_line, accelerator="Ctrl+Enter")
        self.menu_run.add_command(
            label="Run All Instructions", command=lambda: self.my_gui.execute_line(all=True), accelerator="Ctrl+M")
        self.menu_run.add_separator()
        self.menu_run.add_command(
            label="Run File", command=self.my_gui.execute_file, accelerator="Ctrl+Shit+Enter")
        self.add_cascade(label="Run", menu=self.menu_run)

        self.menu_run.entryconfig(1, state='disabled')

        # The 'Stop' button
        self.add_command(
            label="Stop", command=lambda: self.my_gui.stop())
        self.entryconfig(3, state='disabled')

        # The 'Option' button
        self.add_command(
            label="Options", command=self.my_gui.open_option)

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self, tearoff=0)
        self.menu_help.add_command(
            label="Get Started", command=lambda: self.my_gui.output.pretty_print("TODO: User Manual\n", 'blue'))
        self.menu_help.add_command(
            label="RAM Instructions", command=lambda: self.my_gui.output.pretty_print("TODO: RAM\n", 'blue'))
        self.menu_help.add_command(
            label="About", command=lambda: self.my_gui.output.pretty_print("TODO: About\n", 'blue'))

        self.add_cascade(label="Help", menu=self.menu_help)
