exports.createDatabaseNTables = function () {

  var mysql = require('mysql');

  var con =  mysql.createConnection({
      host: "localhost",
      user: "admin",
      password: "1234"
  });

    con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
      con.query("CREATE DATABASE hoteldb", function (err, result) {

      if(err) {
        if (err.sqlMessage.includes('database exists')) console.log("Database already exists.");
        else console.log(err.message)
      }

      else{

        console.log("Database created");   

        con = mysql.createConnection({
          host: "localhost",
          user: "admin",
          password: "1234",
          database: "hoteldb"
        });

          con.query("CREATE TABLE musteri(musteri_no INT PRIMARY KEY, musteri_tipi CHAR(1) NOT NULL)",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table musteri already exists.");
            else console.log(err.message)
          }
            else console.log("Table musteri created.");
        });
      
          con.query("CREATE TABLE bireysel_musteri(musteri_no INT PRIMARY KEY, rezervasyon_no INT, oda_no INT, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, adres VARCHAR(100) NOT NULL, telefon_no VARCHAR(15) NOT NULL)",function(err, result) {
      
          if(err) {
            if(err.message.includes('already exists')) console.log("Table bireysel_musteri already exists.");
            else console.log(err.message)
          }
            else console.log("Table bireysel_musteri created.");
        });
      
          con.query("CREATE TABLE kurumsal_musteri(musteri_no INT PRIMARY KEY, kurum_ismi VARCHAR(100) NOT NULL, kurum_adresi VARCHAR(200) NOT NULL, kurum_tipi VARCHAR(100) NOT NULL, kurumsal_telefon VARCHAR(15) NOT NULL, kurumsal_mail VARCHAR(30) NOT NULL)",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table kurumsal_musteri already exists.");
            else console.log(err.message)
          }
            else console.log("Table kurumsal_musteri created.");
        });
      
          con.query("CREATE TABLE personel(personel_no INT PRIMARY KEY, yonetici_no INT, tesis_no INT, kimlik_no INT NOT NULL, isim VARCHAR(20) NOT NULL, soyisim VARCHAR(20) NOT NULL, dogum_tarihi DATE NOT NULL, yas INT NOT NULL, telefon_no VARCHAR(15) NOT NULL, adres VARCHAR(100) NOT NULL, mail_adresi VARCHAR(30) NOT NULL, kan_grubu VARCHAR(10) NOT NULL, maas INT NOT NULL, gorev VARCHAR(30) NOT NULL, departman VARCHAR(30) NOT NULL, calisma_saati_baslangic VARCHAR(5) NOT NULL, calisma_saati_bitis VARCHAR(5) NOT NULL, izin_gunleri VARCHAR(200))",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table personel already exists.");
            else console.log(err.message)
          }
            else console.log("Table personel created.");
        });
      
          con.query("CREATE TABLE oda(oda_no INT PRIMARY KEY, rezervasyon_no INT, yatak_sayisi INT NOT NULL, oda_tipi VARCHAR(20) NOT NULL, fiyat INT NOT NULL, kat INT NOT NULL, cephe VARCHAR(10) NOT NULL)",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table oda already exists.");
            else console.log(err.message)
          }
            else console.log("Table oda created.");
        });
      
          con.query("CREATE TABLE rezervasyon(rezervasyon_no INT PRIMARY KEY, musteri_no INT, oda_sayisi INT NOT NULL, kisi_sayisi INT NOT NULL, baslangic_tarihi DATE NOT NULL, bitis_tarihi DATE NOT NULL, fiyat INT NOT NULL)",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table rezervasyon already exists.");
            else console.log(err.message)
          }
            else console.log("Table rezervasyon created.");
        });
        
        
          con.query("CREATE TABLE tesis(tesis_no INT PRIMARY KEY, aktivite_no INT, kat INT NOT NULL, musteri_kapasitesi INT NOT NULL, personel_kapasitesi INT NOT NULL, faaliyet_baslangic_saati VARCHAR(10) NOT NULL, faaliyet_bitis_saati VARCHAR(10) NOT NULL, tesis_tipi VARCHAR(20) NOT NULL, aktif_personel_sayisi INT NOT NULL)", function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table tesis already exists.");
            else console.log(err.message)
          }
            else console.log("Table tesis created.");
        });
        
          con.query("CREATE TABLE ticari_tesis(mulk_no INT PRIMARY KEY, kat INT NOT NULL, kira INT NOT NULL, tip VARCHAR(20) NOT NULL, vergi_no INT NOT NULL, kiralayan VARCHAR(30) NOT NULL, sozlesme_baslangic_tarihi DATE NOT NULL, sozlesme_bitis_tarihi DATE NOT NULL)",function(err, result) {

          if(err) {
            if(err.message.includes('already exists')) console.log("Table ticari_tesis already exists.");
            else console.log(err.message)
          }
            else console.log("Table ticari_tesis created.");
        });        
        
          con.query("CREATE TABLE aktivite(aktivite_no INT PRIMARY KEY, musteri_no INT, aktivite_baslangic_tarihi DATE NOT NULL, aktivite_bitis_tarihi DATE NOT NULL, aktivite_ismi VARCHAR(30) NOT NULL, ucret INT NOT NULL)",function(err, result) {
      
          if(err) {
            if(err.message.includes('already exists')) console.log("Table aktivite already exists.");
            else console.log(err.message)
          }
            else console.log("Table aktivite created.");
        });

          con.query("ALTER TABLE bireysel_musteri ADD FOREIGN KEY (rezervasyon_no) REFERENCES rezervasyon(rezervasyon_no)");
          con.query("ALTER TABLE bireysel_musteri ADD FOREIGN KEY (oda_no) REFERENCES oda(oda_no)");
          con.query("ALTER TABLE personel ADD FOREIGN KEY (yonetici_no) REFERENCES personel(personel_no)");
          con.query("ALTER TABLE personel ADD FOREIGN KEY (tesis_no) REFERENCES tesis(tesis_no)");
          con.query("ALTER TABLE oda ADD FOREIGN KEY (rezervasyon_no) REFERENCES rezervasyon(rezervasyon_no)");
          con.query("ALTER TABLE rezervasyon ADD FOREIGN KEY (musteri_no) REFERENCES musteri(musteri_no)");
          con.query("ALTER TABLE tesis ADD FOREIGN KEY (aktivite_no) REFERENCES aktivite(aktivite_no)");
          con.query("ALTER TABLE aktivite ADD FOREIGN KEY (musteri_no) REFERENCES musteri(musteri_no)");
      }
    });
  });
}





