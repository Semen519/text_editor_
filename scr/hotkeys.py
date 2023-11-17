from terms import root, appName, currentFilePath
from edit_file import fileDropDownHandeler


def textchange(event):
    """
    Updates the window title to indicate that the file has changed.

    Args:
        event: The tkinter event object.
    """
    root.title(appName + " - *" + currentFilePath)


def quit_program(e):
    """
    Closes the application.

    Args:
        e: The tkinter event object.
    """
    root.destroy()


def save_program(e):
    """
    Saves the file.

    Args:
        e: The tkinter event object.
    """
    fileDropDownHandeler("save")
