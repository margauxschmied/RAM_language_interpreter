import tkinter as tk
from tkinter import ttk


class toolbar(ttk.Frame):
    """ The icon bar which appear just below the menu bar. """

    def __init__(self, parent, my_gui):
        super().__init__(parent)
        self.parent = parent
        self.my_gui = my_gui
        self.initialize()

    def initialize(self):
        icon1 = tk.PhotoImage(
            file='./ressources/img/run.png')
        icon2 = tk.PhotoImage(
            file='./ressources/img/stop.png')
        icon3 = tk.PhotoImage(
            file='./ressources/img/save.png')
        icon4 = tk.PhotoImage(
            file='./ressources/img/cover.png')
        i1 = icon1.subsample(3, 3)
        i2 = icon2.subsample(3, 3)
        i3 = icon3.subsample(3, 3)
        i4 = icon4.subsample(3, 3)

        self.run_button = ttk.Button(
            self, image=i4, command=lambda: self.my_gui.execute_file())
        self.stop_button = ttk.Button(
            self, image=i2, command=lambda: self.my_gui.stop())
        self.save_button = ttk.Button(
            self, image=i3, command=lambda: self.my_gui.save_file())
        self.cover_button = ttk.Button(
            self, image=i1, command=lambda: self.my_gui.execute_line())
        self.run_button.image = i4
        self.stop_button.image = i2
        self.save_button.image = i3
        self.cover_button.image = i1

        self.pack(fill=tk.X)
        self.save_button.grid(column=0, row=0, pady=2)
        self.run_button.grid(column=1, row=0, pady=2, padx=5)
        self.cover_button.grid(column=2, row=0, pady=2)
        self.stop_button.grid(column=3, row=0, pady=2)
