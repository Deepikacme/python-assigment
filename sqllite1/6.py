import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT * FROM students WHERE marks > 75")
students=c.fetchall()

for student in students:
    print(student)