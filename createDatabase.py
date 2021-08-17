import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="1234"
)

mycursor = con.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS hoteldb")

print("Database active")


con = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="1234",
    database="hoteldb"
)

mycursor = con.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS musteri(musteri_no INT PRIMARY KEY, musteri_tipi CHAR(1) NOT NULL)")

print("Table musteri active")

mycursor.execute("CREATE TABLE IF NOT EXISTS bireysel_musteri(musteri_no INT PRIMARY KEY, rezervasyon_no INT, oda_no INT, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, adres VARCHAR(100) NOT NULL, telefon_no VARCHAR(15) NOT NULL)")

print("Table bireysel_musteri active")

mycursor.execute("CREATE TABLE IF NOT EXISTS kurumsal_musteri(musteri_no INT PRIMARY KEY, kurum_ismi VARCHAR(100) NOT NULL, kurum_adresi VARCHAR(200) NOT NULL, kurum_tipi VARCHAR(100) NOT NULL, kurumsal_telefon VARCHAR(15) NOT NULL, kurumsal_mail VARCHAR(30) NOT NULL)")

print("Table kurumsal_musteri active")

mycursor.execute("CREATE TABLE IF NOT EXISTS personel(personel_no INT PRIMARY KEY, yonetici_no INT, tesis_no INT, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, telefon_no VARCHAR(15) NOT NULL, adres VARCHAR(100) NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, maas INT NOT NULL, gorev VARCHAR(30) NOT NULL, departman VARCHAR(30) NOT NULL, calisma_saati_baslangic VARCHAR(5) NOT NULL, calisma_saati_bitis VARCHAR(5) NOT NULL, izin_gunleri VARCHAR(200))")

print("Table personel active")

mycursor.execute("CREATE TABLE IF NOT EXISTS oda(oda_no INT PRIMARY KEY, rezervasyon_no INT, yatak_sayisi INT NOT NULL, oda_tipi VARCHAR(20) NOT NULL, fiyat INT NOT NULL, kat INT NOT NULL, cephe VARCHAR(10) NOT NULL)")

print("Table oda active")

mycursor.execute("CREATE TABLE IF NOT EXISTS rezervasyon(rezervasyon_no INT PRIMARY KEY, baslangic_tarihi DATE NOT NULL, bitis_tarihi DATE NOT NULL, fiyat INT NOT NULL)")

print("Table rezervasyon active")

mycursor.execute("CREATE TABLE IF NOT EXISTS tesis(tesis_no INT PRIMARY KEY, aktivite_no INT, kat INT NOT NULL, musteri_kapasitesi INT NOT NULL, personel_kapasitesi INT NOT NULL, faaliyet_baslangic_saati VARCHAR(10) NOT NULL, faaliyet_bitis_saati VARCHAR(10) NOT NULL, tesis_tipi VARCHAR(20) NOT NULL, aktif_personel_sayisi INT NOT NULL)")

print("Table rezervasyon active")

mycursor.execute("CREATE TABLE IF NOT EXISTS ticari_tesis(mulk_no INT PRIMARY KEY, kat INT NOT NULL, kira INT NOT NULL, tip VARCHAR(20) NOT NULL, vergi_no INT NOT NULL, kiralayan VARCHAR(30) NOT NULL, sozlesme_baslangic_tarihi DATE NOT NULL, sozlesme_bitis_tarihi DATE NOT NULL)")

print("Table ticari_tesis active")

mycursor.execute("CREATE TABLE IF NOT EXISTS aktivite(aktivite_no INT PRIMARY KEY, musteri_no INT, aktivite_baslangic_tarihi DATE NOT NULL, aktivite_bitis_tarihi DATE NOT NULL, aktivite_ismi VARCHAR(30) NOT NULL, ucret INT NOT NULL)")

print("Table aktivite active")

mycursor.execute(
    "ALTER TABLE bireysel_musteri ADD FOREIGN KEY (rezervasyon_no) REFERENCES rezervasyon(rezervasyon_no)")
mycursor.execute(
    "ALTER TABLE bireysel_musteri ADD FOREIGN KEY (oda_no) REFERENCES oda(oda_no)")
mycursor.execute(
    "ALTER TABLE personel ADD FOREIGN KEY (yonetici_no) REFERENCES personel(personel_no)")
mycursor.execute(
    "ALTER TABLE personel ADD FOREIGN KEY (tesis_no) REFERENCES tesis(tesis_no)")
mycursor.execute(
    "ALTER TABLE oda ADD FOREIGN KEY (rezervasyon_no) REFERENCES rezervasyon(rezervasyon_no)")
mycursor.execute(
    "ALTER TABLE tesis ADD FOREIGN KEY (aktivite_no) REFERENCES aktivite(aktivite_no)")
mycursor.execute(
    "ALTER TABLE aktivite ADD FOREIGN KEY (musteri_no) REFERENCES musteri(musteri_no)")

mycursor.execute("ALTER TABLE oda ADD INDEX (oda_no)")
mycursor.execute(
    "ALTER TABLE rezervasyon ADD INDEX (rezervasyon_no)")
