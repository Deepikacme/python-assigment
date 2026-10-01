import sqlite3

con=sqlite3.connect('college database.db')
c=con.cursor()

c.execute("""
CREATE TABLE  IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT ,
age INTEGER,
course TEXT,
marksINTEGER
) 
""")
con .commit()
con.close()
print(" student table created successfully")
