import tkinter as tk
from terms import text


def word_to_left():
    """
    Moves the cursor to the start of the previous word.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0]) - 1
    column = int(position.partition('.')[2])
    txt = text.get(1.0, tk.END).split('\n')
    if column == 0 and line != 0:
        if line != 0:
            line -= 1
            while len(txt[line]) == 0 and line > 0:
                line -= 1
            if len(txt[line]) != 0:
                column = len(txt[line]) - 1
    else:
        column -= 1
    while column < len(txt[line]) and txt[line][column].isspace():
        if column == 0:
            if line != 0:
                line -= 1
                while len(txt[line]) == 0 and line > 0:
                    line -= 1
                if len(txt[line]) == 0:
                    break
                column = len(txt[line]) - 1
            else:
                break
        else:
            column -= 1
    while column > 0 and not txt[line][column].isspace():
        column -= 1
    if column < len(txt[line]) and txt[line][column].isspace():
        column += 1
    text.mark_set("insert", "%d.%d" % (line + 1, column))


def word_to_right():
    """
    Moves the cursor to the start of the next word.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0]) - 1
    column = int(position.partition('.')[2])
    txt = text.get(1.0, tk.END).split('\n')
    txt = txt[0:-1]
    while column < len(txt[line]) and not txt[line][column].isspace():
        column += 1
    while column < len(txt[line]) and txt[line][column].isspace():
        column += 1
    if column == len(txt[line]) and line != len(txt) - 1:
        line += 1
        while line < len(txt) - 1 and len(txt[line]) == 0:
            line += 1
        column = 0
    while column < len(txt[line]) and txt[line][column].isspace():
        column += 1
    text.mark_set("insert", "%d.%d" % (line + 1, column))


def line_start():
    """
    Moves the cursor to the start of the current line.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0]) - 1
    text.mark_set("insert", "%d.%d" % (line + 1, 0))


def line_end():
    """
    Moves the cursor to the end of the current line.
    """
    position = text.index(tk.INSERT)
    line = int(position.partition('.')[0]) - 1
    txt = text.get(1.0, tk.END).split('\n')
    text.mark_set("insert", "%d.%d" % (line + 1, len(txt[line])))
