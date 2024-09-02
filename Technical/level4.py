from tkinter import *
from tkinter import messagebox
from level5 import*
from bride import bridge
import random 
from Level2 import *
from level3 import *
from level5 import *
from level6 import *
from level7 import *
from final_process import *
def skipaway():
    global response
    response = messagebox.askokcancel("Skip", "Are you sure!")
    if response == True:
        final_check()

def option1():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option2():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option3():
    global correct
    messagebox.showwarning("Information", "Right")
    correct += 1
    final_check()

def countdown(time_left):
    global alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = root3.after(1000, countdown, time_left - 1)
        setTimers.append(cur.split('#')[1])
        alu = cur.split('#')[1]
        print("Level4: ", cur)
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")
        final_check()

def final_check():
    global Timer3, Title3, Marks3, Skip3, Next3, CountScreen3, id3, response, correct, previous_time, alu
    CountScreen3 += 1
    time = setTimers[-1]
    Skip3.append(response)
    now = abs(int(alu) - int(previous_time))
    print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    Timer3.append(now)
    Marks3.append(correct)
    a = False
    if correct == 1:
        a = True
    Next3.append(a)
    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    if CountScreen3 == 5:
        root3.destroy()
        add_data(Timer3, Title3, Marks3, Skip3, Next3, CountScreen3, id3)
    root3.destroy()
    nextLevel(Timer3, Title3, Marks3, Skip3, Next3, CountScreen3, id3, call1)

def fourth_level(Timer2, Title2, Marks2, Skip2, Next2, CountScreen2, id2, next_game_call):
    global root3, label, setTimers, response, correct, previous_time
    global Timer3, Title3, Marks3, Skip3, Next3, CountScreen3, id3, call1
    Timer3 = Timer2
    Title3 = Title2
    Marks3 = Marks2
    Skip3 = Skip2
    Next3 = Next2
    CountScreen3 = CountScreen2
    id3 = id2
    previous_time = Timer2[-1]
    call1 = next_game_call
    
    root3 = Tk()
    ti = 0
    for t in Timer3:
        ti += int(t)
    previous_time = ti
    try:
        root3.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    Title3.append("Level4")
    root3.geometry("850x657+30+15")
    root3.title("level4")
    main_bg = PhotoImage(file="images/level4images/mirror(level 4).png")
    option1tick_img = PhotoImage(file="images/level4images/option1.png")
    option2tick_img = PhotoImage(file="images/level4images/option2.png")
    option3tick_img = PhotoImage(file="images/level4images/option3.png")

    correct = 0
#create message box for answer is correct or wrong
    back = Label(root3, image=main_bg)
    back.pack()

    option1tick_btn = Button(root3,command=option1, image=option1tick_img, borderwidth=0,highlightthickness=0)
    option1tick_btn.place(x=83, y=500)

    option2tick_btn = Button(root3, image=option2tick_img,command=option2, borderwidth=0, highlightthickness=0)
    option2tick_btn.place(x=345, y=500)

    option3tick_btn = Button(root3, image=option3tick_img,command=option3, borderwidth=0, highlightthickness=0)
    option3tick_btn.place(x=600, y=497)

    response = False
    skip = Button(root3, text = "Skip", command=skipaway , height=1, width=8, bg="green", font=('Helvetica', 13))
    skip.place(x = 750, y = 359)

    #timer
    setTimers = []
     # 5min = 300, 10 min = 600
    initial_time = 150
    label = Label(root3, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 756, y = 12)
    countdown(initial_time)

    root3.mainloop()

#fourth_level([], [], [], [], [], 0, 6)