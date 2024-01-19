import sqlite3

conn = sqlite3.connect('veritabani.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE kisiler
    (isim TEXT, soyisim TEXT, yas INTEGER, sehir TEXT)
''')
c.execute("INSERT INTO kisiler VALUES ('Emirhan', 'Pelin', 30, 'Istanbul')")
conn.commit()
conn.close()