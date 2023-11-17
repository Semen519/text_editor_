import tkinter as tk
from terms import text, edit, edit2


def find():
    """
    Finds and highlights occurrences of the search text in the document.
    """
    text.tag_remove('found', '1.0', tk.END)
    search_word = edit.get()
    if search_word:
        index = '1.0'
        while True:
            index = text.search(search_word, index, nocase=1, stopindex=tk.END)
            if not index:
                break
            last_index = '% s+% dc' % (index, len(search_word))
            text.tag_add('found', index, last_index)
            index = last_index
        text.tag_config('found', foreground='red')
    edit.focus_set()


def findNreplace():
    """
    Replaces all occurrences of the search text with the replacement text.
    """
    text.tag_remove('found', '1.0', tk.END)
    search_word = edit.get()
    replace_word = edit2.get()
    if search_word and replace_word:
        index = '1.0'
        while 1:
            index = text.search(search_word, index, nocase=1, stopindex=tk.END)
            if not index:
                break
            last_index = '% s+% dc' % (index, len(search_word))
            text.delete(index, last_index)
            text.insert(index, replace_word)
            last_index = '% s+% dc' % (index, len(replace_word))
            text.tag_add('found', index, last_index)
            index = last_index
        text.tag_config('found', foreground="black")
    edit.focus_set()
