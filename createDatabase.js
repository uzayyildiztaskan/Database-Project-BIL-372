const { Console } = require('console');
var mysql = require('mysql');

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
});