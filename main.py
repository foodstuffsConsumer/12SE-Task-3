import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

try:
    with open('data.json') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

searchedData = []

# --- FUNCTIONS ---

def makeScrollableFrame(parent, row=1, column=0):
    canvas = tk.Canvas(parent)
    canvas.grid(row=row, column=column, sticky='news')

    scrollbar = tk.Scrollbar(parent, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=row, column=column + 1, sticky='news')

    canvas.configure(yscrollcommand=scrollbar.set)
    frame = tk.Frame(canvas)

    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind(
        "<Configure>",
        lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    frame.grid_columnconfigure(0, weight=10)
    frame.grid_columnconfigure(1, weight=0)

    return canvas, scrollbar, frame

def jumpToFile(filepath):
    os.startfile(filepath)

def deleteEntry(delEntry):
    data.remove(delEntry)
    if delEntry in searchedData:
        searchedData.remove(delEntry)

    updateEntries(vfMidFrame, data)
    updateEntries(vfMidFrameSR, searchedData)

def swapMenu(frame):
    tk.Frame.tkraise(frame)
    tk.Frame.tkraise(vfMidCanvas)
    searchBar.delete(0, tk.END)

def searchForEntry(frame, toSearch):
    if not toSearch:
        tk.Frame.tkraise(vfMidCanvas)
        return
    
    rawTexts = []
    texts = []
    for child in frame.winfo_children():
        if isinstance(child, ttk.Label):
            rawTexts.append(child.cget("text"))
    for item in rawTexts:
        if toSearch in item:
            texts.append(item)
    tk.Frame.tkraise(vfMidCanvasSR)

    for i in data:
        for j in i.values():
            if j in texts:
                searchedData.append(i)

    updateEntries(vfMidFrameSR, searchedData)

def updateEntries(frame, list):
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(len(list)):
        ttk.Label(frame, text=list[i]['name'], font=('Helvetica', 20), background='white', width=47).grid(row=i, column=0, padx=5, pady=5, sticky='news')
        ttk.Button(frame, image=JMPImage, command=lambda i=i:jumpToFile(list[i]['filepath']),width=3).grid(row=i, column=1, padx=5, pady=5, sticky='news')
        ttk.Button(frame, image=DELImage, command=lambda i=i:deleteEntry(list[i]),width=3).grid(row=i, column=3, padx=5, pady=5, sticky='news')

    with open("data.json", "w") as f:
        json.dump(data, f, indent=1)

def addEntryMenu():
    file = filedialog.askopenfilename(initialdir = "/", title = "Select a file.")
    if not file:
        return
    
    entry = {
        "filepath": file,
        "name": Path(file).stem,
    }

    data.append(entry)

    updateEntries(vfMidFrame, data)

# --- WINDOW SETUP ---

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 850
window_height = 500

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.title('filecheck')
root.iconbitmap('./assets/filecheckICO.ico')

root.resizable(0, 0)

# --- FRAME SETUP ---

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

mainFrame = tk.Frame(root, bg='white')
mainFrame.grid(row=0, column=0, sticky='news')

vfFrame = tk.Frame(root, bg='white')
vfFrame.grid(row=0, column=0, sticky='news')

vfFrame.grid_rowconfigure(0, weight=2)
vfFrame.grid_rowconfigure(1, weight=15)
vfFrame.grid_rowconfigure(2, weight=3)
vfFrame.grid_columnconfigure(0, weight=1)

vfTopFrame = tk.Frame(vfFrame, bg='white')
vfTopFrame.grid(row=0, column=0, sticky='news')

vfMidCanvas, vfMidScrollbar, vfMidFrame = makeScrollableFrame(vfFrame, row=1, column=0)
vfMidCanvasSR, vfMidScrollbarSR, vfMidFrameSR = makeScrollableFrame(vfFrame, row=1, column=0)
tk.Frame.tkraise(vfMidCanvas)

vfBtmFrame = tk.Frame(vfFrame, bg='white')
vfBtmFrame.grid(row=2, column=0, sticky='news')

tk.Frame.tkraise(mainFrame)

# --- STYLES ---

menuMainStyle = ttk.Style()
menuMainStyle.configure("Menu.TButton", font=('Helvetica', 35))

viewEntriesStyle = ttk.Style()
viewEntriesStyle.configure("ViewEntries.TButton", font=('Helveitca', 20))

# --- MAIN FRAME WIDGETS ---

rawLogoImage = tk.PhotoImage(file='./assets/filecheckPNG.png')
logoImage = rawLogoImage.subsample(6,6)

title = ttk.Label(mainFrame, image=logoImage, justify='left', text='filecheck', font=("Helvetica", 50), background='white', compound=tk.LEFT)
title.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='news')

addEntriesButton = ttk.Button(mainFrame, text='add entries', style="Menu.TButton", command=addEntryMenu)
addEntriesButton.grid(row=1, column=0, padx=10, pady=3, sticky='news')

viewEntriesButton = ttk.Button(mainFrame, text='view entries', style="Menu.TButton", command=lambda:swapMenu(vfFrame))
viewEntriesButton.grid(row=2, column=0, padx=10, pady=3, sticky='news')

exitButton = ttk.Button(mainFrame, text='exit', style="Menu.TButton", command=root.destroy)
exitButton.grid(row=3, column=0, padx=10, pady=3, sticky='news')

# --- VIEW ENTRIES FRAME WIDGETS ---

searchBar = ttk.Entry(vfTopFrame, width=49, font=('Helvetica', 20))
searchBar.pack(side='left', padx=20, pady=0)

searchButton = ttk.Button(vfTopFrame, text='go', width=3, style='ViewEntries.TButton', command=lambda:searchForEntry(vfMidFrame, searchBar.get()))
searchButton.pack(side='left', padx=0, pady=0)

returnButton = ttk.Button(vfBtmFrame, text='return to menu', style='Menu.TButton', command=lambda:swapMenu(mainFrame))
returnButton.pack(side='bottom', padx=0, pady=10)

rawJMPImage = tk.PhotoImage(file='./assets/jumptofile.png')
JMPImage = rawJMPImage.subsample(6, 6)

rawDELImage = tk.PhotoImage(file="./assets/delete.png")
DELImage = rawDELImage.subsample(6, 6)

# --- INITIALISATION ---

updateEntries(vfMidFrame, data)
root.mainloop()