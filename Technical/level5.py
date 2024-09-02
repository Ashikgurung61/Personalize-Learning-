from tkinter import *
from tkinter import messagebox
from bride import *
from level6 import* 
import random
from final_process import *
from Level2 import *
from level3 import *
from level4 import *
from level6 import *
from level7 import *
from final_process import *

#skip 
def skipaway():
    global response
    response = messagebox.askokcancel("Skip", "Are you sure!")
    if response == True:
        final_check()

#answer feedback box
def option1():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option2():
    global correct
    messagebox.showinfo("Information", "Right")
    correct += 1
    final_check()

def option3():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def option4():
    messagebox.showwarning("Information", "Wrong")
    final_check()

def countdown(time_left):
    global alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = root4.after(1000, countdown, time_left - 1)
        setTimers.append(cur.split('#')[1])
        alu = cur.split('#')[1]
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")
        final_check()

def final_check():
    global Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4, response, correct, previous_time, call1, alu
    CountScreen4 += 1
    time = setTimers[-1]
    Skip4.append(response)
    now = abs(int(alu) - int(previous_time))
    print(f"now: {now}, time: {time}, privious_time: {previous_time}")
    Timer4.append(now)
    Marks4.append(correct)
    a = False
    if correct == 1:
        a = True
    Next4.append(a)

    # if CountScreen4 >= 5:
    #     root4.destroy()
    #     add_data(Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4)

    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    if CountScreen4 == 5:
        root4.destroy()
        add_data(Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4)
    root4.destroy()
    nextLevel(Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4, call1)
    

def fifth_level(Timer3, Title3, Marks3, Skip3, Next3, CountScreen3, id3, next_game_call):
    global root4, avail, setTimers, label, response, correct, previous_time
    global Timer4, Title4, Marks4, Skip4, Next4, CountScreen4, id4, call1

    Timer4 = Timer3
    Title4 = Title3
    Marks4 = Marks3
    Skip4 = Skip3
    Next4 = Next3
    CountScreen4 = CountScreen3
    id4 = id3
    Title4.append("Level5")
    previous_time = Timer3[-1]
    call1 = next_game_call
    #call1.remove('fifth_level')
    root4 = Tk()
    correct = 0
    ti = 0
    for t in Timer4:
        ti += int(t)
    previous_time = ti
    try:
        root4.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root4.geometry("850x657+30+15")
    root4.title("level5")
    # tick_img = PhotoImage(file="tick.png")
    # wrg = PhotoImage(file = "wrong.png")
    main_bg = PhotoImage(file="images/level5images/stack(level5).png")
    option1tick_img = PhotoImage(file="images/level5images/option1.png")
    option2tick_img = PhotoImage(file="images/level5images/option2.png")
    option3tick_img = PhotoImage(file="images/level5images/option3.png")
    option4tick_img = PhotoImage(file="images/level5images/option4.png")

#create message box for answer is correct or wrong
    back = Label(root4, image=main_bg)
    back.pack()

    option1tick_btn = Button(root4, image=option1tick_img,command=option1, borderwidth=0,highlightthickness=0)
    option1tick_btn.place(x=115, y=580)

    option2tick_btn = Button(root4, image=option2tick_img,command=option2, borderwidth=0, highlightthickness=0)
    option2tick_btn.place(x=295, y=580)

    option3tick_btn = Button(root4, image=option3tick_img,command=option3, borderwidth=0, highlightthickness=0)
    option3tick_btn.place(x=475, y=580)

    option4tick_btn = Button(root4, image=option4tick_img,command=option4, borderwidth=0, highlightthickness=0)
    option4tick_btn.place(x=670, y=580)

    response = False
    skip = Button(root4, text = "Skip", command=skipaway , height=1, width=8, bg="green", font=('Helvetica', 13))
    skip.place(x = 750, y = 100)

    #timer
    setTimers = []

     # 5min = 300, 10 min = 600
    initial_time = 150
    label = Label(root4, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 756, y = 12)
    countdown(initial_time)

    root4.mainloop()

#fifth_level([1], [], [], [], [], 0, 6, [sixth_level, seventh_level])