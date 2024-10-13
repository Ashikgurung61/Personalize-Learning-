from playsound import playsound
from tkinter import *
from tkinter import messagebox
import random
from final_process import add_data

def audio():
    playsound("Passages/audio/Audio`s/Audio/1723494580425854rq4cm-voicemaker.in-speech.mp3")
    play_count += 1

def countdown(time_left):
    global label, alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = root13.after(1000, countdown, time_left - 1)
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
    correct_opt=0
    next_button = Button(root13, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)

def opt2_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root13, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def opt3_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root13, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
   
def opt4_func():
    global correct_opt
    correct_opt=1
    next_button = Button(root13, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def finale():
    now=abs(int(alu)-int(ti))
    A3Time.append(now)
    A3Marks.append(correct_opt)
    # countS += 1
    if correct_opt == 1:
        A3Next.append(True)
    else:
        A3Next.append(False)
    A3Skip.append(val)
    print(A3next_game_call)
    if A3CountScreen == 5:
        root13.destroy()
        add_data(A3Time, A3Title, A3Marks,A3Skip, A3Next, A3CountScreen,A3a)
    nextLevel = random.choices(A3next_game_call)[0]
    A3next_game_call.remove(nextLevel)
    root13.destroy()
    nextLevel(A3Time, A3Title, A3Marks,A3Skip, A3Next, A3CountScreen,A3a, A3next_game_call)
    #print("Marks: ", correct_opt,"Time", now)
    #print(f"Time: {P3Time}, Title: {P3Title}, Marks: {P3Marks}, SKip: {P3Skip}, Next: {P3Next}, Screen_Count: {P3CountScreen}, Last : {P3a}, Fun: {P3next_game_call}")
    

def Audio3(Time,Title,Marks,Skip,Next,CountScreen,a,next_game_call):
    global root13, label, setTimers,A3Next,A3Time,A3Title,A3a,A3CountScreen,A3Marks,A3next_game_call,A3Skip
    global ti, play_count, val
    A3Time=Time
    A3Title= Title
    A3Marks=Marks
    A3Skip=Skip
    A3Next=Next
    A3CountScreen=CountScreen
    A3a=a
    A3next_game_call=next_game_call

    A3CountScreen+=1
    A3Title.append('Audio3')
    
    ti = 0
    for t in A3Time:
        ti += int(t)

    play_count = 0
    root13 = Tk()
    root13.geometry("800x632")

    opt1 = PhotoImage(file="audio/Audio3/opt1.png")
    opt2 = PhotoImage(file="audio/Audio3/opt2.png")
    opt3 = PhotoImage(file="audio/Audio3/opt3.png")
    opt4 = PhotoImage(file="audio/Audio3/opt4.png")

    play_sound=PhotoImage(file="audio/Audio3/play.png")

    back_img = PhotoImage(file = "audio/Audio3/Audio3img.png")
    back_label = Label(root13, image= back_img)
    back_label.pack()

    play = Button(root13, command=audio, border=0,image=play_sound,highlightthickness=0)
    play.place(x = 75, y = 62)


    optionA = Button(root13, image= opt1, border=0, highlightthickness=0, command=opt1_func)
    optionA.place(x = 58, y = 250)

    optionB = Button(root13, image= opt2, border=0, highlightthickness=0, command=opt2_func)
    optionB.place(x = 58, y = 310)

    optionC = Button(root13, image= opt3, border=0, highlightthickness=0, command=opt3_func)
    optionC.place(x = 60, y = 365)

    optionD = Button(root13, image= opt4, border=0, highlightthickness=0, command=opt4_func)
    optionD.place(x = 60, y = 430)

    val = False
    skip_btn = Button(root13, text= "Skip",bg='green', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    setTimers = []
    initial_time = 300
    label = Label(root13, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 725, y = 25)
    countdown(initial_time)
    root13.mainloop()