from tkinter import *
from tkinter import messagebox
from level3 import *
import random
from level3 import *
from level4 import *
from level5 import *
from level6 import *
from level7 import *
from final_process import *
counts = 0
def rabbit_hide():
    global avail, counts 
    function_name = 'rabbit_hide'
    if function_name not in avail:
        tick = Label(root1, image = tick_img)
        tick.place(x = 640, y = 568)
        counts += 1
        avail.add(function_name)
    check_gameover()

def cup_hide():
    global counts, avail
    function_name = 'cup_hide'
    if function_name not in avail:
        tick = Label(root1, image = tick_img)
        tick.place(x = 160, y = 478)
        counts += 1
        avail.add(function_name)
    check_gameover()
    
def book_hide():
    global counts, avail
    function_name = 'book_hide'
    if function_name not in avail:
        tick = Label(root1, image = tick_img)
        tick.place(x = 145, y = 555)
        counts += 1
        avail.add(function_name)
    check_gameover()

def flag_hide():
    global counts, avail
    function_name = 'flag_hide'
    if function_name not in avail:
        tick = Label(root1, image = tick_img)
        tick.place(x = 640, y = 475)
        counts += 1
        avail.add(function_name)
    check_gameover()

def check_gameover():
    if counts >= 4:
        response = messagebox.showinfo("Game Over", "Next Level")
        if response == "ok":
            final()

def countdown(time_left):
        global label1, setTimers, alu
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label1.config(text=time_format)
            cur1 = root1.after(1000, countdown, time_left - 1)
            setTimers.append(cur1.split('#')[1])
            alu = cur1.split('#')[1]
            print("Level2: ", alu)
            
        else:
            messagebox.showwarning("Times Up","Times Oves, Go Next!")
            final()

def skipnow():
        global val
        val = messagebox.askokcancel("Skip", "Are you sure!")
        if val == True:
            final()

def final():
    global Timer1, Title1, Skip1, Next1, CountScreen1, setTimers
    global id, val, Marks1, counts, previous_time, call1, alu
    CountScreen1 += 1
    time = setTimers[-1]
    now = abs(int(alu) - int(previous_time))
    print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    Timer1.append(now)
    Skip1.append(val)
    Marks1.append(counts)
    a = False
    if counts >= 4:
        a = True

    Next1.append(a)
    if CountScreen1 == 5:
        root1.destroy()
        add_data(Timer1, Title1, Marks1, Skip1, Next1, CountScreen1, id)
    root1.destroy()
    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    nextLevel(Timer1, Title1, Marks1, Skip1, Next1, CountScreen1, id, call1)

def second_level(Timer, Title, Marks, Skip, Next, CountScreen, a, next_game_call):
    global root1, tick_img, avail, setTimers, id, label1, val, previous_time
    global Timer1, Title1, Skip1, Next1, CountScreen1, Marks1, call1
    call1 = next_game_call
    Marks1 = Marks
    Timer1 = Timer
    Title1 = Title
    Skip1 = Skip
    Next1 = Next
    CountScreen1 = CountScreen
    id = a 
    ti = 0
    for t in Timer1:
        ti += int(t)
    previous_time = ti
    Title.append('Level2')
    #call1.remove('second_level')
    root1 = Tk()
    try:
        root1.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root1.geometry("850x657+30+15")
    root1.title("Game")

    avail = set()

    tick_img = PhotoImage(file="tick.png")
    main_bg = PhotoImage(file="images/level2images/LevelTwo.png")
    rabbit_img = PhotoImage(file="images/level2images/rabbit.png")
    book_img = PhotoImage(file="images/level2images/book.png")
    flag_img = PhotoImage(file="images/level2images/flag.png")
    cup_img = PhotoImage(file="images/level2images/cup.png")

    back = Label(root1, image=main_bg)
    back.pack()

    rabbit_btn = Button(root1, image=rabbit_img, command=rabbit_hide, borderwidth=0, highlightthickness=0)
    rabbit_btn.place(x=633, y=356)

    book_btn = Button(root1, image=book_img, command=book_hide, borderwidth=0, highlightthickness=0)
    book_btn.place(x=122, y=334)

    flag_btn = Button(root1, image=flag_img, command=flag_hide, borderwidth=0, highlightthickness=0)
    flag_btn.place(x=240, y=64)

    cup_btn = Button(root1, image=cup_img, command=cup_hide, borderwidth=0, highlightthickness=0)
    cup_btn.place(x=560, y=318)

    setTimers = []
    #timer
    initial_time = 300
    label1 = Label(root1, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label1.place(x = 30, y = 462)
    countdown(initial_time)

    val = False        
    skip = Button(root1, text = "Skip", command=skipnow, height=1, width=8, bg="red", font=('Helvetica', 13))
    skip.place(x = 746, y = 462)

    root1.mainloop()

#second_level([10], [], [], [], [], 0, 6, ['Hi'])