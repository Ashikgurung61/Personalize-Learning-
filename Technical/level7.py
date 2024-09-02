from bride import *
from tkinter import *
from tkinter import messagebox
import random 
from Level2 import *
from level3 import *
from level4 import *
from level5 import *
from level6 import *
from final_process import *

#skip
def skipaway():
    global response
    reponse = messagebox.askokcancel("Skip", "Are you sure!")
    if reponse == True:
        response = True
        final_check()

#answer feedback box
def option1():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option2():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option3():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option4():
    messagebox.showwarning("Information", "Right")
    final_check()

def countdown(time_left):
        global alu
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=time_format)
            cur = root6.after(1000, countdown, time_left - 1)
            setTimers.append(cur.split('#')[1])
            alu = cur.split('#')[1]
        else:
            messagebox.showwarning("Times Up","Times Oves, Go Next!")
            final_check()

def final_check():
    global Timer6, Title6, Marks6, Skip6, Next6, CountScreen6, id6, alu, response, correct, previous_time, call1
    CountScreen6 += 1
    time = setTimers[-1]
    Skip6.append(response)
    now = abs(int(alu) - int(previous_time))
    print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    Timer6.append(now)
    Marks6.append(correct)
    a = False
    if correct >= 1:
        a = True
    Next6.append(a)
    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    if CountScreen6 == 5:
        root6.destroy()
        add_data(Timer6, Title6, Marks6, Skip6, Next6, CountScreen6, id6)

    root6.destroy()
    nextLevel(Timer6, Title6, Marks6, Skip6, Next6, CountScreen6, id6, call1)
    
def seventh_level(Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5, next_game_call):
    global root6,avail, setTimers, correct, response, previous_time, call1
    global Timer6, Title6, Marks6, Skip6, Next6, CountScreen6, id6, label
    Timer6 = Timer5
    Title6 = Title5
    Marks6 = Marks5
    Skip6 = Skip5
    Next6 = Next5
    CountScreen6 = CountScreen5
    id6 = id5 
    previous_time = Timer5[-1]
    #initialization
    correct = 0
    Title6.append("Level7")
    call1 = next_game_call
    #call1.remove('seventh_level')
    ti = 0
    for t in Timer6:
        ti += int(t)
    previous_time = ti
    root6 = Tk()
    try:
        root6.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root6.geometry("850x657+30+15")
    root6.title("level7")

    avail = set()
    main_bg = PhotoImage(file="images/level7images/sequence(level7).png")
    option1tick_img = PhotoImage(file="images/level7images/option1.png")
    option2tick_img = PhotoImage(file="images/level7images/option2.png")
    option3tick_img = PhotoImage(file="images/level7images/option3.png")
    option4tick_img = PhotoImage(file="images/level7images/option4.png")

#create message box for answer is correct or wrong
    back = Label(root6, image=main_bg)
    back.pack()

    option1tick_btn = Button(root6, image=option1tick_img,command=option1, borderwidth=0,highlightthickness=0)
    option1tick_btn.place(x=73, y=380)

    option2tick_btn = Button(root6, image=option2tick_img,command=option2, borderwidth=0, highlightthickness=0)
    option2tick_btn.place(x=250,y=380)

    option3tick_btn = Button(root6, image=option3tick_img,command=option3, borderwidth=0, highlightthickness=0)
    option3tick_btn.place(x=425, y=382)

    option4tick_btn = Button(root6, image=option4tick_img,command=option4, borderwidth=0, highlightthickness=0)
    option4tick_btn.place(x=610, y=372)

    response = False
    skip = Button(root6, text = "Skip", command=skipaway , height=1, width=8, bg="green", font=('Helvetica', 13))
    skip.place(x = 750, y = 210)

    setTimers = []
    initial_time = 300 # 5min = 300, 10 min = 600

    label = Label(root6, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 766, y = 12)
    countdown(initial_time)

    root6.mainloop()
#seventh_level([], [], [], [], [], 0, 6)