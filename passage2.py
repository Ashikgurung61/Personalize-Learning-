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
    next_button.place(x=640, y=585)

def opt2_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
    
def opt3_func():
    global correct_opt
    correct_opt=1
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
   
def opt4_func():
    global correct_opt
    correct_opt=0
    next_button = Button(root9, text="Next", bg='green', height=2, width=9,command=finale)
    next_button.place(x=640, y=585)
    
def finale():
    now=abs(int(alu)-int(ti))
    P2Time.append(now)
    P2Marks.append(correct_opt)
    # countS += 1
    if correct_opt == 1:
        P2Next.append(True)
    else:
        P2Next.append(False)
    P2Skip.append(val)
    
    if P2CountScreen == 5:
        root9.destroy()
        add_data(P2Time, P2Title, P2Marks, P2Skip, P2Next, P2CountScreen, P2a)

    nextLevel = random.choices(P2next_game_call)[0]
    P2next_game_call.remove(nextLevel)
    #print("Marks: ", correct_opt,"Time", now)
    #print(f"Time: {P2Time}, Title: {P2Title}, Marks: {P2Marks}, SKip: {P2Skip}, Next: {P2Next}, Screen_Count: {P2CountScreen}, Last : {P2a}, Fun: {P2next_game_call}")
    root9.destroy()
    nextLevel(P2Time, P2Title, P2Marks, P2Skip, P2Next, P2CountScreen, P2a, P2next_game_call)


def passage2(Time,Title,Marks,Skip,Next,CountScreen,a,next_game_call):
    global root9, label, setTimers,P2Next,P2Time,P2Title,P2a,P2CountScreen,P2Marks,P2next_game_call,P2Skip
    global ti, P2next_game_call, val, alu
    P2Time=Time
    P2Title= Title
    P2Marks=Marks
    P2Skip=Skip
    P2Next=Next
    P2CountScreen=CountScreen
    P2a=a
    P2next_game_call=next_game_call
    alu = 0
    P2CountScreen+=1
    P2Title.append('Passage2')
    
    ti=0
    for t in P2Time:
        ti += int(t)

    root9 = Tk()
    try:
        root9.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root9.geometry("850x670+30+15")
    root9.title("Level 1")

    opt1 = PhotoImage(file="Passage2/opt1.png")
    opt2 = PhotoImage(file="Passage2/opt2.png")
    opt3 = PhotoImage(file="Passage2/opt3.png")
    opt4 = PhotoImage(file="Passage2/opt4.png")

    back_img = PhotoImage(file = "Passage2/Passage2img.png")
    back_label = Label(root9, image= back_img)
    back_label.pack()

    btn_op1 = Button(root9, image=opt1, borderwidth=0, highlightthickness=0 , command= opt1_func)
    btn_op1.place(x = 33, y = 425)

    btn_op2 = Button(root9, image=opt2, borderwidth=0, highlightthickness=0, command= opt2_func)
    btn_op2.place(x = 455, y = 422)

    btn_op3 = Button(root9, image=opt3, borderwidth=0, highlightthickness=0, command= opt3_func)
    btn_op3.place(x = 30, y = 505)

    btn_op4 = Button(root9, image=opt4, borderwidth=0, highlightthickness=0, command= opt4_func)
    btn_op4.place(x = 455, y = 505)

    val = False
    skip_btn = Button(root9, text= "Skip",bg='green', height=1, width=7, command= skipnow)
    skip_btn.place(x = 70, y=590)

    setTimers = []
    initial_time = 300
    label = Label(root9, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 730, y = 25)
    countdown(initial_time)
    root9.mainloop()
#passage2([10], [], [], [], [], 1, 6, ['Hi'])