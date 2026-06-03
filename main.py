import tkinter as tk
from tkinter import ttk

from addFileModule import addFilesMenu
from viewFileModule import viewFilesMenu

# --- WINDOW SETUP ---

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 850
window_height = 500

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# --- WINDOW CONTENT ---

root.title('soundcheck')
root.iconbitmap('./assets/soundcheckICO.ico')

rawImage = tk.PhotoImage(file='./assets/soundcheckPNG.png')
image = rawImage.subsample(6,6)

image_label = ttk.Label(
    root,
    image=image,
    justify='left',
    text='SoundCheck', 
    font=("Helvetica", 50),
    compound=tk.LEFT
)
image_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

menuStyle = ttk.Style()
menuStyle.configure("MMS.TButton", font=('Helvetica', 35))

addFilesButton = ttk.Button(root, text='Add Files', style="MMS.TButton", command=addFilesMenu)
addFilesButton.grid(row=1, column=0, padx=10, pady=3, sticky='w')

viewFilesButton = ttk.Button(root, text='View Files', style="MMS.TButton", command=viewFilesMenu)
viewFilesButton.grid(row=2, column=0, padx=10, pady=3, sticky='w')

exitButton = ttk.Button(root, text='Exit', style="MMS.TButton", command=root.destroy)
exitButton.grid(row=3, column=0, padx=10, pady=3, sticky='w')

root.mainloop()