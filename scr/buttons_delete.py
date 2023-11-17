import tkinter as tk
from terms import text


def to_delete_word():
    """
    Deletes the word at the current cursor position.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0]) - 1
    column = int(position.partition('.')[2])
    print(column)
    txt = text.get(1.0, tk.END).split('\n')
    txt = txt[0:-1]
    start_column = column
    end_column = column
    while end_column < len(txt[line]) and not txt[line][end_column].isspace():
        end_column += 1
    while start_column >= 0 and not txt[line][start_column - 1].isspace():
        start_column -= 1
    print(start_column, end_column)
    text.delete(f"{line + 1}.{start_column}", f"{line + 1}.{end_column}")


def to_delete_line():
    """
    Deletes the line at the current cursor position.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0])
    text.delete(f"{line}.0", f"{line + 1}.0")
