const { Console } = require('console');
var mysql = require('mysql');
const { getSystemErrorMap } = require('util');

var con = mysql.createConnection({
    host: "localhost",
    user: "admin",
    password: "1234",
    database: "hoteldb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query("CREATE DATABASE hoteldb", function (err, result) {
    if (err) console.log("Database already exists");
    else console.log("Database created");
  });
  con.query("CREATE TABLE musteri(musteri_no INT PRIMARY KEY, musteri_tipi CHAR(1) NOT NULL)", function(err, result) {

      if(err) console.log("Table musteri already exists.");
      else console.log("Table musteri created.");
  });

  con.query("CREATE TABLE bireysel_musteri(musteri_no INT PRIMARY KEY, rezervasyon_no INT NOT NULL, oda_no INT NOT NULL, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, adres VARCHAR(100) NOT NULL, telefon_no VARCHAR(15) NOT NULL)", function(err, result) {

    if(err) console.log("Table bireysel_musteri already exists.");
    else console.log("Table bireysel_musteri Created");
  });

  con.query("CREATE TABLE personel(personel_no INT PRIMARY KEY, yonetici_no INT NOT NULL, tesis_no INT NOT NULL, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, telefon_no VARCHAR(15) NOT NULL, adres VARCHAR(100) NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, maas INT NOT NULL, gorev VARCHAR(30) NOT NULL, departman VARCHAR(30) NOT NULL, calisma_saati_baslangic VARCHAR(5) NOT NULL, calisma_saati_bitis VARCHAR(5) NOT NULL, izin_gunleri VARCHAR(200))", function(err, result) {

    if(err) console.log("Table personel already exists.");
    else console.log("Table personel Created");
  });

  con.query("CREATE TABLE oda(oda_no INT PRIMARY KEY, rezervasyon_no INT NOT NULL, yatak_sayisi INT NOT NULL, oda_tipi VARCHAR(20) NOT NULL, fiyat INT NOT NULL, kat INT NOT NULL, cephe VARCHAR(10) NOT NULL)", function(err, result) {

    if(err) console.log("Table oda already exists.");
    else console.log("Table oda Created");
  });
});


