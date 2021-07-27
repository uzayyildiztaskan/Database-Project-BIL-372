
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
});