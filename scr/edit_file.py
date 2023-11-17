from terms import root, text, appName, noFileOpenedString, fileTypes, currentFilePath
from tkinter import filedialog
import tkinter as tk


def fileDropDownHandeler(action):
    """
    Handles actions for the File menu dropdown.

    Args:
        action (str): The action to perform (open, new, save, saveAs).
    """

    global currentFilePath
    if action == "open":
        file = filedialog.askopenfilename(filetypes=fileTypes)
        root.title(appName + " - " + file)
        currentFilePath = file
        with open(file, 'r') as f:
            text.delete(1.0, tk.END)
            text.insert(tk.INSERT, f.read())
    elif action == "new":
        currentFilePath = noFileOpenedString
        text.delete(1.0, tk.END)
        root.title(appName + " - " + currentFilePath)
    elif action == "save" or action == "saveAs":
        if currentFilePath == noFileOpenedString or action == 'saveAs':
            currentFilePath = filedialog.asksaveasfilename(filetypes=fileTypes)
        with open(currentFilePath, 'w') as f:
            f.write(text.get('1.0', 'end'))
        root.title(appName + " - " + currentFilePath)
