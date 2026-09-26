import sqlite3

con=sqlite3.connect('college database.db')
c=con.cursor()

c.execute("INSERT INTO student values(1,'deepika',20,'python',90)")
c.execute("INSERT INTO student values(2,'deepa',21,'java',80)")
c.execute("INSERT INTO student values (3,'manasa',22'sql',70)")
c.exeute("INSERT INTO student values(4,'manuu',23,'c++',60)")
con.commit()
print("5 records inserted successfully")