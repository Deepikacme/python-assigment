import sqlite3

con=sqlite3.connect ("student.db")
cur=con.cursor("""
CREATE TABLE IF NOT EXISTS student
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL))
""")
cur.execute("INSERT INTO student(name)VALUES('John Doe')")
con.commit()
con.close()
