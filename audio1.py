from playsound import playsound
from tkinter import *
from tkinter import messagebox
import random
from final_process import add_data
def audio():
    playsound("audio/Audio`s/Audio/1723494812506d76xcoyu-voicemaker.in-speech.mp3")

def countdown(time_left):
    global label, alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = root11.after(1000, countdown, time_left - 1)
        alu = cur.split('#')[1]
        print("Level1: ", cur)
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")

def skipnow():
    global val, correct_opt
    correct_opt = 0
    val=messagebox.askokcancel("Skip","Are you sure!")
    if val== True:
        finale()

def opt1_func():
    global correct_opt
    correct_opt=1
    next_button = Button(root11, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)

def opt2_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root11, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def opt3_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root11, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
   
def opt4_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root11, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def finale():
    now=abs(int(alu)-int(ti))
    A1Time.append(now)
    A1Marks.append(correct_opt)
    # countS += 1
    if correct_opt == 1:
        A1Next.append(True)
    else:
        A1Next.append(False)
    A1Skip.append(val)
    print(A1next_game_call)
    if A1CountScreen == 5:
        root11.destroy()
        add_data(A1Time, A1Title, A1Marks,A1Skip, A1Next, A1CountScreen,A1a)
        
    nextLevel = random.choices(A1next_game_call)[0]
    A1next_game_call.remove(nextLevel)
    root11.destroy()
    nextLevel(A1Time, A1Title, A1Marks,A1Skip, A1Next, A1CountScreen,A1a, A1next_game_call)
    
    #print("Marks: ", correct_opt,"Time", now)
    #print(f"Time: {P3Time}, Title: {P3Title}, Marks: {P3Marks}, SKip: {P3Skip}, Next: {P3Next}, Screen_Count: {P3CountScreen}, Last : {P3a}, Fun: {P3next_game_call}")
    


def Audio1(Time,Title,Marks,Skip,Next,CountScreen,a,next_game_call):
    global root11, label, setTimers,A1Next,A1Time,A1Title,A1a,A1CountScreen,A1Marks,A1next_game_call,A1Skip
    global ti, val, play_count
    A1Time=Time
    A1Title= Title
    A1Marks=Marks
    A1Skip=Skip
    A1Next=Next
    A1CountScreen=CountScreen
    A1a=a
    A1next_game_call=next_game_call

    A1CountScreen+=1
    A1Title.append('Audio1')
    
    ti=0
    for t in A1Time:
        ti += int(t)
    play_count = 0
    root11 = Tk()
    root11.geometry("800x632")

    opt1 = PhotoImage(file="audio/Audio1/opt1.png")
    opt2 = PhotoImage(file="audio/Audio1/opt2.png")
    opt3 = PhotoImage(file="audio/Audio1/opt3.png")
    opt4 = PhotoImage(file="audio/Audio1/opt4.png")

    play_sound=PhotoImage(file="audio/Audio1/play.png")

    back_img = PhotoImage(file = "audio/Audio1/AUDIO1img.png")
    back_label = Label(root11, image= back_img)
    back_label.pack()

    play = Button(root11, command=audio, border=0,image=play_sound,highlightthickness=0)
    play.place(x = 50, y = 87)


    optionA = Button(root11, image= opt1, border=0, highlightthickness=0, command=opt1_func)
    optionA.place(x = 35, y = 250)

    optionB = Button(root11, image= opt2, border=0, highlightthickness=0, command=opt2_func)
    optionB.place(x = 35, y = 315)

    optionC = Button(root11, image= opt3, border=0, highlightthickness=0, command=opt3_func)
    optionC.place(x = 35, y = 380)

    optionD = Button(root11, image= opt4, border=0, highlightthickness=0, command=opt4_func)
    optionD.place(x = 35, y = 450)

    val = False
    skip_btn = Button(root11, text= "Skip",bg='green', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    setTimers = []
    initial_time = 300
    label = Label(root11, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 725, y = 25)
    countdown(initial_time)

    root11.mainloop()
#Audio1([10], [], [], [], [], 1, 6, ['Audio2'])