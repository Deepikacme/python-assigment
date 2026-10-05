
import sqlite3
con=sqlite3.connect("college.db")
print("Database connected")
print("Connection failed")
con.close()
print("Connection closed")