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
c.execute("INSERT OR IGNORE INTO students VALUES (1,'Deepika',20,'Python',85)")
c.execute("INSERT OR IGNORE INTO students VALUES (2,'Priya',19,'Java',90)")
c.execute("INSERT OR IGNORE INTO students VALUES (3,'Anjali',20,'Python',78)")
c.execute("INSERT OR IGNORE INTO students VALUES (4,'Sravani',19,'C',88)")
c.execute("INSERT OR IGNORE INTO students VALUES (5,'Divya',20,'Python',92)")
con.commit()
c.execute("SELECT*FROM students WHERE course='Python'")
students=c.fetchall()

for student in students:
    print(student)
con.close()