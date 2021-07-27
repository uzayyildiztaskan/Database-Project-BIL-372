
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
    var sql = "INSERT INTO musteri(musteri_no, musteri_tipi) VALUES ?";
    var values= [
        [1, 1],
        [2, 1],
        [3, 2],
        [4, 2],
        [5, 2],
        [6, 1],
        [7, 2],
        [8, 1],
        [9, 2],
        [10, 1],
        [11, 1],
        [12, 2],
        [13, 2],
        [14, 1],
        [15, 2],
        [16, 2],
        [17, 2],
        [18, 1],
        [19, 1],
        [20, 2],
        [21, 1],
        [22, 2],
        [23, 2],
        [24, 1],
        [25, 2],
        [26, 1],
        [27, 2],
        [28, 1],
        [29, 1],
        [30, 1],
        [31, 2],
        [32, 2],
        [33, 1],
        [34, 1],
        [35, 1],
        [36, 2],
        [37, 1],
        [38, 2],
        [39, 1],
        [40, 2],
        [41, 1],
        [42, 2],
        [43, 1],
        [44, 2],
        [45, 2],
        [46, 1],
        [47, 1],
        [48, 2],
        [49, 1],
        [50, 1]
    ];
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
    
    sql = "INSERT INTO bireysel_musteri(musteri_no, rezervasyon_no, oda_no, kimlik_no, isim, soyisim, dogum_tarihi, yas, mail_adresi, kan_grubu, adres, telefon_no) VALUES ?";
    values = [
        [1, null, null, 769, 'Yasin', 'King', '1976/8/8', 44, 'Yasin@gmail.com', '0 rh-', '81 Seaton Place Northwest Washington DC 20001', '15122815673'],
        [2, null, null, 248, 'Ellis', 'Holt', '2003/10/27', 17, 'Ellis@gmail.com', 'A rh-', '5114 Greentree Drive Nashville TN 37211', '17143863667'],        
        [6, null, null, 128, 'Antonia', 'Norris', '2007/10/21', 13, 'Antonia@gmail.com', 'A rh-', '132 Laurel Green Court Savannah GA 31419', '13168473939'], 
        [8, null, null, 213, 'Charlotte', 'Carrillo', '1946/3/29', 74, 'Charlotte@gmail.com', 'B rh+', '22572 Toreador Drive Salinas CA 93908', '13171267357'],
        [10, null, null, 47, 'Maxwell', 'Solis', '2016/6/12', 4, 'Maxwell@gmail.com', 'AB rh+', '23 Sable Run Lane Methuen MA 01844', '13122243916'],
        [11, null, null, 717, 'Farhan', 'Lovell', '1972/2/6', 48, 'Farhan@gmail.com', 'A rh-', '74 Springfield Street B Agawam MA 01001', '18143918845'],
        [14, null, null, 324, 'Allen', 'Wagner', '1959/5/14', 61, 'Allen@gmail.com', 'B rh-', '8398 West Denton Lane Glendale AZ 85305', '19157254858'],
        [18, null, null, 550, 'Omar', 'Stanley', '1985/4/2', 35, 'Omar@gmail.com', 'AB rh+', '6657 West Rose Garden Lane Glendale AZ 85308', '17133102757'],
        [19, null, null, 567, 'Joel', 'Griffin', '1958/1/16', 62, 'Joel@gmail.com', '0 rh-', '1903 Bashford Manor Lane Louisville KY 40218', '17119138275'],
        [21, null, null, 641, 'Charles', 'King', '1947/11/15', 73, 'Charles@gmail.com', 'B rh+', '8800 Cordell Circle #APT 000003 Anchorage AK 99502', '18109599025'],
        [24, null, null, 244, 'Harley', 'Hunt', '1945/4/17', 75, 'Harley@gmail.com', 'A rh+', '1513 Cathy Street Savannah GA 31415', '13182865283'],
        [26, null, null, 185, 'Caitlyn', 'Griffin', '1951/2/3', 69, 'Caitlyn@gmail.com', 'AB rh+', '716 Waller Road Brentwood TN 37027', '17140785056'],
        [28, null, null, 233, 'Clayton', 'Wagner', '2007/4/3', 13, 'Clayton@gmail.com', 'A rh+', '165 Saint John Street Manchester CT 06040', '18152766625'],
        [29, null, null, 109, 'Clayton', 'Ortiz', '1955/11/28', 65, 'Clayton@gmail.com', '0 rh-', '913 Fallview Trail Nashville TN 37211', '19118519747'],
        [30, null, null, 373, 'Conor', 'Reid', '1992/5/20', 28, 'Conor@gmail.com', 'B rh-', '270 Chrissy\'s Court VT 05443', '18177429620'],
        [33, null, null, 28, 'Jimmy', 'Gomez', '1951/6/17', 69, 'Jimmy@gmail.com', 'A rh-', '1347 Blackwalnut Court Annapolis MD 21403', '17129040063'],
        [34, null, null, 106, 'Harley', 'Watson', '2017/11/29', 3, 'Harley@gmail.com', 'A rh-', '7431 Candace Way #1 Louisville KY 40214', '17125141290'],
        [35, null, null, 495, 'Connor', 'Shelton', '1942/8/26', 78, 'Connor@gmail.com', 'B rh+', '21950 Arnold Center Road Carson CA 90810', '19182519159'],
        [37, null, null, 615, 'Roman', 'Howarth', '1971/7/16', 49, 'Roman@gmail.com', '0 rh-', '1649 Timberridge Court Fayetteville AR 72704', '17152479654'],
        [39, null, null, 62, 'Zakariya', 'Graham', '1995/3/4', 25, 'Zakariya@gmail.com', 'AB rh+', '109 Summit Street Burlington VT 05401', '13177445747'],
        [41, null, null, 692, 'Casey', 'Mccarthy', '1970/1/23', 50, 'Casey@gmail.com', 'B rh+', '5108 Franklin Street Savannah GA 31405', '18110362118'],
        [43, null, null, 629, 'Roman', 'Olson', '1979/7/28', 41, 'Roman@gmail.com', 'AB rh+', '5461 West Shades Valley Drive Montgomery AL 36108', '17157122873'],
        [46, null, null, 293, 'Leonard', 'Howarth', '2016/1/4', 4, 'Leonard@gmail.com', 'B rh-', '87 Horseshoe Drive West Windsor VT 05037', '19159844899'],
        [47, null, null, 660, 'Dale', 'Fernandez', '1976/4/20', 44, 'Dale@gmail.com', 'A rh-', '6231 North 67th Avenue #241 Glendale AZ 85301', '17138073047'],
        [49, null, null, 364, 'Isobelle', 'Mccoy', '2018/1/2', 2, 'Isobelle@gmail.com', 'B rh+', '125 John Street Santa Cruz CA 95060', '13110421873'],
        [50, null, null, 505, 'Dale', 'Haynes', '1952/2/25', 68, 'Dale@gmail.com', 'A rh+', '60 Desousa Drive Manchester CT 06040', '13135885953']
    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });



    sql = "INSERT INTO personel(personel_no, yonetici_no, tesis_no, kimlik_no, isim, soyisim, dogum_tarihi, yas, telefon_no, adres, mail_adresi, kan_grubu, maas, gorev, departman, calisma_saati_baslangic, calisma_saati_bitis, izin_gunleri) VALUES ?";
    values = [
        [0, null, null, 7291253228, 'Harley', 'Briggs', '23/9/1958', 62, '13108165429', '4 Old Colony Way Yarmouth MA 02664', 'Harley@gmail.com', '0 rh-', 7500, 'Hizmet Personeli', 'Spa', '20.00', '08.00', 'Cumartesi-Pazar'],
        [1, null, null, 5312646933, 'Connor', 'Briggs', '26/2/1972', 48, '19128884766', '310 Timrod Road Manchester CT 06040', 'Connor@gmail.com', 'AB rh-', 10000, 'Yönetici', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [2, null, null, 1106489528, 'Amir', 'Shelton', '2/9/1971', 49, '17175209890', '8821 West Myrtle Avenue Glendale AZ 85305', 'Amir@gmail.com', '0 rh-', 7500, 'Sekreter', 'Spa', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [3, null, null, 5802774145, 'Ellie', 'Edwards', '27/2/1944', 76, '19160455660', '5108 Franklin Street Savannah GA 31405', 'Ellie@gmail.com', 'B rh+', 10000, 'Sekreter', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [4, null, null, 2969726746, 'Kieron', 'Hunt', '24/10/1952', 68, '15167618280', '8376 Albacore Drive Pasadena MD 21122', 'Kieron@gmail.com', 'AB rh+', 2800, 'Sekreter', 'Spor Salonu', '08.00', '20.00', 'Cumartesi-Pazar'],
        [5, null, null, 0927825671, 'Farhan', 'Moreno', '27/4/1949', 71, '19161959041', '1770 Colony Way Fayetteville AR 72704', 'Farhan@gmail.com', 'AB rh-', 2800, 'Sekreter', 'Golf', '09.00', '17.00', 'Pazar-Pazartesi'],
        [6, null, null, 6166265921, 'Yasin', 'Meyer', '7/12/2006', 14, '19178909397', '109 Summit Street Burlington VT 05401', 'Yasin@gmail.com', '0 rh+', 10000, 'Garson', 'Havuz', '09.00', '17.00', 'Pazartesi-Cuma'],
        [7, null, null, 5605889154, 'Zakariya', 'Meyer', '1/1/1976', 44, '17152343579', '165 Saint John Street Manchester CT 06040', 'Zakariya@gmail.com', 'AB rh-', 7500, 'Sekreter', 'Spa', '08.00', '20.00', 'Pazar-Pazartesi'],
        [8, null, null, 5048473335, 'Kieron', 'Reid', '12/5/1942', 78, '13198280368', '5114 Greentree Drive Nashville TN 37211', 'Kieron@gmail.com', 'A rh-', 5000, 'Yönetici', 'Disco', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [9, null, null, 6970034405, 'Roman', 'Mccoy', '9/1/1979', 41, '18176849148', '132 Laurel Green Court Savannah GA 31419', 'Roman@gmail.com', 'AB rh+', 10000, 'Hizmet Personeli', 'İdari', '09.00', '17.00', 'Pazartesi-Cuma'],
        [10, null, null, 8321518159, 'Tristan', 'Carrillo1', '9/11/1991', 29, '15160775515', '5811 Crossings Boulevard Nashville TN 37013', 'Tristan@gmail.com', 'B rh-', 10000, 'Yönetici', 'İdari', '08.00', '20.00', 'Cumartesi-Pazar'],
        [11, null, null, 6985139330, 'Ellie', 'Phillips', '4/7/1995', 25, '15126686680', '519 West 75th Avenue #APT 000003 Anchorage AK 99518', 'Ellie@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20.00', '08.00', 'Pazar-Pazartesi'],
        [12, null, null, 1168077233, 'Jimmy', 'White', '27/6/1969', 51, '19126123165', '1407 Walden Court Crofton MD 21114', 'Jimmy@gmail.com', 'B rh+', 5000, 'Muhasebeci', 'Disco', '09.00', '17.00', 'Cumartesi-Pazar'],
        [13, null, null, 7487528953, 'Zakariya', 'Rodriguez', '5/1/1940', 80, '19160028698', '210 Lacross Lane Westmore VT 05860', 'Zakariya@gmail.com', 'A rh-', 10000, 'Sekreter', 'Spa', '20.00', '08.00', 'Cumartesi-Pazar'],
        [14, null, null, 6431864495, 'Anabelle', 'Mullins', '25/9/1993', 27, '18190245594', '150 Carter Street Manchester CT 06040', 'Anabelle@gmail.com', '0 rh+', 3500, 'Hizmet Personeli', 'Spa', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [15, null, null, 5090093644, 'Allen', 'Mccoy', '22/6/1955', 65, '18167980382', '81 Seaton Place Northwest Washington DC 20001', 'Allen@gmail.com', '0 rh+', 10000, 'Yönetici', 'Spor Salonu', '20.00', '08.00', 'Pazartesi-Cuma'],
        [16, null, null, 2525078980, 'Charles', 'Mccarthy', '27/4/1940', 80, '18178033897', '1364 Capri Drive Panama City FL 32405', 'Charles@gmail.com', '0 rh-', 2800, 'Hizmet Personeli', 'Disco', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [17, null, null, 2941881759, 'Allanah', 'Carrillo1', '16/7/2010', 10, '19180437403', '130 Old Route 103 Chester VT 05143', 'Allanah@gmail.com', '0 rh-', 10000, 'Sekreter', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [18, null, null, 2662866012, 'Antonia', 'Mccoy', '13/7/1995', 25, '19117444795', '1508 Massachusetts Avenue Southeast Washington DC 20003', 'Antonia@gmail.com', 'A rh-', 10000, 'Hizmet Personeli', 'Golf', '08.00', '20.00', 'Cumartesi-Pazar'],
        [19, null, null, 6728937564, 'Connor', 'Griffin', '11/5/1949', 71, '19163533345', '8800 Cordell Circle #APT 000003 Anchorage AK 99502', 'Connor@gmail.com', 'B rh+', 3500, 'Garson', 'İdari', '09.00', '17.00', 'Cumartesi-Pazar'],
        [20, null, null, 4278891262, 'Allen', 'Griffin', '21/10/1968', 52, '19125292925', '5461 West Shades Valley Drive Montgomery AL 36108', 'Allen@gmail.com', 'B rh+', 5000, 'Sekreter', 'Havuz', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [21, null, null, 9921658691, 'Charlotte', 'Shelton', '23/7/1984', 36, '15184552956', '4 Old Colony Way Yarmouth MA 02664', 'Charlotte@gmail.com', 'A rh-', 10000, 'Garson', 'Mutfak', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [22, null, null, 3621798089, 'Caitlyn', 'Haynes', '5/8/2008', 12, '17152190173', '74 Ranch Drive Montgomery AL 36109', 'Caitlyn@gmail.com', 'AB rh-', 5000, 'Hizmet Personeli', 'İdari', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [23, null, null, 8267606466, 'Allanah', 'Olson', '11/6/1951', 69, '15171991394', '18 Densmore Drive Essex VT 05452', 'Allanah@gmail.com', 'A rh+', 2800, 'Yönetici', 'Golf', '20.00', '08.00', 'Cumartesi-Pazar'],
        [24, null, null, 6349573165, 'Leonard', 'Laing', '17/3/1993', 27, '13106770779', '8821 West Myrtle Avenue Glendale AZ 85305', 'Leonard@gmail.com', '0 rh+', 10000, 'Muhasebeci', 'Disco', '08.00', '20.00', 'Cumartesi-Pazar'],
        [25, null, null, 2259988038, 'Farhan', 'Carrillo1', '16/10/1975', 45, '15161565664', '232 Maine Avenue Panama City FL 32401', 'Farhan@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [26, null, null, 3687164176, 'Amir', 'Fernandez', '15/10/2019', 1, '19162422359', '210 Lacross Lane Westmore VT 05860', 'Amir@gmail.com', '0 rh-', 7500, 'Yönetici', 'Golf', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [27, null, null, 7540470286, 'Kieron', 'White', '3/12/1972', 48, '19125561305', '913 Fallview Trail Nashville TN 37211', 'Kieron@gmail.com', '0 rh-', 3500, 'Sekreter', 'Spor Salonu', '08.00', '20.00', 'Pazartesi-Cuma'],
        [28, null, null, 6111845998, 'Kieron', 'Shelton', '13/6/1990', 30, '17108941379', '1508 Massachusetts Avenue Southeast Washington DC 20003', 'Kieron@gmail.com', 'A rh-', 2800, 'Hizmet Personeli', 'Spa', '20.00', '08.00', 'Pazar-Pazartesi'],
        [29, null, null, 8984901187, 'Farhan', 'Edwards', '15/2/1953', 67, '18138491711', '232 Maine Avenue Panama City FL 32401', 'Farhan@gmail.com', '0 rh+', 10000, 'Sekreter', 'İdari', '20.00', '08.00', 'Cumartesi-Pazar']
        

    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });


    sql = "INSERT INTO oda(oda_no, rezervasyon_no, yatak_sayisi, oda_tipi, fiyat, kat, cephe) VALUES ?";
    values = [
        [0, 4916, 1, 'Normal', 4000, 1, 'Doğu'],
        [1, 2871, 6, 'Ultra Deluxe', 750, 3, 'Doğu'],
        [2, 2896, 4, 'Family Room', 15000, 4, 'Kuzey'],
        [3, 2378, 6, 'Ultra Deluxe', 500, 2, 'Kuzey'],
        [4, 578, 1, 'Suite', 2000, 3, 'Kuzey'],
        [5, 4940, 3, 'Deluxe', 15000, 1, 'Güney'],
        [6, 467, 3, 'Normal', 1000, 1, 'Güney'],
        [7, 975, 3, 'Ultra Deluxe', 4000, 4, 'Doğu'],
        [8, 1128, 1, 'Deluxe', 1000, 2, 'Güney'],
        [9, 1840, 5, 'Ultra Deluxe', 4000, 1, 'Güney'],
        [10, 3105, 2, 'Normal', 15000, 3, 'Güney'],
        [11, 3767, 4, 'Normal', 2000, 4, 'Kuzey'],
        [12, 1721, 5, 'Ultra Deluxe', 1000, 4, 'Güney'],
        [13, 4782, 1, 'Deluxe', 2000, 2, 'Güney'],
        [14, 1958, 2, 'Normal', 750, 3, 'Kuzey'],
        [15, 4299, 5, 'King Suite', 4000, 3, 'Güney'],
        [16, 4399, 2, 'King Suite', 15000, 5, 'Doğu'],
        [17, 4060, 2, 'Suite', 15000, 1, 'Kuzey'],
        [18, 1650, 2, 'King Suite', 2000, 5, 'Batı'],
        [19, 2306, 1, 'Deluxe', 15000, 4, 'Kuzey'],
        [20, 1894, 1, 'Normal', 4000, 2, 'Güney'],
        [21, 487, 5, 'Suite', 4000, 5, 'Kuzey'],
        [22, 5104, 2, 'Normal', 750, 5, 'Batı'],
        [23, 3468, 4, 'Deluxe', 2000, 3, 'Batı'],
        [24, 3098, 6, 'King Suite', 2000, 2, 'Doğu'],
        [25, 5046, 4, 'Family Room', 1000, 4, 'Doğu'],
        [26, 1946, 3, 'King Suite', 750, 1, 'Batı'],
        [27, 688, 2, 'Suite', 4000, 5, 'Kuzey'],
        [28, 4329, 1, 'Family Room', 750, 3, 'Batı'],
        [29, 3682, 2, 'Normal', 750, 4, 'Batı'],
        [30, 5221, 2, 'Deluxe', 500, 3, 'Doğu'],
        [31, 4444, 3, 'Suite', 750, 4, 'Batı'],
        [32, 1762, 4, 'Suite', 2000, 5, 'Kuzey'],
        [33, 423, 1, 'Normal', 1000, 2, 'Kuzey'],
        [34, 2444, 6, 'King Suite', 15000, 3, 'Doğu'],
        [35, 1040, 5, 'King Suite', 15000, 4, 'Doğu'],
        [36, 1642, 2, 'Family Room', 2000, 2, 'Güney'],
        [37, 3262, 3, 'Deluxe', 2000, 1, 'Batı'],
        [38, 3200, 2, 'Ultra Deluxe', 1000, 3, 'Güney'],
        [39, 3791, 1, 'Normal', 4000, 3, 'Kuzey'],
        [40, 1160, 3, 'Normal', 4000, 4, 'Batı'],
        [41, 3489, 2, 'Suite', 500, 4, 'Güney'],
        [42, 1817, 6, 'King Suite', 500, 5, 'Batı'],
        [43, 3475, 5, 'Ultra Deluxe', 4000, 2, 'Batı'],
        [44, 4103, 6, 'Family Room', 1000, 4, 'Güney'],
        [45, 390, 4, 'Ultra Deluxe', 1000, 5, 'Batı'],
        [46, 4841, 2, 'King Suite', 2000, 1, 'Doğu'],
        [47, 591, 3, 'Suite', 4000, 3, 'Doğu'],
        [48, 1656, 6, 'Family Room', 4000, 2, 'Batı'],
        [49, 4525, 3, 'Family Room', 2000, 1, 'Güney'],
        [50, 4318, 2, 'Deluxe', 2000, 5, 'Güney'],
        [51, 3249, 2, 'Deluxe', 500, 1, 'Güney'],
        [52, 4971, 4, 'Suite', 1000, 1, 'Güney'],
        [53, 3984, 4, 'Family Room', 1000, 4, 'Batı'],
        [54, 4120, 3, 'Deluxe', 500, 4, 'Güney'],
        [55, 728, 3, 'Normal', 15000, 3, 'Batı'],
        [56, 2380, 1, 'Deluxe', 500, 4, 'Kuzey'],
        [57, 4337, 3, 'Normal', 500, 5, 'Kuzey'],
        [58, 2825, 6, 'King Suite', 1000, 1, 'Doğu'],
        [59, 4040, 5, 'Suite', 750, 1, 'Batı'],
        [60, 371, 5, 'Ultra Deluxe', 1000, 5, 'Batı'],
        [61, 4190, 4, 'King Suite', 15000, 2, 'Kuzey'],
        [62, 2879, 4, 'Suite', 15000, 3, 'Doğu'],
        [63, 1030, 5, 'Family Room', 15000, 3, 'Kuzey'],
        [64, 3694, 2, 'Normal', 15000, 4, 'Doğu'],
        [65, 4538, 1, 'Family Room', 500, 4, 'Güney'],
        [66, 2053, 5, 'Deluxe', 500, 1, 'Batı'],
        [67, 4838, 5, 'Normal', 750, 1, 'Batı'],
        [68, 1226, 1, 'Deluxe', 4000, 3, 'Batı'],
        [69, 1352, 4, 'Deluxe', 15000, 4, 'Kuzey'],
        [70, 4435, 3, 'Suite', 15000, 1, 'Kuzey'],
        [71, 779, 6, 'Normal', 500, 1, 'Batı'],
        [72, 459, 3, 'King Suite', 4000, 4, 'Batı'],
        [73, 2072, 5, 'King Suite', 500, 1, 'Doğu'],
        [74, 4443, 3, 'Normal', 4000, 4, 'Güney']
        
    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });


    sql = "INSERT INTO aktivite(aktivite_no, musteri_no, aktivite_baslangic_tarihi, aktivite_bitis_tarihi, aktivite_ismi, ucret) VALUES ?";
    values = [
        [0, 47, '28/1/1957', '32/1/1957', 'Dans Gösterisi', 100],
        [1, null, '26/8/1959', '27/8/1959', 'Dans Gösterisi', 1000],
        [2, 43, '5/5/1987', '8/5/1987', 'Paintball', 0],
        [3, 18, '18/2/1997', '21/2/1997', 'Egzotik Masaj', 0],
        [4, 36, '7/2/1987', '7/2/1987', 'Golf', 50],
        [5, null, '29/4/1956', '30/4/1956', 'Dans Gösterisi', 500],
        [6, 2, '30/3/1970', '34/3/1970', 'Diving Yarismasi', 0],
        [7, 9, '30/8/1982', '31/8/1982', 'Golf', 250],
        [8, 45, '2/8/2002', '4/8/2002', 'Su Topu', 100],
        [9, 27, '20/1/1959', '23/1/1959', 'Dans Gösterisi', 1000]
         
    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });




});