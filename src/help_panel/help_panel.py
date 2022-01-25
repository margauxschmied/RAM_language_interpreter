from tkinter import *
from tkhtmlview import HTMLLabel

import sys
text_for_help = 'src/help_panel/text_help_panel/'


"""This file aims to mange the tag Help"""

button_properties = {
    'relief': 'solid',
    'activebackground': '#F9FC77',
    'cursor': 'hand2',
    'width': 20
}

file_path_list = [
    ('File', 'text_file.html'),
    ('Run', 'text_run.html'),
    ('Stop', 'text_stop.html'),
    ('Options', 'text_options.html'),
    ('Shortcuts', 'text_shortcuts.html'),
    ('Icons', 'text_icons.html'),

]


def right_empty_panel(parent):
    panel_right_empty = PanedWindow(parent)
    panel_right_empty.pack()


def clean_panel(panel):
    [i.destroy() for i in panel.winfo_children()]


def right_panel(parent, file_path_list):
    clean_panel(parent)
    file = open(file_path_list, 'r')
    data = file.read()
    my_label = HTMLLabel(parent, html=data)
    my_label.pack(pady=20, padx=20)
    file.close()


def create_button(panel_left, panel_right, pos):
    return Button(panel_left,
                  **button_properties,
                  text=file_path_list[pos][0],
                  command=lambda: right_panel(panel_right, text_for_help + file_path_list[pos][1]))


def main(root):
    parent = Toplevel(root)
    panel_left = PanedWindow(parent)
    panel_right = PanedWindow(parent)
    button_list = [create_button(panel_left, panel_right, i)
                   for i in range(len(file_path_list))]
    for pos, button in enumerate(button_list):
        button.grid(column=0, row=pos, pady=5)
    panel_left.pack(side="left")
    panel_right.pack(expand=1, fill=BOTH)
    root.mainloop()
