import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("SELECT course, COUNT(*) FROM students GROUP BY course")
rows=c.fetchall()

for row in rows:
    print(row)
con.close()