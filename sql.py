import sqlite3

conn = sqlite3.connect('veritabani.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE kisiler
    (isim TEXT, soyisim TEXT)
''')
c.execute("INSERT INTO kisiler VALUES ('Ahmet', 'Mehmet')")
conn.commit()
conn.close()