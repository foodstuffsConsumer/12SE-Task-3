from tkinter import filedialog
from pathlib import Path

def addEntryMenu():
    entry = filedialog.askopenfilename(initialdir = "/", title = "Select a file.")
    return Path(entry)
    