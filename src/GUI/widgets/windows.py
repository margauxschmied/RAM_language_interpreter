import tkinter as tk
from tkinter import ttk

import src.GUI.widgets.texte as tx


def create_code_window(my_gui):
    """ Window in which the final code is. """
    code_window = tk.Toplevel(my_gui.root)
    code_window.title("Executed Code RAM")
    code_window.geometry('400x400')
    code_window.withdraw()
    code_window.protocol("WM_DELETE_WINDOW",
                         lambda: my_gui.on_closing(code_window))
    tree_scroll = tk.Scrollbar(code_window)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    executed_code = tx.texte(code_window)
    executed_code.pack(fill=tk.BOTH, expand=1)
    executed_code.configure(state='disabled')
    executed_code.tag_config(
        'mark', foreground="white", background="green")
    tree_scroll.config(command=executed_code.yview)
    my_gui.code_windows.append(code_window)
    my_gui.codes.append(executed_code)


def create_memory_window(my_gui):
    """ Memory in which all used registers are. """
    table_window = tk.Toplevel(my_gui.root)
    table_window.geometry('250x250')
    table_window.resizable(False, False)
    table_window.title("Memory")
    tree_scroll = tk.Scrollbar(table_window)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    table = ttk.Treeview(table_window, yscrollcommand=tree_scroll)
    tree_scroll.config(command=table.yview)
    table['columns'] = ('register', 'value')
    table.column("#0", width=0,  stretch=tk.NO)
    table.column("register", anchor=tk.CENTER, width=80)
    table.column("value", anchor=tk.CENTER, width=80)

    table.heading("#0", text="", anchor=tk.CENTER)
    table.heading("register", text="Register", anchor=tk.CENTER)
    table.heading("value", text="Value", anchor=tk.CENTER)

    table.pack(fill=tk.BOTH, expand=1)

    table_window.withdraw()
    table_window.protocol("WM_DELETE_WINDOW",
                          lambda: my_gui.on_closing(table_window))
    my_gui.table_windows.append(table_window)
    my_gui.tables.append(table)
