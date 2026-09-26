import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("DELETE FROM students WHERE id=5")
con.commit()
print("Student deleted successfully")
con.close()