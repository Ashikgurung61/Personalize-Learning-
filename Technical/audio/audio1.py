from playsound import playsound
from tkinter import *

def audio():
    playsound("audio/Audio/Audio/1723494812506d76xcoyu-voicemaker.in-speech.mp3")

root8 = Tk()

_ = Label(root8, text = "WHat is the name of our University").pack()
play = Button(root8, text = "Play", command=audio).pack()

root8.mainloop()