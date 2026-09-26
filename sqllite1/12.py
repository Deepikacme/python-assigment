import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT*FROM students ORDER BY marks DESC")
rows=c.fetchall()

for row in rows:
    print(row)
con.close()