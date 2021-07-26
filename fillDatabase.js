
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
});