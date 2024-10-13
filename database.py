import mysql.connector

con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01")
cursor = con.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS personalize")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
cursor.close()
con.close()
print("---------Database created successfully!------------")


con1 = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "personalize")
cursor1 = con1.cursor()

cursor1.execute("CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT,name VARCHAR(100), gender ENUM('Male', 'Female', 'Other'),opinion TEXT, birth_year YEAR, tenPercent INT,12Percent INT,graduatePercent INT,masterpercent INT,PRIMARY KEY (user_id))")
cursor1.execute("CREATE TABLE marks (user_id INT,screen1 INT,screen2 INT,screen3 INT,screen4 INT,screen5 INT,total INT,FOREIGN KEY (user_id) REFERENCES users(user_id))")
cursor1.execute("CREATE TABLE time (user_id INT,screen1 INT,screen2 INT,screen3 INT,screen4 INT,screen5 INT,FOREIGN KEY (user_id) REFERENCES users(user_id))")
cursor1.execute("CREATE TABLE title (user_id INT,screen1 varchar(25),screen2 varchar(25),screen3 varchar(25),screen4 varchar(25),screen5 varchar(25),FOREIGN KEY (user_id) REFERENCES users(user_id))")
cursor1.execute("CREATE TABLE attention_calculator (user_id int, skip_count varchar(100), next_count varchar(100), skip_score int, next_score int, Foreign key(user_id) REFERENCES users(user_id))")

for tb in cursor1:
    print(tb)
    
con1.commit()
cursor1.close()
con1.close()

print("----------All the table Executed successfully!------------")