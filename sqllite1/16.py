import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT MAX(marks), MIN(marks) FROM students")
highest, lowest=c.fetchone()
print("Highest marks:",highest)
print("Lowest marks:",lowest)
con.close()