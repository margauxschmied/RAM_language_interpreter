import tkinter as tk


class toolbar(tk.Frame):
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

        self.run_button = tk.Button(
            self, image=i4, command=lambda: self.my_gui.execute_file())
        self.stop_button = tk.Button(
            self, image=i2, command=lambda: self.my_gui.stop())
        self.save_button = tk.Button(
            self, image=i3, command=lambda: self.my_gui.save_file())
        self.cover_button = tk.Button(
            self, image=i1, command=lambda: self.my_gui.execute_line())
        self.run_button.image = i4
        self.stop_button.image = i2
        self.save_button.image = i3
        self.cover_button.image = i1

        self.pack(fill=tk.X)
        self.save_button.grid(column=0, row=0)
        self.run_button.grid(column=1, row=0, padx=5)
        self.cover_button.grid(column=2, row=0)
        self.stop_button.grid(column=3, row=0)
