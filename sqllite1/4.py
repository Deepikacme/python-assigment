import sqlite3

con = sqlite3.connect("college.db")
c = con.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

c.execute("INSERT INTO students VALUES (1,'deepika',20,'CME',85)")
c.execute("INSERT INTO students VALUES (2,'manasa', 19,'CSE',90)")
c.execute("INSERT INTO students VALUES (3,'anjali', 20,'ECE',78)")
c.execute("INSERT INTO students VALUES (4,'sravani', 19,'CSE',88)")
c.execute("INSERT INTO students VALUES (5,'divya', 20,'CME',92)")

con.commit()

# Display all students
c.execute("SELECT * FROM students")

students=c.fetchall()

for student in students:
    print(student)

con.close()