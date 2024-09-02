from tkinter import *
from tkinter import messagebox
from bride import *
from level4 import *
from Level2 import *
from level4 import *
from level5 import *
from level6 import *
from level7 import *
import random  
from final_process import *
def tick_joystick():
    global tick_img, correct
    correct += 1
    tick = Label(image= tick_img)
    tick.place(x = 650, y = 150)
    if chance == 0:
        final_check()

def barscannertick():
    global chance, correct
    chance -= 1
    correct += 1
    tick = Label(image= tick_img)
    tick.place(x = 250, y = 250)
    if chance == 0:
        final_check()

def keyboardtick():
    global tick_img, chance, correct
    chance -= 1
    correct += 1
    tick = Label(image= tick_img)
    tick.place(x = 390, y = 80)
    if chance == 0:
        final_check()

def mictick():
    global tick_img, chance, correct
    chance -= 1
    correct += 1
    tick = Label(image= tick_img)
    tick.place(x = 486, y = 218)
    if chance == 0:
        final_check()

def mousetick():
    global tick_img, chance, correct
    chance -= 1
    correct += 1
    tick = Label(image= tick_img)
    tick.place(x = 41, y = 350)
    if chance == 0:
        final_check()

# def wrong():
#     global wrg, chance, correct
#     correct -= 1
#     if correct < 0:
#         correct = 0
#     wrong_tick = Label(image= wrg)
#     wrong_tick.place(x = 650, y = 150)
#     if chance == 0:
#         final_check()

def headphoneswrong():
    global wrg, chance, correct
    chance -= 1
    # correct -= 1
    # if correct < 0:
    #     correct = 0
    wrong_tick = Label(image= wrg)
    wrong_tick.place(x =350,y = 500)
    if chance == 0:
        final_check()

def monitorwrong():
    global wrg, chance, correct
    chance -= 1
    wrong_tick = Label(image= wrg)
    wrong_tick.place(x =550,y = 418)
    # correct -= 1
    # if correct < 0:
    #     correct = 0
    if chance == 0:
        final_check()

def webcamwrong():
    global wrg, chance, correct
    chance -= 1
    # correct -= 1
    # if correct < 0:
    #     correct = 0
    wrong_tick = Label(image= wrg)
    wrong_tick.place(x =35,y = 66)
    if chance == 0:
        final_check()

def skipaway():
    global val
    val = messagebox.askokcancel("Skip", "Are you sure!")
    if val == True:
        final_check()

def countdown(time_left):
        global alu
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=time_format)
            cur = root2.after(1000, countdown, time_left - 1)
            setTimers.append(cur.split('#')[1])
            alu = cur.split('#')[1]
            
        else:
            messagebox.showwarning("Times Up","Times Oves, Go Next!")
            final_check()

def final_check():
    global Timer2, Title2, Skip2, Next2, CountScreen2, setTimers
    global id2, val, Marks2, correct, previous_time, call1, alu
    CountScreen2 += 1
    time = setTimers[-1]
    now = abs(int(time) - int(previous_time))
    print(f"now: {alu}, time: {time}, privious_time: {previous_time}")
    Skip2.append(val)
    Timer2.append(now)
    Marks2.append(correct)
    a = False
    if correct >= 3:
        a = True
    Next2.append(a)
    nextLevel = random.choices(call1)[0]
    call1.remove(nextLevel)
    if CountScreen2 == 5:
        root2.destroy()
        add_data(Timer2, Title2, Marks2, Skip2, Next2, CountScreen2, id2)
    root2.destroy()
    nextLevel(Timer2, Title2, Marks2, Skip2, Next2, CountScreen2, id2, call1)

def third_level(Timer1, Title1, Marks1, Skip1, Next1, CountScreen1, id, next_game_call):
    global root2, avail, chance, label, setTimers, correct, tick_img, wrg, val, previous_time
    global Timer2, Title2, Skip2, Next2, CountScreen2, Marks2, id2, call1
    Marks2 = Marks1
    Timer2 = Timer1
    Title2 = Title1
    Skip2 = Skip1
    Next2 = Next1
    id2 = id
    call1 = next_game_call
    CountScreen2 = CountScreen1
    previous_time = Timer1[-1]
    Title2.append('Level3')
    #call1.remove('third_level')
    root2 = Tk()
    try:
        root2.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root2.geometry("850x657+30+15")
    root2.title("level3")
    ti = 0
    for t in Timer2:
        ti += int(t)
    previous_time = ti
    correct = 0
    avail = set()

    tick_img = PhotoImage(file="tick.png")
    wrg = PhotoImage(file = "wrong.png")
    main_bg = PhotoImage(file="images/level3images/level3.png")
    barscanner_img = PhotoImage(file="images/level3images/barscanner.png")
    headphones_img = PhotoImage(file="images/level3images/headphones.png")
    joystick_img = PhotoImage(file="images/level3images/joystick.png")
    keyboard_img = PhotoImage(file="images/level3images/keyboard.png")
    mic_img = PhotoImage(file="images/level3images/mic.png")
    monitor_img = PhotoImage(file="images/level3images/monitor.png")
    mouse_img = PhotoImage(file="images/level3images/mouse.png")
    webcam_img = PhotoImage(file="images/level3images/webcam.png")

    back = Label(root2, image=main_bg)
    back.pack()

    joystick_btn = Button(root2, image=joystick_img, borderwidth=0, command = tick_joystick, highlightthickness=0)
    joystick_btn.place(x=650, y=80)

    headphones_btn = Button(root2, image=headphones_img, command=headphoneswrong, borderwidth=0, highlightthickness=0)
    headphones_btn.place(x=300, y=450)

    barscanner_btn = Button(root2, image=barscanner_img, command=barscannertick, borderwidth=0, highlightthickness=0)
    barscanner_btn.place(x=250, y=250)

    heading = Label(root2, text = "Chances: ", font = ("Time New Roman", 18))
    heading.place(x = 680,y = 30)

    chances  = Label(root2, text = "5", font = ("Time New Roman", 18)).place(x = 790, y = 30)
    chance = 4
    keyboard_btn = Button(root2, image=keyboard_img, command=keyboardtick, borderwidth=0, highlightthickness=0)
    keyboard_btn.place(x=250, y=85)

    mic_btn = Button(root2, image=mic_img, command=mictick, borderwidth=0, highlightthickness=0)
    mic_btn.place(x=486, y=218)

    monitor_btn = Button(root2, image=monitor_img, command=monitorwrong, borderwidth=0, highlightthickness=0)
    monitor_btn.place(x=550, y=418)

    mouse_btn = Button(root2, image=mouse_img, command=mousetick, borderwidth=0, highlightthickness=0)
    mouse_btn.place(x=41, y=350)

    webcam_btn = Button(root2, image=webcam_img, command=webcamwrong, borderwidth=0, highlightthickness=0)
    webcam_btn.place(x=35, y=66)

    val = False
    skip = Button(root2, text = "Skip", command=skipaway, height=1, width=8, bg="green", font=('Helvetica', 13))
    skip.place(x = 750, y = 370)

    #timer
    setTimers = []
    # 5min = 300, 10 min = 600
    initial_time = 300 
    label = Label(root2, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 30, y = 12)

    countdown(initial_time)
    root2.mainloop()

#third_level([], [], [], [], [], 0, 6)
