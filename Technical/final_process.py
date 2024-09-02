import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "personalize")
cursor = con.cursor()

time_Query = "insert into time(user_id, screen1, screen2, screen3, screen4, screen5) values (%s, %s, %s, %s, %s, %s)"
title_Query = "insert into title(user_id, screen1, screen2, screen3, screen4, screen5) values (%s, %s, %s, %s, %s, %s)"
mark_Query = "insert into marks(user_id, screen1, screen2, screen3, screen4, screen5, total) values (%s, %s, %s, %s, %s, %s, %s)"
calculator = "insert into attention_calculator(user_id, skip_count, next_count, skip_score, next_score) values (%s, %s, %s, %s, %s)"

def add_data(time, title, mark, skip, next, countScreen, id):
    count_skip = 0
    for i in skip:
        if i == True:
            count_skip += 1
    
    count_next = 0
    for j in next:
        if j == True:
            count_next += 1
    
    skip_count = ""
    for i in skip:
        skip_count += str(i) + ","
    next_count = ""
    for j in next:
        next_count += str(j) + ","
    total_mark = 0
    for i in mark:
        total_mark += i

    time_value = (id, time[0], time[1], time[2], time[3], time[4])
    title_value = (id, title[0], title[1], title[2], title[3], title[4])
    mark_value = (id, mark[0], mark[1], mark[2], mark[3], mark[4], total_mark)
    skip_value = (id,skip_count, next_count, count_skip, count_next)
    try:
        cursor.execute(time_Query, time_value)
        cursor.execute(title_Query, title_value)
        cursor.execute(mark_Query, mark_value)
        cursor.execute(calculator, skip_value)
        messagebox.showinfo("Success","Data Saved")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "Please Insert the correct Value")
    finally:
        con.commit()
#add_data([8, 3,5,6,7], ['1','2','3','4','5'], [ 3, 4, 2, 1, 0], [True, False, True, False, True],[True, False, True, False, True],5, 28)

