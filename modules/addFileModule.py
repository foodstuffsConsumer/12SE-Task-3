import tkinter as tk
from tkinter import filedialog

def addFilesMenu():
    filedialog.askopenfilename(initialdir = "/", title = "Select a file.")