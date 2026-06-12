import tkinter as tk
from tkinter import ttk

from modules.addFileModule import addFilesMenu
from modules.tagConfigModule import tagConfigMenu

# --- WINDOW SETUP ---

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 850
window_height = 500

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.title('soundcheck')
root.iconbitmap('./assets/soundcheckICO.ico')

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

vfMidCanvas = tk.Canvas(vfFrame, bg='blue')
vfMidCanvas.grid(row=1, column=0, sticky='news')

vfScrollbar = tk.Scrollbar(vfFrame, orient='vertical', command=vfMidCanvas.yview)
vfScrollbar.grid(row=1, column=1, sticky='ns')

vfMidCanvas.configure(yscrollcommand=vfScrollbar.set)

vfMidFrame = tk.Frame(vfMidCanvas, bg='red')
vfMidFrame.pack()

vfMidCanvas.create_window((0, 0), window=vfMidFrame, anchor="nw")
vfMidFrame.bind("<Configure>", lambda e: vfMidCanvas.configure(scrollregion=vfMidCanvas.bbox("all")))

vfBtmFrame = tk.Frame(vfFrame, bg='white')
vfBtmFrame.grid(row=2, column=0, sticky='news')

tk.Frame.tkraise(mainFrame)

# --- STYLES ---

menuMainStyle = ttk.Style()
menuMainStyle.configure("Menu.TButton", font=('Helvetica', 35))

viewFilesTopStyle = ttk.Style()
viewFilesTopStyle.configure("ViewTop.TButton", font=('Helveitca', 20))

# --- MAIN FRAME WIDGETS ---

rawLogoImage = tk.PhotoImage(file='./assets/soundcheckPNG.png')
logoImage = rawLogoImage.subsample(6,6)

title = ttk.Label(mainFrame, image=logoImage, justify='left', text='soundcheck', font=("Helvetica", 50), background='white', compound=tk.LEFT)
title.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='news')

addFilesButton = ttk.Button(mainFrame, text='add files', style="Menu.TButton", command=addFilesMenu)
addFilesButton.grid(row=1, column=0, padx=10, pady=3, sticky='news')

viewFilesButton = ttk.Button(mainFrame, text='view files', style="Menu.TButton", command=lambda:tk.Frame.tkraise(vfFrame))
viewFilesButton.grid(row=2, column=0, padx=10, pady=3, sticky='news')

exitButton = ttk.Button(mainFrame, text='exit', style="Menu.TButton", command=root.destroy)
exitButton.grid(row=3, column=0, padx=10, pady=3, sticky='news')

# --- VIEW FILES FRAME WIDGETS ---

filtersButton = ttk.Menubutton(vfTopFrame, text='tag filters', width=8, style='ViewTop.TButton')

filtersTestList = ["Tag1", "Tag2", "Tag3", "TagA", "TagB"]
filters_menu = tk.Menu(filtersButton, tearoff=0)
for item in filtersTestList:
    filters_menu.add_command(label=item)

filtersButton["menu"] = filters_menu
filtersButton.pack(side='left', padx=10, pady=0)

searchBar = ttk.Entry(vfTopFrame, width=41, font=('Helvetica', 20))
searchBar.pack(side='left', padx=0, pady=0)

searchButton = ttk.Button(vfTopFrame, text='go', width=3, style='ViewTop.TButton', command=lambda:print("We didn't find anything. Because we weren't searching,"))
searchButton.pack(side='left', padx=10, pady=0)

returnButton = ttk.Button(vfBtmFrame, text='return to menu', style='Menu.TButton', command=lambda:tk.Frame.tkraise(mainFrame))
returnButton.pack(side='left', padx=59, pady=0)

configButton = ttk.Button(vfBtmFrame, text='tag configuration', style='Menu.TButton', command=tagConfigMenu)
configButton.pack(side='left', padx=0, pady=0)




# --- INITIALISATION ---

root.mainloop()