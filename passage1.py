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
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")
        
def skipnow():
        global val, correct_opt
        correct_opt = 0
        val = messagebox.askokcancel("Skip", "Are you sure!")
        if val == True:
            finale()

def opt1_funct():
    global correct_opt
    correct_opt = 0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=10, command= finale)
    next_button.place(x=640, y=585)
    
def opt2_funct():
    global correct_opt
    correct_opt = 1
    next_button = Button(rootp, text="Next", bg='green', height=2, width=10, command= finale)
    next_button.place(x=640, y=585)

def opt3_funct():
    global correct_opt
    correct_opt = 0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=10, command= finale)
    next_button.place(x=640, y=585)

def opt4_funct():
    global correct_opt
    correct_opt = 0
    next_button = Button(rootp, text="Next", bg='green', height=2, width=10, command= finale)
    next_button.place(x=640, y=585)

def finale():
    #global p1Marks, p1Next, p1Skip, p1Time, P1Title, a1
    p1Marks.append(correct_opt)
    # countS += 1
    if correct_opt == 1:
        p1Next.append(True)
    else:
        p1Next.append(False)
    now = abs(int(alu) - int(ti))
    #print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    p1Time.append(now)
    p1Skip.append(val)
    print(lvl)
    if countS == 5:
        rootp.destroy()
        add_data(p1Time, P1Title, p1Marks, p1Skip, p1Next, countS, a1)
        
    nextLevel = random.choices(lvl)[0]
    lvl.remove(nextLevel)
    rootp.destroy()
    nextLevel(p1Time, P1Title, p1Marks, p1Skip, p1Next, countS, a1, lvl)
    

def passage1(Timer, Title, Marks, Skip, Next, CountScreen, a, next_game_call):
    global rootp, label, p1Marks, p1Next, p1Skip, p1Time, P1Title, a1, correct_opt
    global p1Marks, val, ti, lvl, countS
    
    p1Time = Timer
    P1Title = Title
    p1Marks = Marks
    p1Skip = Skip
    p1Next = Next
    countS = CountScreen
    countS += 1
    a1 = a
    lvl = next_game_call
    P1Title.append('Passage1')
    # correct_opt = 0
    ti = 0
    for t in p1Time:
        ti += int(t)
    rootp = Tk()
    try:
        rootp.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    rootp.geometry("850x670+30+15")
    rootp.title("Level 1")


    opt1 = PhotoImage(file="Passage1/opt1.png")
    opt2 = PhotoImage(file="Passage1/opt2.png")
    opt3 = PhotoImage(file="Passage1/opt3.png")
    opt4 = PhotoImage(file="Passage1/opt4.png")

    back_img = PhotoImage(file = "Passage1/Passage1img.png")
    back_label = Label(rootp, image= back_img)
    back_label.pack()

    btn_op1 = Button(rootp, image=opt1, borderwidth=0, highlightthickness=0, command=opt1_funct)
    btn_op1.place(x = 36, y = 370)

    btn_op2 = Button(rootp, image=opt2, borderwidth=0, highlightthickness=0, command=opt2_funct)
    btn_op2.place(x = 448, y = 370)

    btn_op3 = Button(rootp, image=opt3, borderwidth=0, highlightthickness=0, command=opt3_funct)
    btn_op3.place(x = 35, y = 435)

    btn_op4 = Button(rootp, image=opt4, borderwidth=0, highlightthickness=0, command=opt4_funct)
    btn_op4.place(x = 447, y = 435)

    val = False
    skip_btn = Button(rootp, text= "Skip",bg='red', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    # next_button = Button(rootp, text="Next", bg='green', height=2, width=10, command= finale)
    # next_button.place(x=640, y=585)

    setTimers = []
    initial_time = 300
    label = Label(rootp, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 730, y = 25)
    countdown(initial_time)
    rootp.mainloop()

#passage1([10], [], [], [], [], 1, 6, ['Hi'])