import sqlite3

con=sqlite3.connect("college.db")
c=con.cursor()
c.execute("UPDATE students SET marks=95 WHERE id=1")
con.commit()
print("Marks updated successfully")
con.close()