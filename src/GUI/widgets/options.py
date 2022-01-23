from pathlib import Path
import os
import json
import tkinter as tk
from tkinter import ttk
dir_path = './src/GUI/settings'
file_path = dir_path + '/config.json'


class option_window(tk.Toplevel):
    def __init__(self, parent, my_gui):
        super().__init__(parent)
        self.parent = parent
        self.my_gui = my_gui
        self.initialize()

    def initialize(self):

        self.title("Options")
        self.grab_set()
        self.focus()
        self.geometry("285x90")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW",
                      lambda: self.my_gui.reset_destroy(self))
        check1 = ttk.Checkbutton(self, text='Show Line Numbers',
                                 variable=self.my_gui.choice_show_line_numbers, onvalue=1, offvalue=0)
        check1.grid(column=0, row=0, sticky='W')
        check2 = ttk.Checkbutton(
            self, text='Automaticaly Open Executed Code Window', variable=self.my_gui.choice_automaticaly_code, onvalue=1, offvalue=0)
        check2.grid(column=0, row=1, sticky='W')

        check3 = ttk.Checkbutton(
            self, text='Automaticaly Open Memory Window', variable=self.my_gui.choice_automaticaly_memory, onvalue=1, offvalue=0)
        check3.grid(column=0, row=2, sticky='W')

        valid = ttk.Button(self, text="Confirm",
                           command=lambda: self.my_gui.save_destroy(self))
        valid.grid(column=0, row=3)


def save(data):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    file = Path(file_path)
    file.touch(exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f)


def read():
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return {'show_line': '1', 'open_code': '1', 'open_memory': '1'}
