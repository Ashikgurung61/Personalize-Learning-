from tkinter import *
from tkinter import messagebox
from Level2 import *
from level3 import *
from level4 import *
from level5 import *
from level6 import *
from level7 import *
import random
from bride import bridge
import mysql.connector 

lst = [second_level, third_level, fourth_level, fifth_level, sixth_level, seventh_level]
con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "personalize")
cursor = con.cursor()

def dog_hide():
    global count, tick_placed_functions
    function_name = 'dog_hide'
    if function_name not in tick_placed_functions:
        tick = Label(roots, image=tick_img)
        tick.place(x=220, y=528)
        count += 1
        tick_placed_functions.add(function_name)
    check_game_over()

def cat_hide():
    global count, tick_placed_functions
    function_name = 'cat_hide'
    if function_name not in tick_placed_functions:
        tick = Label(roots, image=tick_img)
        tick.place(x=380, y=528)
        count += 1
        tick_placed_functions.add(function_name)
    check_game_over()

def win_hide():
    global count, tick_placed_functions
    function_name = 'win_hide'
    if function_name not in tick_placed_functions:
        tick = Label(roots, image=tick_img)
        tick.place(x=625, y=500)
        count += 1
        tick_placed_functions.add(function_name)
    check_game_over()

def boot_hide():
    global count, tick_placed_functions
    function_name = 'boot_hide'
    if function_name not in tick_placed_functions:
        tick = Label(roots, image=tick_img)
        tick.place(x=499, y=510)
        count += 1
        tick_placed_functions.add(function_name)
    check_game_over()

def check_game_over():
    if count >= 4:
        response = messagebox.showinfo("Game Over", "Continue")
        if response == "ok":
            add_data()

def countdown(time_left):
    global label, alu
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        cur = roots.after(1000, countdown, time_left - 1)
        alu = setTimers.append(cur.split('#')[1])
        print("Level1: ", cur)
    else:
        messagebox.showwarning("Times Up","Times Oves, Go Next!")
        add_data()

def skipnow():
        global val
        val = messagebox.askokcancel("Skip", "Are you sure!")
        if val == True:
            add_data()

def add_data():
    global setTimers, count, val, a, alu
    global Timer, Title, Marks, Skip, Next, CountScreen 
    CountScreen += 1
    time = setTimers[-1]
    Timer.append(time)
    Marks.append(count)
    Skip.append(val)
    nxt = False
    if count >= 4:
        nxt = True
    Next.append(nxt)
    roots.destroy()
    chance = [40, 40, 40, 40, 40, 40]
    nextLevel = random.choices(lst, weights=chance, k=1)[0]
    lst.remove(nextLevel)
    nextLevel(Timer, Title, Marks, Skip, Next, CountScreen, a, lst)

def level1(last):
    global roots, count, tick_placed_functions, tick_img, setTimers, val, label, a
    global Timer, Title, Marks, Skip, Next, CountScreen  #This is the most important variables.
    Timer = [] #This should store the times for each Screen or level
    Title = [] #This Store the Title whether level 1 or level 2 ... level15
    Marks = [] #Total number of correct
    Skip = [] #Total number of skip in each level
    Next = [] #Automatically taken to next level
    CountScreen = 0 #Screen Count Maximum 5
    a = last
    
    Title.append('Level1')
    roots = Tk()
    try:
        roots.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    count = 0
    roots.geometry("850x670+30+15")
    roots.title("Level 1")
    roots.configure(background="lightgray")

    tick_placed_functions = set()
    
    tick_img = PhotoImage(file="tick.png")
    image = PhotoImage(file="images/level1images/back.png")
    hides = PhotoImage(file='images/level1images/button.png')
    dog_img = PhotoImage(file='images/level1images/dog.png')
    win_img = PhotoImage(file = 'images/level1images/window.png')
    below = PhotoImage(file = "images/level1images/Water.png")
    boot = PhotoImage(file = "images/level1images/boot.png")

    label = Label(roots, image=image)
    label.place(x=28, y=10)

    cat_btn = Button(roots, width=55, height=70, image=hides, command=cat_hide, borderwidth=0, highlightthickness=0)
    cat_btn.place(x=333, y=397)

    dog_btn = Button(roots, image=dog_img, command=dog_hide, borderwidth=0, highlightthickness=0)
    dog_btn.place(x=600, y=197)

    win_btn = Button(roots, image=win_img, command=win_hide, borderwidth=0, highlightthickness=0)
    win_btn.place(x=641, y=105)

    boot_btn = Button(roots, image=boot, command=boot_hide, borderwidth=0, highlightthickness=0)
    boot_btn.place(x=765, y=365)

    label = Label(roots, image=below)
    label.place(x=28, y=460)
    
    setTimers = []
    #timer

    initial_time = 300
    label = Label(roots, text="00:00", font=('Helvetica', 20),foreground="White", background="Red", borderwidth=0)
    label.place(x = 30, y = 462)
    countdown(initial_time)

    val = False        
    skip = Button(roots, text = "Skip", command=skipnow, height=1, width=8, bg="red", font=('Helvetica', 13))
    skip.place(x = 746, y = 462)
    
    roots.mainloop()
level1(6)