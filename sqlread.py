import sqlite3

conn = sqlite3.connect('veritabani.db')
c = conn.cursor()

c.execute("SELECT * FROM kisiler")
rows = c.fetchall() 

for row in rows:
    print(row) 
conn.close()