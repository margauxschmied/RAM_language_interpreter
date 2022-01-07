import tkinter as tk

from tkinter.scrolledtext import ScrolledText
# from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class Texte(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, width=20, height=10,
                         bg="lightgrey", wrap='word')
        self.pack(expand=True, fill='both')
        self.add_text('This is an exemple text')

    def add_text(self, txt: str):
        self.insert(tk.END, txt)

    def clean(self):
        self.delete(0, tk.END)

    def add_clean(self, txt: str):
        self.clean()
        self.add_text(txt)

# class MainWindow(tk.PanedWindow):

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("RAM_language_interpreter")
#         self.btn = QPushButton("Execute")
#         self.btn.pressed.connect(self.start_process)
#         self.text = QPlainTextEdit()
#         # self.text.setReadOnly(True)

#         l = QVBoxLayout()
#         l.addWidget(self.btn)
#         l.addWidget(self.text)

#         w = QWidget()
#         w.setLayout(l)

#         self.setCentralWidget(w)

#     def start_process(self):
#         # We'll run our process here.
#         print(self.text.getPaintContext())
#         pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")

    root.iconphoto(False, tk.PhotoImage(file='img/ramen.png'))
    # root.geometry("640x480")

    Texte(root)

    root.mainloop()

    # app = QApplication(sys.argv)
    # # my_icon = QIcon()
    # # my_icon.addFile('ressources/img/ramen.png')
    # #
    # # app.setWindowIcon(my_icon)
    # app.setWindowIcon(QIcon("ressources/img/ramen.png"))
    # app.setDesktopFileName("RAM_language_interpreter")
    #
    # w = MainWindow()
    # w.show()
    #
    # sys.exit(app.exec())
