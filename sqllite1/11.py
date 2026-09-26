import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
students=[
    (6,"deepu",20,"Python",85),
    (7,"mani",19,"Java",78),
    (8,"lalli",20,"Python",92),
    (9,"manasa",21,"Java",74),
    (10,"sita",19,"Python",88),
    (11,"Ravi",20,"C", 81),
    (12,"Meena",21,"Python",95),
    (13,"Arjun",20,"Java",69),
    (14,"Divya",19,"C",87),
    (15,"Vijay",21,"Python",90)
]
c.executemany(
    "INSERT INTO students(id,name,age,course,marks)VALUES (?,?,?,?,?)",
    students
)
con.commit()
print("10 students inserted successfully")
con.close()