import tkinter as tk
from tkinter import ttk
from addFileModule import addFilesMenu

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

mainFrame = tk.Frame(root, bg='white')
mainFrame.grid(row=0, column=0, sticky='news')

vfFrame = tk.Frame(root, bg='white')
vfFrame.grid(row=0, column=0, sticky='news')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

tk.Frame.tkraise(mainFrame)

# --- STYLES ---

menuStyle = ttk.Style()
menuStyle.configure("Menu.TButton", font=('Helvetica', 35))

# --- MAIN FRAME WIDGETS ---

rawImage = tk.PhotoImage(file='./assets/soundcheckPNG.png')
image = rawImage.subsample(6,6)

title = ttk.Label(mainFrame, image=image, justify='left', text='soundcheck', font=("Helvetica", 50), background='white', compound=tk.LEFT)
title.grid(sticky='news', row=0, column=0, columnspan=3, padx=10, pady=10)

addFilesButton = ttk.Button(mainFrame, text='add files', style="Menu.TButton", command=addFilesMenu)
addFilesButton.grid(sticky='news', row=1, column=0, padx=10, pady=3)

viewFilesButton = ttk.Button(mainFrame, text='view files', style="Menu.TButton", command=lambda:tk.Frame.tkraise(vfFrame))
viewFilesButton.grid(sticky='news', row=2, column=0, padx=10, pady=3)

exitButton = ttk.Button(mainFrame, text='exit', style="Menu.TButton", command=root.destroy)
exitButton.grid(sticky='news', row=3, column=0, padx=10, pady=3)

# --- VIEW FILES FRAME WIDGETS ---

ITWORKs = ttk.Label(vfFrame, text="You're MOM! ARGHARHAHRHAR", background='white', font=("Helvetical", 35))
ITWORKs.pack()

backtomain = ttk.Button(vfFrame, text='i wanna go home', style='Menu.TButton', command=lambda:tk.Frame.tkraise(mainFrame))
backtomain.pack()

# --- INITIALISATION ---

root.mainloop()