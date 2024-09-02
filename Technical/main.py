from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Level_1 import level1

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "personalize")
cursor = con.cursor()

mroot = Tk()
mroot.title("Personalize Learnin")

try:
    mroot.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

#Configuration of BackGround and inserting images
mroot.geometry("800x620+30+15")
main_bg = PhotoImage(file= "Images/main.png")
label_back = Label(mroot, image=main_bg)
label_back.place(x=0, y=0)

#Collection of Images
submit_img = PhotoImage(file = "Images/submit.png")

name = Entry(mroot, bd = 0, width = 14, font=("Helvetica", 22), background="white")
name.place(x = 80, y = 75)

course = ttk.Combobox(mroot,values = ["BCA","MCA","B.Tech","M.Tech"],width = 12,font=("Helvetica", 22), background="white")
course.place(x = 385, y = 75)

year = Entry(mroot, bd = 0, width = 14, font=("Helvetica", 22), background="white")
year.place(x = 82, y = 279)

gender = ttk.Combobox(mroot,values = ["Male","Female"],width = 12,font=("Helvetica", 22), background="white")
gender.place(x = 80, y = 177)

opinion = ttk.Combobox(mroot,values = ["By Force","Influence","My Opinion"],width = 12,font=("Helvetica", 22), background="white")
opinion.place(x = 385, y = 177)

ten = Entry(mroot, bd = 0, width = 14, font=("Helvetica", 22), background="white")
ten.place(x = 385, y = 279)

twelve = Entry(mroot, bd = 0, width = 14, font=("Helvetica", 22), background="white")
twelve.place(x = 82, y = 381)

ug = Entry(mroot, bd = 0, width = 14, font=("Helvetica", 22), background="white")
ug.place(x = 385, y = 381)

def login():
    n = name.get()
    c = gender.get()
    o = opinion.get()
    y = year.get()
    t = ten.get()
    tw = twelve.get()
    ugs = ug.get()

    val1 = (n, c, o, y, t, tw, ugs)
    try:
        if (o == "") or (y == "") or (c == ""):
            messagebox.showerror("Empty","Please Enter Details")
        else:
            cursor.execute("INSERT INTO users (name, gender, opinion, birth_year, tenPercent, 12Percent, graduatePercent) VALUES (%s, %s, %s, %s, %s, %s, %s)", val1)
            con.commit()
            last_id = cursor.lastrowid
            messagebox.showinfo("Success", "Let's Try Some Test")
            mroot.destroy()
            level1(last_id)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "Please Insert the correct Value")
    finally:
        con.commit()


submit = Button(mroot, image=submit_img, command=login,  borderwidth=0, highlightthickness=0)
submit.place(x = 283, y = 455)

mroot.mainloop()