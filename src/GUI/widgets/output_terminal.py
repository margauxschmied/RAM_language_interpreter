from tkinter.scrolledtext import ScrolledText


class output_terminal(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, bg="white", wrap='word')

        self.configure(state='disabled')
        self.tag_config('blue', foreground="blue")
        self.tag_config('red', foreground="red")
        self.tag_config('orange', foreground="orange")
        self.tag_config('gray', foreground="gray30")
        self.tag_config('green', foreground="green")
        self.tag_config('black', foreground="black")

    def pretty_print(self, s, fg='black'):
        self.configure(state='normal')
        self.insert('end', s, fg)
        self.yview_moveto(1)
        self.configure(state='disabled')
