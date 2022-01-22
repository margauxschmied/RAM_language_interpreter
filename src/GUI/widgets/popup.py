import tkinter as tk


class popup1(tk.Menu):
    def __init__(self, parent, my_gui):
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.my_gui = my_gui
        self.initialize()

    def initialize(self):
        self.add_command(
            label="Mark This Line as End", command=lambda: self.my_gui.mark_line(self.my_gui.get_current_text_editor(), self.my_gui.get_current_text_editor().index('insert'), True))
        self.add_command(
            label="Remove Line Mark", command=lambda: self.my_gui.remove_mark(self.my_gui.get_current_text_editor(), self.my_gui.get_current_text_editor().index('insert'), True))
        self.add_separator()
        self.add_command(
            label="Execute File", command=lambda: self.my_gui.execute_file())


class popup2(tk.Menu):
    def __init__(self, parent, my_gui):
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.my_gui = my_gui
        self.initialize()

    def initialize(self):
        self.add_command(
            label="Execute Int", command=lambda: self.my_gui.execute_file())
        self.add_separator()
        self.add_command(
            label="Convert Into RAM in New File", command=lambda: self.my_gui.convert_int_new_file())
