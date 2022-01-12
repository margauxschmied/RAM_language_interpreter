import tkinter as tk
from main import Frame
inc = '#include '
de = '#define '


def copy_text(text_editor):
    text = tk.Text()
    text.insert('1.0', text_editor.get('1.0', 'end-1c'))
    return text


def file_includes(text_editor, output):
    index = '1.0'

    text_editor_temp = copy_text(text_editor)

    while index:
        index = text_editor_temp.search(inc, '1.0', stopindex=tk.END)

        if index != '':
            index_end = Frame.idx_to_nb(index) + '.end'
            line = text_editor_temp.get(index, index_end)
            path = line[len(inc):]

            text_editor_temp.delete(index, index_end)

            try:
                f2 = open(path, 'r')
                text_editor_temp.insert(index, f2.read())
                f2.close()

            except FileNotFoundError:
                output.pretty_print(
                    '[' + line + '] (line ' + Frame.idx_to_nb(index) + '): ', 'blue')
                output.pretty_print(" File not found\n", 'red')
                continue

    return text_editor_temp


def replace_all(text_editor, word, replace):
    text = text_editor.get('1.0', 'end-1c')
    text = text.replace(word, replace)
    text_editor.delete('1.0', tk.END)
    text_editor.insert('1.0', text)


def user_defines(text_editor, output):
    index = '1.0'

    text_editor_temp = copy_text(text_editor)

    while index:
        index = text_editor_temp.search(de, '1.0', stopindex=tk.END)
        if index != '':
            index_end = Frame.idx_to_nb(index) + '.end'
            line = text_editor_temp.get(index, index_end)
            text_editor_temp.delete(index, index_end)
            words = line.split(' ')
            if len(words) != 3:
                output.pretty_print(
                    '[' + line + '] (line ' + Frame.idx_to_nb(index) + '): ', 'blue')
                output.pretty_print(
                    " 2 parameters expected (found " + str(len(words) - 1) + ')\n', 'red')
                continue
            word = words[1]
            replace = words[2]
            replace_all(text_editor_temp, word, replace)

    return text_editor_temp
