from tkinter import *
from tkinter import messagebox
from bride import *
from level7 import*
import random 
from Level2 import *
from level3 import *
from level4 import *
from level5 import *
from level7 import *
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
    global correct, avail
    messagebox.showinfo("Information", "Right")
    correct += 1
    final_check()

def countdown(time_left):
        global alu
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=time_format)
            cur = root5.after(1000, countdown, time_left - 1)
            setTimers.append(cur.split('#')[1])
            alu = cur.split('#')[1]
        else:
            messagebox.showwarning("Times Up","Times Oves, Go Next!")
            final_check()

def final_check():
    global Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5, response, correct, previous_time, alu
    CountScreen5 += 1
    time = setTimers[-1]
    Skip5.append(response)
    now = abs(int(alu) - int(previous_time))
    print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    Timer5.append(now)
    Marks5.append(correct)
    a = False
    if correct >= 1:
        a = True
    Next5.append(a)
    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    if CountScreen5 == 5:
        root5.destroy()
        add_data(Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5)
    root5.destroy()
    #bridge(Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5)
    nextLevel(Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5, call1)

def sixth_level(Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4, next_game_call):
    global root5, avail, label, setTimers, response, correct
    global Timer5, Title5, Marks5, Skip5, Next5, CountScreen5, id5, previous_time, call1
    Timer5 = Timer4
    Title5 = Title4
    Marks5 = Marks4
    Skip5 = Skip4
    Next5 = Next4
    CountScreen5 = CountScreen4
    id5 = id4 
    correct = 0
    Title5.append('Level6')
    previous_time = Timer4[-1]
    call1 = next_game_call
    #call1.remove('sixth_level')
    ti = 0
    for t in Timer5:
        ti += int(t)
    previous_time = ti
    root5 = Tk()
    try:
        root5.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root5.geometry("850x657+30+15")
    root5.title("level6")

    avail = set()
    main_bg = PhotoImage(file="images/level6images/ring(level6).png")
    option1tick_img = PhotoImage(file="images/level6images/option1.png")
    option2tick_img = PhotoImage(file="images/level6images/option2.png")
    option3tick_img = PhotoImage(file="images/level6images/option3.png")
    option4tick_img = PhotoImage(file="images/level6images/option4.png")

    back = Label(root5, image=main_bg)
    back.pack()

    option1tick_btn = Button(root5, image=option1tick_img,command=option1, borderwidth=0,highlightthickness=0)
    option1tick_btn.place(x=120, y=545)

    option2tick_btn = Button(root5, image=option2tick_img,command=option2, borderwidth=0, highlightthickness=0)
    option2tick_btn.place(x=300,y=540)

    option3tick_btn = Button(root5, image=option3tick_img,command=option3, borderwidth=0, highlightthickness=0)
    option3tick_btn.place(x=475, y=540)

    option4tick_btn = Button(root5, image=option4tick_img,command=option4, borderwidth=0, highlightthickness=0)
    option4tick_btn.place(x=630, y=540)

    response = False
    skip = Button(root5, text = "Skip", command=skipaway , height=1, width=8, bg="green", font=('Helvetica', 13))
    skip.place(x = 750, y = 400)

    #timer
    setTimers = []
    initial_time = 300 # 5min = 300, 10 min = 600
    label = Label(root5, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 766, y = 12)
    countdown(initial_time)

    root5.mainloop()
#sixth_level([], [], [], [], [], 0, 6)