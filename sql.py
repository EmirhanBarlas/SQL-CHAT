import sqlite3 # Sqlite3 kütüphanesini dahil ediyoruz.

conn = sqlite3.connect('veritabani.db') # veritabani.db adında bir veritabanı dosyası oluşturuyoruz.
c = conn.cursor() # Veritabanı üzerinde işlem yapabilmek için bir imleç oluşturuyoruz.
c.execute('''
    CREATE TABLE kisiler
    (isim TEXT, soyisim TEXT, yas INTEGER, sehir TEXT, country TEXT)
''') # Veritabanında kisiler tablosunu oluşturuyoruz.
c.execute("INSERT INTO kisiler VALUES ('Emirhan', 'Pelin', 30, 'Istanbul', 'Turkey')") # Veritabanına veri ekliyoruz.
conn.commit() # Veritabanı üzerindeki değişiklikleri kaydediyoruz.
conn.close() # Veritabanı bağlantısını kapatıyoruz.