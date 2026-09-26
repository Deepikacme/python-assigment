import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT COUNT(*) FROM students")
count=c.fetchone()[0]
print("Total students:",count)
con.close()