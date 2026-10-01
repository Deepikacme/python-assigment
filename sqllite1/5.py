import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

c.execute("INSERT OR IGNORE INTO students VALUES (1, 'Deepika', 20, 'CME', 85)")
c.execute("INSERT OR IGNORE INTO students VALUES (2, 'Priya', 19, 'CSE', 90)")
c.execute("INSERT OR IGNORE INTO students VALUES (3, 'Anjali', 20, 'ECE', 78)")
c.execute("INSERT OR IGNORE INTO students VALUES (4, 'Sravani', 19, 'CSE', 88)")
c.execute("INSERT OR IGNORE INTO students VALUES (5, 'Divya', 20, 'CME', 92)")
con.commit()
c.execute("SELECT name FROM students")
students=c.fetchall()

for student in students:
    print(student[0])
con.close()
