import tkinter as tk
import sys
from terms import appName, noFileOpenedString, currentFilePath, fileTypes, root, text, frame, edit, edit2
from edit_file import fileDropDownHandeler
from hotkeys import textchange, quit_program, save_program
from buttons_find import find, findNreplace
from buttons_move import word_to_left, word_to_right, line_end, line_start
from buttons_delete import to_delete_line, to_delete_word


def make_menu():
    """
    Creates the main menu for the text editor.
    """
    root.geometry('300x300')
    root.minsize(height=360, width=920)
    root.title(appName + '-' + currentFilePath)
    root.grid_columnconfigure(0, weight=1)
    menu = tk.Menu(root)
    fileDropdown = tk.Menu(menu, tearoff=False)
    fileDropdown.add_command(label='New', command=lambda: fileDropDownHandeler("new"))
    fileDropdown.add_command(label='Open', command=lambda: fileDropDownHandeler("open"))
    fileDropdown.add_separator()
    fileDropdown.add_command(label='Save', command=lambda: fileDropDownHandeler("save"))
    fileDropdown.add_command(label='Save as', command=lambda: fileDropDownHandeler("saveAs"))
    menu.add_cascade(label='File', menu=fileDropdown)
    root.config(menu=menu)


if __name__ == '__main__':

    make_menu()

    # Code to create and pack buttons and labels
    Find = tk.Button(frame, text='Find')
    replace = tk.Button(frame, text='FindNReplace')
    word_left = tk.Button(frame, text='<--word')
    word_right = tk.Button(frame, text='word-->')
    line_left = tk.Button(frame, text='to start of line')
    line_right = tk.Button(frame, text='to end of line')
    delete_word = tk.Button(frame, text='delete word')
    delete_line = tk.Button(frame, text='delete line')

    tk.Label(frame, text='Find').pack(side=tk.LEFT)
    edit.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    edit.focus_set()
    Find.pack(side=tk.LEFT)
    tk.Label(frame, text="Replace With ").pack(side=tk.LEFT)
    edit2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    edit2.focus_set()
    replace.pack(side=tk.LEFT)
    word_left.pack(side=tk.LEFT, padx=[20, 0])
    word_right.pack(side=tk.LEFT)
    line_left.pack(side=tk.LEFT)
    line_right.pack(side=tk.LEFT)
    delete_word.pack(side=tk.LEFT)
    delete_line.pack(side=tk.LEFT)
    frame.pack(side=tk.TOP)

    # Bind hotkeys for text change, quit, and save
    text.pack(side=tk.BOTTOM, fill=tk.BOTH)
    text.bind('<KeyPress>', textchange)
    text.bind('<Control-x>', quit_program)
    text.bind('<Control-s>', save_program)

    # Code to handle opening a file via command line argument
    if len(sys.argv) == 2:
        currentFilePath = sys.argv[1]
        root.title(appName + " - " + currentFilePath)
        with open(currentFilePath, 'r') as f:
            text.delete(1.0, tk.END)
            text.insert(tk.INSERT, f.read())

    # Configure button commands
    delete_word.config(command=to_delete_word)
    delete_line.config(command=to_delete_line)
    line_left.config(command=line_start)
    line_right.config(command=line_end)
    word_right.config(command=word_to_right)
    word_left.config(command=word_to_left)
    Find.config(command=find)
    replace.config(command=findNreplace)

    root.mainloop()
