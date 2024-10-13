from playsound import playsound
from tkinter import *
from tkinter import messagebox
import random
from final_process import add_data
def audio():
    playsound("Passages/audio/Audio`s/Audio/1723494913689u6045fu-voicemaker.in-speech.mp3")
    play_count += 1

def countdown(time_left):
    global label, alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = root9.after(1000, countdown, time_left - 1)
        alu = cur.split('#')[1]
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
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)

def opt2_func():
    global correct_opt
    correct_opt=1
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def opt3_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
   
def opt4_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=620, y=500)
    
def finale():
    now=abs(int(alu)-int(ti))
    A2Time.append(now)
    A2Marks.append(correct_opt)
    # countS += 1
    if correct_opt == 1:
        A2Next.append(True)
    else:
        A2Next.append(False)
    A2Skip.append(val)
    print(A2next_game_call)
    if A2CountScreen == 5:
        root9.destroy()
        add_data(A2Time, A2Title, A2Marks,A2Skip, A2Next, A2CountScreen,A2a)
    nextLevel = random.choices(A2next_game_call)[0]
    A2next_game_call.remove(nextLevel)
    root9.destroy()
    nextLevel(A2Time, A2Title, A2Marks,A2Skip, A2Next, A2CountScreen,A2a, A2next_game_call)
    #print("Marks: ", correct_opt,"Time", now)
    #print(f"Time: {P3Time}, Title: {P3Title}, Marks: {P3Marks}, SKip: {P3Skip}, Next: {P3Next}, Screen_Count: {P3CountScreen}, Last : {P3a}, Fun: {P3next_game_call}")
    


def Audio2(Time,Title,Marks,Skip,Next,CountScreen,a,next_game_call):
    global root9, label, A2Next,A2Time,A2Title,A2a,A2CountScreen,A2Marks,A2next_game_call,A2Skip
    global ti, play_count, val
    A2Time=Time
    A2Title= Title
    A2Marks=Marks
    A2Skip=Skip
    A2Next=Next
    A2CountScreen=CountScreen
    A2a=a
    A2next_game_call=next_game_call

    A2CountScreen+=1
    A2Title.append('Audio2')
    
    ti=0
    for t in A2Time:
        ti += int(t)
    play_count = 0
    root9 = Tk()
    root9.geometry("800x632")

    opt1 = PhotoImage(file="audio/Auido2/opt1.png")
    opt2 = PhotoImage(file="audio/Auido2/opt2.png")
    opt3 = PhotoImage(file="audio/Auido2/opt3.png")
    opt4 = PhotoImage(file="audio/Auido2/opt4.png")

    play_sound=PhotoImage(file="audio/Auido2/play.png")

    back_img = PhotoImage(file = "audio/Auido2/Audio2img.png")
    back_label = Label(root9, image= back_img)
    back_label.pack()

    play = Button(root9, command=audio, border=0,image=play_sound,highlightthickness=0)
    play.place(x = 70, y = 62)


    optionA = Button(root9, image= opt1, border=0, highlightthickness=0, command=opt1_func)
    optionA.place(x = 50, y = 250)

    optionB = Button(root9, image= opt2, border=0, highlightthickness=0, command=opt2_func)
    optionB.place(x = 50, y = 315)

    optionC = Button(root9, image= opt3, border=0, highlightthickness=0, command=opt3_func)
    optionC.place(x = 50, y = 380)

    optionD = Button(root9, image= opt4, border=0, highlightthickness=0, command=opt4_func)
    optionD.place(x = 50, y = 445)

    val = False
    skip_btn = Button(root9, text= "Skip",bg='green', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    initial_time = 300
    label = Label(root9, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 725, y = 25)
    countdown(initial_time)

    root9.mainloop()
#Audio2([1], [], [], [], [], 0, 6, [])