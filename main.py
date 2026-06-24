import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from modules.tagConfigModule import tagConfigMenu
from modules.entryTagsModule import entryTagsPopup

# --- FUNCTIONS ---

def addEntryMenu():
    file = filedialog.askopenfilename(initialdir = "/", title = "Select a file.")
    if not file:
        return
    
    entry = {
        "file": file,
        "tags": []
    }

    try:
        with open('data.json') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(entry)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=1)

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

vfMidCanvas = tk.Canvas(vfFrame)
vfMidCanvas.grid(row=1, column=0, sticky='news')

vfMidScrollbar = tk.Scrollbar(vfFrame, orient='vertical', command=vfMidCanvas.yview)
vfMidScrollbar.grid(row=1, column=1, sticky='news')

vfMidCanvas.configure(yscrollcommand=vfMidScrollbar.set)
vfMidFrame = tk.Frame(vfMidCanvas)

vfMidCanvas.create_window((0, 0), window=vfMidFrame, anchor="nw")
vfMidFrame.bind("<Configure>", lambda e: vfMidCanvas.configure(scrollregion=vfMidCanvas.bbox("all")))

vfMidFrame.grid_columnconfigure(0, weight=10)
vfMidFrame.grid_columnconfigure(1, weight=0)

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

viewEntriesButton = ttk.Button(mainFrame, text='view entries', style="Menu.TButton", command=lambda:tk.Frame.tkraise(vfFrame))
viewEntriesButton.grid(row=2, column=0, padx=10, pady=3, sticky='news')

exitButton = ttk.Button(mainFrame, text='exit', style="Menu.TButton", command=root.destroy)
exitButton.grid(row=3, column=0, padx=10, pady=3, sticky='news')

# --- VIEW ENTRIES FRAME WIDGETS ---

filtersButton = ttk.Menubutton(vfTopFrame, text='tag filters', width=8, style='ViewEntries.TButton')

filtersTestList = ["Tag1", "Tag2", "Tag3", "TagA", "TagB"]
filters_menu = tk.Menu(filtersButton, tearoff=0)
for item in filtersTestList:
    filters_menu.add_command(label=item)

filtersButton["menu"] = filters_menu
filtersButton.pack(side='left', padx=10, pady=0)

searchBar = ttk.Entry(vfTopFrame, width=41, font=('Helvetica', 20))
searchBar.pack(side='left', padx=0, pady=0)

searchButton = ttk.Button(vfTopFrame, text='go', width=3, style='ViewEntries.TButton', command=lambda:print("We didn't find anything. Because we weren't searching,"))
searchButton.pack(side='left', padx=10, pady=0)

returnButton = ttk.Button(vfBtmFrame, text='return to menu', style='Menu.TButton', command=lambda:tk.Frame.tkraise(mainFrame))
returnButton.pack(side='left', padx=59, pady=0)

configButton = ttk.Button(vfBtmFrame, text='tag configuration', style='Menu.TButton', command=tagConfigMenu)
configButton.pack(side='left', padx=0, pady=0)

rawJMPImage = tk.PhotoImage(file='./assets/jumptofile.png')
JMPImage = rawJMPImage.subsample(6, 6)

rawTAGImage = tk.PhotoImage(file="./assets/tags.png")
TAGImage = rawTAGImage.subsample(6, 6)

rawDELImage = tk.PhotoImage(file="./assets/delete.png")
DELImage = rawDELImage.subsample(6, 6)

for i in range(30):
    ttk.Label(vfMidFrame, text=f"test item number {i+1}", font=('Helvetica', 20), background='white', width=43).grid(row=i, column=0, padx=5, pady=5, sticky='news')
    ttk.Button(vfMidFrame, image=JMPImage, command=lambda:print("Jump To File"),width=3).grid(row=i, column=1, padx=5, pady=5, sticky='news')
    ttk.Button(vfMidFrame, image=TAGImage, command=lambda:entryTagsPopup(),width=3).grid(row=i, column=2, padx=5, pady=5, sticky='news')
    ttk.Button(vfMidFrame, image=DELImage, command=lambda:print("Delete Entry"),width=3).grid(row=i, column=3, padx=5, pady=5, sticky='news')

# --- INITIALISATION ---

root.mainloop()