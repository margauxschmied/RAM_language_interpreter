import tkinter as tk

from tkinter.scrolledtext import ScrolledText
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class Texte(tk.Text):
    def __init__(self, parent):
        # self = tk.Text(root)

        self = ScrolledText(parent, width=20, height=10, bg="lightgrey", wrap="none")


        self.grid(row=0, column=0, sticky="nsew")
        self.insert(tk.END, 'This is an example text.')
        self.pack(expand=True, fill='both')

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAM_language_interpreter")
        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        # self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def start_process(self):
        # We'll run our process here.
        print(self.text.getPaintContext())
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RAM_language_interpreter")

    root.iconphoto(False, tk.PhotoImage(file='img/ramen.png'))
    root.geometry("640x480")

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
