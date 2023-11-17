from tkinter import Tk, scrolledtext, Frame, Entry

appName = 'Text editor by Semyon'  # Application name
noFileOpenedString = 'New File'  # Default string for new files
currentFilePath = noFileOpenedString  # Path of the currently opened file
fileTypes = [("Text Files", "*.txt"), ("Markdown", "*.md")]  # Supported file types

root = Tk()  # Main Tkinter window
text = scrolledtext.ScrolledText(root, height=999)  # Main text area
frame = Frame(root)  # Frame to hold buttons and entries
edit = Entry(frame)  # Entry field for Find
edit2 = Entry(frame)  # Entry field for Replace
