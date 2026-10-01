import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT AVG(marks) FROM students")
average=c.fetchone()[0]
print("Average marks:",average)
con.close()