
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

    sql = "INSERT INTO rezervasyon(rezervasyon_no, musteri_no, oda_sayisi, kisi_sayisi, baslangic_tarihi, bitis_tarihi, fiyat) VALUES ?";
    values = [
        [543, null, 3, 1, '1982/12/2', '1982/12/8', 3690],
        [532, null, 2, 5, '2007/9/15', '2007/9/18', 2556],
        [182, null, 3, 4, '2000/3/5', '2000/3/13', 2139],
        [439, null, 1, 5, '2012/5/3', '2012/5/5', 521],
        [503, null, 1, 5, '2009/8/16', '2009/8/22', 870],
        [353, null, 1, 1, '2005/6/11', '2005/6/15', 1441],
        [433, null, 2, 2, '2004/2/3', '2004/2/8', 2470],
        [79, null, 3, 3, '2008/7/8', '2008/7/15', 4143],
        [177, null, 1, 3, '2015/10/13', '2015/10/19', 1160],
        [53, null, 3, 4, '2018/2/22', '2018/2/25', 3318],
        [997, null, 3, 5, '1983/10/30', '1983/11/5', 2985],
        [502, null, 3, 3, '1983/10/12', '1983/10/18', 4272],
        [782, null, 2, 7, '2013/5/28', '2013/6/3', 1578],
        [440, null, 1, 6, '1983/12/21', '1983/12/26', 814],
        [236, null, 1, 6, '2019/5/20', '2019/5/28', 543],
        [179, null, 3, 4, '2010/1/17', '2010/1/19', 2787],
        [379, null, 2, 4, '1986/3/8', '1986/3/15', 2852],
        [381, null, 2, 4, '1995/5/27', '1995/6/1', 2428],
        [936, null, 2, 3, '2020/11/12', '2020/11/14', 1920],
        [407, null, 3, 1, '1984/10/10', '1984/10/13', 3801],
        [278, null, 2, 4, '1980/8/10', '1980/8/13', 2362],
        [469, null, 2, 7, '1993/12/30', '1994/1/7', 2870],
        [411, null, 3, 7, '1990/8/15', '1990/8/20', 3876],
        [89, null, 3, 3, '2009/1/22', '2009/1/29', 3456],
        [519, null, 1, 3, '1990/12/10', '1990/12/17', 1310],
        [347, null, 2, 6, '1985/3/30', '1985/3/7', 1020],
        [553, null, 2, 6, '2010/2/16', '2010/2/20', 2384],
        [438, null, 2, 2, '2000/2/14', '2000/2/18', 1144],
        [377, null, 2, 1, '2018/6/27', '2018/7/4', 1912],
        [27, null, 2, 1, '1993/10/4', '1993/10/7', 1850],
        [958, null, 1, 2, '1993/11/10', '1993/11/12', 1290],
        [907, null, 3, 6, '1988/3/7', '1988/3/14', 2892],
        [115, null, 2, 3, '1985/7/5', '1985/7/7', 2280],
        [456, null, 2, 4, '1981/11/22', '1981/11/29', 2846],
        [310, null, 2, 2, '1989/8/11', '1989/8/18', 1608]
    ];
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });

    sql = "INSERT INTO tesis(tesis_no, aktivite_no, kat, musteri_kapasitesi, personel_kapasitesi, faaliyet_baslangic_saati, faaliyet_bitis_saati, tesis_tipi, aktif_personel_sayisi) VALUES ?";
    values = [
        [1, null, 2, 75, 10, "08:30", "11:30", "Breakfast Saloon", 6],
        [2, null, 1, 30, 5, "12:30", "18:30", "Game Saloon", 4],
        [3, null, 0, 100, 10, "08:30", "23:30", "Pool", 6],
        [4, null, 2, 40, 4, "19:00", "02:00", "Bar", 4],
        [5, null, 0, 44, 3, "08:30", "22:30", "Football Pitch", 1],
        [6, null, 2, 20, 10, "14:00", "18:00", "Massage Spa", 9],
        [7, null, 1, 50, 1, "20:30", "23:30", "Movie Theater", 1],
        [8, null, 3, 80, 20, "22:30", "03:30", "Disco", 16],
        [9, null, 0, 30, 5, "09:00", "17:00", "Golf Pitch", 5],
        [10, null, 3, 100, 30, "18:30", "21:30", "Diner Saloon", 27]
    ];
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });

    sql = "INSERT INTO ticari_tesis(mulk_no, kat, kira, tip, vergi_no, kiralayan, sozlesme_baslangic_tarihi, sozlesme_bitis_tarihi) VALUES ?";
    values = [
        [1, 2, 3000, 'Conferance Room', 60069468, "Eco Focus", "2021/04/15", "2021/04/19"],
        [2, 0, 5000, 'Market', 24655609, "Migros Market", "2017/08/01", "2023/08/01"],
        [3, 2, 3000, 'Conferance Room', 41925201, "Inspire Fitness Co", "2016/01/22", "2016/01/24"],
        [4, 0, 8000, 'Market', 21116262, "Migros Market", "2019/03/1", "2025/03/1"],
        [5, 0, 8000, 'Market', 35309419, "A101", "2021/01/01", "2027/01/01"]
    ];
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });

    sql = "INSERT INTO personel(personel_no, yonetici_no, tesis_no, kimlik_no, isim, soyisim, dogum_tarihi, yas, telefon_no, adres, mail_adresi, kan_grubu, maas, gorev, departman, calisma_saati_baslangic, calisma_saati_bitis, izin_gunleri) VALUES ?";
    values = [
        [0, null, null, 729125322, 'Harley', 'Briggs', '1958/09/23', 62, '13108165429', '4 Old Colony Way Yarmouth MA 02664', 'Harley@gmail.com', '0 rh-', 7500, 'Hizmet Personeli', 'Spa', '20.00', '08.00', 'Cumartesi-Pazar'],
        [1, null, null, 531264693, 'Connor', 'Briggs', '1972/02/26', 48, '19128884766', '310 Timrod Road Manchester CT 06040', 'Connor@gmail.com', 'AB rh-', 10000, 'Yönetici', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [2, null, null, 110648952, 'Amir', 'Shelton', '1971/09/02', 49, '17175209890', '8821 West Myrtle Avenue Glendale AZ 85305', 'Amir@gmail.com', '0 rh-', 7500, 'Sekreter', 'Spa', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [3, null, null, 580277414, 'Ellie', 'Edwards', '1944/02/27', 76, '19160455660', '5108 Franklin Street Savannah GA 31405', 'Ellie@gmail.com', 'B rh+', 10000, 'Sekreter', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [4, null, null, 296972674, 'Kieron', 'Hunt', '1952/10/24', 68, '15167618280', '8376 Albacore Drive Pasadena MD 21122', 'Kieron@gmail.com', 'AB rh+', 2800, 'Sekreter', 'Spor Salonu', '08.00', '20.00', 'Cumartesi-Pazar'],
        [5, null, null, 092782567, 'Farhan', 'Moreno', '1949/04/13', 71, '19161959041', '1770 Colony Way Fayetteville AR 72704', 'Farhan@gmail.com', 'AB rh-', 2800, 'Sekreter', 'Golf', '09.00', '17.00', 'Pazar-Pazartesi'],
        [6, null, null, 616626592, 'Yasin', 'Meyer', '2006/12/07', 14, '19178909397', '109 Summit Street Burlington VT 05401', 'Yasin@gmail.com', '0 rh+', 10000, 'Garson', 'Havuz', '09.00', '17.00', 'Pazartesi-Cuma'],
        [7, null, null, 560588915, 'Zakariya', 'Meyer', '1976/01/01', 44, '17152343579', '165 Saint John Street Manchester CT 06040', 'Zakariya@gmail.com', 'AB rh-', 7500, 'Sekreter', 'Spa', '08.00', '20.00', 'Pazar-Pazartesi'],
        [8, null, null, 504847333, 'Kieron', 'Reid', '1942/05/12', 78, '13198280368', '5114 Greentree Drive Nashville TN 37211', 'Kieron@gmail.com', 'A rh-', 5000, 'Yönetici', 'Disco', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [9, null, null, 697003440, 'Roman', 'Mccoy', '1979/01/09', 41, '18176849148', '132 Laurel Green Court Savannah GA 31419', 'Roman@gmail.com', 'AB rh+', 10000, 'Hizmet Personeli', 'İdari', '09.00', '17.00', 'Pazartesi-Cuma'],
        [10, null, null, 832151819, 'Tristan', 'Carrillo1', '1991/11/09', 29, '15160775515', '5811 Crossings Boulevard Nashville TN 37013', 'Tristan@gmail.com', 'B rh-', 10000, 'Yönetici', 'İdari', '08.00', '20.00', 'Cumartesi-Pazar'],
        [11, null, null, 698513933, 'Ellie', 'Phillips', '1995/07/04', 25, '15126686680', '519 West 75th Avenue #APT 000003 Anchorage AK 99518', 'Ellie@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20.00', '08.00', 'Pazar-Pazartesi'],
        [12, null, null, 116807723, 'Jimmy', 'White', '1969/06/27', 51, '19126123165', '1407 Walden Court Crofton MD 21114', 'Jimmy@gmail.com', 'B rh+', 5000, 'Muhasebeci', 'Disco', '09.00', '17.00', 'Cumartesi-Pazar'],
        [13, null, null, 748752853, 'Zakariya', 'Rodriguez', '1940/01/05', 80, '19160028698', '210 Lacross Lane Westmore VT 05860', 'Zakariya@gmail.com', 'A rh-', 10000, 'Sekreter', 'Spa', '20.00', '08.00', 'Cumartesi-Pazar'],
        [14, null, null, 643186495, 'Anabelle', 'Mullins', '1993/09/25', 27, '18190245594', '150 Carter Street Manchester CT 06040', 'Anabelle@gmail.com', '0 rh+', 3500, 'Hizmet Personeli', 'Spa', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [15, null, null, 509003644, 'Allen', 'Mccoy', '1955/06/22', 65, '18167980382', '81 Seaton Place Northwest Washington DC 20001', 'Allen@gmail.com', '0 rh+', 10000, 'Yönetici', 'Spor Salonu', '20.00', '08.00', 'Pazartesi-Cuma'],
        [16, null, null, 252578980, 'Charles', 'Mccarthy', '1940/04/24', 80, '18178033897', '1364 Capri Drive Panama City FL 32405', 'Charles@gmail.com', '0 rh-', 2800, 'Hizmet Personeli', 'Disco', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [17, null, null, 294881759, 'Allanah', 'Carrillo1', '2010/07/16', 10, '19180437403', '130 Old Route 103 Chester VT 05143', 'Allanah@gmail.com', '0 rh-', 10000, 'Sekreter', 'Disco', '20.00', '08.00', 'Pazartesi-Cuma'],
        [18, null, null, 262866012, 'Antonia', 'Mccoy', '1995/07/13', 25, '19117444795', '1508 Massachusetts Avenue Southeast Washington DC 20003', 'Antonia@gmail.com', 'A rh-', 10000, 'Hizmet Personeli', 'Golf', '08.00', '20.00', 'Cumartesi-Pazar'],
        [19, null, null, 628937564, 'Connor', 'Griffin', '1949/05/11', 71, '19163533345', '8800 Cordell Circle #APT 000003 Anchorage AK 99502', 'Connor@gmail.com', 'B rh+', 3500, 'Garson', 'İdari', '09.00', '17.00', 'Cumartesi-Pazar'],
        [20, null, null, 427889126, 'Allen', 'Griffin', '1968/10/21', 52, '19125292925', '5461 West Shades Valley Drive Montgomery AL 36108', 'Allen@gmail.com', 'B rh+', 5000, 'Sekreter', 'Havuz', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [21, null, null, 992165861, 'Charlotte', 'Shelton', '1984/07/23', 36, '15184552956', '4 Old Colony Way Yarmouth MA 02664', 'Charlotte@gmail.com', 'A rh-', 10000, 'Garson', 'Mutfak', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [22, null, null, 362179889, 'Caitlyn', 'Haynes', '2008/08/05', 12, '17152190173', '74 Ranch Drive Montgomery AL 36109', 'Caitlyn@gmail.com', 'AB rh-', 5000, 'Hizmet Personeli', 'İdari', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [23, null, null, 826760466, 'Allanah', 'Olson', '1951/06/11', 69, '15171991394', '18 Densmore Drive Essex VT 05452', 'Allanah@gmail.com', 'A rh+', 2800, 'Yönetici', 'Golf', '20.00', '08.00', 'Cumartesi-Pazar'],
        [24, null, null, 634953165, 'Leonard', 'Laing', '1993/03/17', 27, '13106770779', '8821 West Myrtle Avenue Glendale AZ 85305', 'Leonard@gmail.com', '0 rh+', 10000, 'Muhasebeci', 'Disco', '08.00', '20.00', 'Cumartesi-Pazar'],
        [25, null, null, 22988038, 'Farhan', 'Carrillo1', '1975/10/16', 45, '15161565664', '232 Maine Avenue Panama City FL 32401', 'Farhan@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20.00', '08.00', 'Pazartesi-Perşembe'],
        [26, null, null, 368716417, 'Amir', 'Fernandez', '2019/10/15', 1, '19162422359', '210 Lacross Lane Westmore VT 05860', 'Amir@gmail.com', '0 rh-', 7500, 'Yönetici', 'Golf', '09.00', '17.00', 'Pazartesi-Perşembe'],
        [27, null, null, 754470286, 'Kieron', 'White', '1972/12/03', 48, '19125561305', '913 Fallview Trail Nashville TN 37211', 'Kieron@gmail.com', '0 rh-', 3500, 'Sekreter', 'Spor Salonu', '08.00', '20.00', 'Pazartesi-Cuma'],
        [28, null, null, 611845998, 'Kieron', 'Shelton', '1990/06/13', 30, '17108941379', '1508 Massachusetts Avenue Southeast Washington DC 20003', 'Kieron@gmail.com', 'A rh-', 2800, 'Hizmet Personeli', 'Spa', '20.00', '08.00', 'Pazar-Pazartesi'],
        [29, null, null, 884901187, 'Farhan', 'Edwards', '1953/02/15', 67, '18138491711', '232 Maine Avenue Panama City FL 32401', 'Farhan@gmail.com', '0 rh+', 10000, 'Sekreter', 'İdari', '20.00', '08.00', 'Cumartesi-Pazar']
        

    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });


    sql = "INSERT INTO oda(oda_no, rezervasyon_no, yatak_sayisi, oda_tipi, fiyat, kat, cephe) VALUES ?";
    values = [
        [1, null, 1, 'Normal', 4000, 1, 'Doğu'],
        [2, null, 6, 'Ultra Deluxe', 750, 3, 'Doğu'],
        [3, null, 4, 'Family Room', 15000, 4, 'Kuzey'],
        [4, null, 6, 'Ultra Deluxe', 500, 2, 'Kuzey'],
        [5, null, 1, 'Suite', 2000, 3, 'Kuzey'],
        [6, null, 3, 'Deluxe', 15000, 1, 'Güney'],
        [7, null, 3, 'Normal', 1000, 1, 'Güney'],
        [8, null, 3, 'Ultra Deluxe', 4000, 4, 'Doğu'],
        [9, null, 1, 'Deluxe', 1000, 2, 'Güney'],
        [10, null, 5, 'Ultra Deluxe', 4000, 1, 'Güney'],
        [11, null, 2, 'Normal', 15000, 3, 'Güney'],
        [12, null, 4, 'Normal', 2000, 4, 'Kuzey'],
        [13, null, 5, 'Ultra Deluxe', 1000, 4, 'Güney'],
        [14, null, 1, 'Deluxe', 2000, 2, 'Güney'],
        [15, null, 2, 'Normal', 750, 3, 'Kuzey'],
        [16, null, 5, 'King Suite', 4000, 3, 'Güney'],
        [17, null, 2, 'King Suite', 15000, 5, 'Doğu'],
        [18, null, 2, 'Suite', 15000, 1, 'Kuzey'],
        [19, null, 2, 'King Suite', 2000, 5, 'Batı'],
        [20, null, 1, 'Deluxe', 15000, 4, 'Kuzey'],
        [21, null, 1, 'Normal', 4000, 2, 'Güney'],
        [22, null, 5, 'Suite', 4000, 5, 'Kuzey'],
        [23, null, 2, 'Normal', 750, 5, 'Batı'],
        [24, null, 4, 'Deluxe', 2000, 3, 'Batı'],
        [25, null, 6, 'King Suite', 2000, 2, 'Doğu'],
        [26, null, 4, 'Family Room', 1000, 4, 'Doğu'],
        [27, null, 3, 'King Suite', 750, 1, 'Batı'],
        [28, null, 2, 'Suite', 4000, 5, 'Kuzey'],
        [29, null, 1, 'Family Room', 750, 3, 'Batı'],
        [30, null, 2, 'Normal', 750, 4, 'Batı'],
        [31, null, 2, 'Deluxe', 500, 3, 'Doğu'],
        [32, null, 3, 'Suite', 750, 4, 'Batı'],
        [33, null, 4, 'Suite', 2000, 5, 'Kuzey'],
        [34, null, 1, 'Normal', 1000, 2, 'Kuzey'],
        [35, null, 6, 'King Suite', 15000, 3, 'Doğu'],
        [36, null, 5, 'King Suite', 15000, 4, 'Doğu'],
        [37, null, 2, 'Family Room', 2000, 2, 'Güney'],
        [38, null, 3, 'Deluxe', 2000, 1, 'Batı'],
        [39, null, 2, 'Ultra Deluxe', 1000, 3, 'Güney'],
        [40, null, 3, 'Normal', 4000, 4, 'Batı'],
        [41, null, 2, 'Suite', 500, 4, 'Güney'],
        [42, null, 6, 'King Suite', 500, 5, 'Batı'],
        [43, null, 5, 'Ultra Deluxe', 4000, 2, 'Batı'],
        [44, null, 6, 'Family Room', 1000, 4, 'Güney'],
        [45, null, 4, 'Ultra Deluxe', 1000, 5, 'Batı'],
        [46, null, 2, 'King Suite', 2000, 1, 'Doğu'],
        [47, null, 3, 'Suite', 4000, 3, 'Doğu'],
        [48, null, 6, 'Family Room', 4000, 2, 'Batı'],
        [49, null, 3, 'Family Room', 2000, 1, 'Güney'],
        [50, null, 2, 'Deluxe', 2000, 5, 'Güney'],
        [51, null, 2, 'Deluxe', 500, 1, 'Güney'],
        [52, null, 4, 'Suite', 1000, 1, 'Güney'],
        [53, null, 4, 'Family Room', 1000, 4, 'Batı'],
        [54, null, 3, 'Deluxe', 500, 4, 'Güney'],
        [55, null, 3, 'Normal', 15000, 3, 'Batı'],
        [56, null, 1, 'Deluxe', 500, 4, 'Kuzey'],
        [57, null, 3, 'Normal', 500, 5, 'Kuzey'],
        [58, null, 6, 'King Suite', 1000, 1, 'Doğu'],
        [59, null, 5, 'Suite', 750, 1, 'Batı'],
        [60, null, 5, 'Ultra Deluxe', 1000, 5, 'Batı'],
        [61, null, 4, 'King Suite', 15000, 2, 'Kuzey'],
        [62, null, 4, 'Suite', 15000, 3, 'Doğu'],
        [63, null, 5, 'Family Room', 15000, 3, 'Kuzey'],
        [64, null, 2, 'Normal', 15000, 4, 'Doğu'],
        [65, null, 1, 'Family Room', 500, 4, 'Güney'],
        [66, null, 5, 'Deluxe', 500, 1, 'Batı'],
        [67, null, 5, 'Normal', 750, 1, 'Batı'],
        [68, null, 1, 'Deluxe', 4000, 3, 'Batı'],
        [69, null, 4, 'Deluxe', 15000, 4, 'Kuzey'],
        [70, null, 3, 'Suite', 15000, 1, 'Kuzey'],
        [71, null, 6, 'Normal', 500, 1, 'Batı'],
        [72, null, 3, 'King Suite', 4000, 4, 'Batı'],
        [73, null, 5, 'King Suite', 500, 1, 'Doğu'],
        [74, null, 3, 'Normal', 4000, 4, 'Güney'],
        [75, null, 1, 'Normal', 4000, 3, 'Kuzey'],
        
    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });


    sql = "INSERT INTO aktivite(aktivite_no, musteri_no, aktivite_baslangic_tarihi, aktivite_bitis_tarihi, aktivite_ismi, ucret) VALUES ?";
    values = [
        [0, null, '1957/01/28', '1957/01/30', 'Dans Gösterisi', 100],
        [1, null, '1959/08/26', '1959/08/27', 'Dans Gösterisi', 1000],
        [2, null, '1987/05/05', '1987/05/08', 'Paintball', 0],
        [3, null, '1997/02/18', '1997/02/21', 'Egzotik Masaj', 0],
        [4, null, '1987/02/07', '1987/02/07', 'Golf', 50],
        [5, null, '1956/04/29', '1956/04/30', 'Dans Gösterisi', 500],
        [6, null, '1970/03/30', '1970/04/04', 'Diving Yarismasi', 0],
        [7, null, '1982/08/30', '1982/08/30', 'Golf', 250],
        [8, null, '2002/08/02', '2002/08/04', 'Su Topu', 100],
        [9, null, '1959/01/20', '1959/01/23', 'Dans Gösterisi', 1000]
         
    ]
    
    con.query(sql, [values], function (err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
});