import tkinter as tk

from src.GUI.widgets.cantor_top_level import create_cantor_panel
from src.help_panel import help_panel
from src.ram_instructions import ram_instr
from src.about import about


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
            label="Open File", command=lambda: self.my_gui.open_file(), accelerator="Ctrl+O")
        self.menu_file.add_command(
            label="Save", command=lambda: self.my_gui.save_file(), accelerator="Ctrl+S")

        self.menu_file.add_separator()
        self.menu_file.add_command(
            label="Exit", command=lambda: self.my_gui.root.destroy(), accelerator="Esc")

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

        # The 'Utility Tools'
        self.menu_tools = tk.Menu(self, tearoff=0)
        self.menu_tools.add_command(
            label='Apply Preprocessing', command=lambda: self.my_gui.apply_preprocessing())
        self.menu_tools.add_separator()
        self.menu_tools.add_command(
            label='Cantor Encode', command=lambda: create_cantor_panel(self.master, True))
        self.menu_tools.add_command(
            label='Cantor Decode', command=lambda: create_cantor_panel(self.master, False))
        self.add_cascade(label="Tools", menu=self.menu_tools)

        # The 'Option' button
        self.add_command(
            label="Options", command=self.my_gui.open_option)

        # The 'Help' contextual menu
        self.menu_help = tk.Menu(self, tearoff=0)
        self.menu_help.add_command(
            label="Get Started", command=lambda: help_panel.main(self.master))
        self.menu_help.add_command(
            label="RAM Instructions", command=lambda: ram_instr.open_ram_instr(self.master))
        self.menu_help.add_command(
            label="About", command=lambda: about.open_about(self.master))

        self.add_cascade(label="Help", menu=self.menu_help)
