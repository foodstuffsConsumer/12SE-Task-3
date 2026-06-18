import tkinter as tk
from tkinter import filedialog

def addEntryMenu():
    filedialog.askopenfilename(initialdir = "/", title = "Select a file.")