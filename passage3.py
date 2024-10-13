from tkinter import * 
from tkinter import messagebox
import random
from final_process import add_data
def countdown(time_left):
    global label, alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = rootp.after(1000, countdown, time_left - 1)
        alu = cur.split('#')[1]
        print(alu)
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")

def skipnow():
    global val, correct_opt
    correct_opt = 0
    val=messagebox.askokcancel("Skip","Are you sure!")
    if val == True:
        finale()

def opt1_func():
    global correct_opt
    correct_opt=1
    next_button = Button(rootp, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)

def opt2_func():
    global correct_opt
    correct_opt=0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
    
def opt3_func():
    global correct_opt
    correct_opt=0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
   
def opt4_func():
    global correct_opt
    correct_opt=0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
    
def finale():
    now=abs(int(alu)-int(ti))
    P3Time.append(now)
    P3Marks.append(correct_opt)
    if correct_opt == 1:
        P3Next.append(True)
    else:
        P3Next.append(False)
    P3Skip.append(val)
    if P3CountScreen == 5:
        rootp.destroy()
        add_data(P3Time, P3Title, P3Marks, P3Skip, P3Next, P3CountScreen, P3a)
    nextLevel = random.choices(P3next_game_call)[0]
    P3next_game_call.remove(nextLevel)
    
    #print("Marks: ", correct_opt,"Time", now)
    #print(f"Time: {P3Time}, Title: {P3Title}, Marks: {P3Marks}, SKip: {P3Skip}, Next: {P3Next}, Screen_Count: {P3CountScreen}, Last : {P3a}, Fun: {P3next_game_call}")
    rootp.destroy()
    nextLevel(P3Time, P3Title, P3Marks, P3Skip, P3Next, P3CountScreen, P3a, P3next_game_call)

def passage3(Time,Title,Marks,Skip,Next,CountScreen,a,next_game_call):
    global rootp, label,P3Next,P3Time,P3Title,P3a,P3CountScreen,P3Marks,P3next_game_call,P3Skip
    global ti, val
    P3Time=Time
    P3Title= Title
    P3Marks=Marks
    P3Skip=Skip
    P3Next=Next
    P3CountScreen=CountScreen
    P3a=a
    P3next_game_call=next_game_call

    P3CountScreen+=1
    P3Title.append('Passage3')
    
    ti=0
    for t in P3Time:
        ti += int(t)

    rootp = Tk()
    try:
        rootp.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    rootp.geometry("850x670+30+15")
    rootp.title("Level 1")

    opt1 = PhotoImage(file="Passage3/opt1.png")
    opt2 = PhotoImage(file="Passage3/opt2.png")
    opt3 = PhotoImage(file="Passage3/opt3.png")
    opt4 = PhotoImage(file="Passage3/opt4.png")

    back_img = PhotoImage(file = "Passage3/Passage3img.png")
    back_label = Label(rootp, image= back_img)
    back_label.pack()

    btn_op1 = Button(rootp, image=opt1, borderwidth=0, highlightthickness=0, command= opt1_func)
    btn_op1.place(x = 35, y = 380)

    btn_op2 = Button(rootp, image=opt2, borderwidth=0, highlightthickness=0, command= opt2_func)
    btn_op2.place(x = 475, y = 376)

    btn_op3 = Button(rootp, image=opt3, borderwidth=0, highlightthickness=0, command= opt3_func)
    btn_op3.place(x = 35, y = 460)

    btn_op4 = Button(rootp, image=opt4, borderwidth=0, highlightthickness=0, command= opt4_func)
    btn_op4.place(x = 480, y = 460)

    val = False
    skip_btn = Button(rootp, text= "Skip",bg='red', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    setTimers = []
    initial_time = 300
    label = Label(rootp, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 730, y = 25)
    countdown(initial_time)
    rootp.mainloop()
#passage3([10], [], [], [], [], 1, 6, ['Hi'])