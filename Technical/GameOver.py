from tkinter import *

def gameover():
    root2 = Tk()
    root2.title("Game")
    over_bg = PhotoImage(file="Over.png")
    back_ov = Label(root2, image=over_bg)
    back_ov.pack()
    root2.mainloop()