import mysql.connector
import random

con = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="1234",
    database="hoteldb"
)

mycursor = con.cursor()

sql = "INSERT IGNORE INTO musteri(musteri_no, musteri_tipi) VALUES (%s, %s)"
valuesMusteri = [
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
]

mycursor.executemany(sql, valuesMusteri)

sql = "INSERT IGNORE INTO bireysel_musteri(musteri_no, rezervasyon_no, oda_no, kimlik_no, isim, soyisim, dogum_tarihi, yas, mail_adresi, kan_grubu, adres, telefon_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

valuesBireyselMusteri = [
    [1, None, None, 769, 'Yasin', 'King', '1976/8/8', 44, 'Yasin@gmail.com',
     '0 rh-', '81 Seaton Place Northwest Washington DC 20001', '15122815673'],
    [2, None, None, 248, 'Ellis', 'Holt', '2003/10/27', 17, 'Ellis@gmail.com',
     'A rh-', '5114 Greentree Drive Nashville TN 37211', '17143863667'],
    [6, None, None, 128, 'Antonia', 'Norris', '2007/10/21', 13, 'Antonia@gmail.com',
     'A rh-', '132 Laurel Green Court Savannah GA 31419', '13168473939'],
    [8, None, None, 213, 'Charlotte', 'Carrillo', '1946/3/29', 74, 'Charlotte@gmail.com',
     'B rh+', '22572 Toreador Drive Salinas CA 93908', '13171267357'],
    [10, None, None, 47, 'Maxwell', 'Solis', '2016/6/12', 4, 'Maxwell@gmail.com',
     'AB rh+', '23 Sable Run Lane Methuen MA 01844', '13122243916'],
    [11, None, None, 717, 'Farhan', 'Lovell', '1972/2/6', 48, 'Farhan@gmail.com',
     'A rh-', '74 Springfield Street B Agawam MA 01001', '18143918845'],
    [14, None, None, 324, 'Allen', 'Wagner', '1959/5/14', 61, 'Allen@gmail.com',
     'B rh-', '8398 West Denton Lane Glendale AZ 85305', '19157254858'],
    [18, None, None, 550, 'Omar', 'Stanley', '1985/4/2', 35, 'Omar@gmail.com',
     'AB rh+', '6657 West Rose Garden Lane Glendale AZ 85308', '17133102757'],
    [19, None, None, 567, 'Joel', 'Griffin', '1958/1/16', 62, 'Joel@gmail.com',
     '0 rh-', '1903 Bashford Manor Lane Louisville KY 40218', '17119138275'],
    [21, None, None, 641, 'Charles', 'King', '1947/11/15', 73, 'Charles@gmail.com',
     'B rh+', '8800 Cordell Circle #APT 000003 Anchorage AK 99502', '18109599025'],
    [24, None, None, 244, 'Harley', 'Hunt', '1945/4/17', 75, 'Harley@gmail.com',
     'A rh+', '1513 Cathy Street Savannah GA 31415', '13182865283'],
    [26, None, None, 185, 'Caitlyn', 'Griffin', '1951/2/3', 69, 'Caitlyn@gmail.com',
     'AB rh+', '716 Waller Road Brentwood TN 37027', '17140785056'],
    [28, None, None, 233, 'Clayton', 'Wagner', '2007/4/3', 13, 'Clayton@gmail.com',
     'A rh+', '165 Saint John Street Manchester CT 06040', '18152766625'],
    [29, None, None, 109, 'Clayton', 'Ortiz', '1955/11/28', 65, 'Clayton@gmail.com',
     '0 rh-', '913 Fallview Trail Nashville TN 37211', '19118519747'],
    [30, None, None, 373, 'Conor', 'Reid', '1992/5/20', 28, 'Conor@gmail.com',
     'B rh-', '270 Chrissy\'s Court VT 05443', '18177429620'],
    [33, None, None, 28, 'Jimmy', 'Gomez', '1951/6/17', 69, 'Jimmy@gmail.com',
     'A rh-', '1347 Blackwalnut Court Annapolis MD 21403', '17129040063'],
    [34, None, None, 106, 'Harley', 'Watson', '2017/11/29', 3, 'Harley@gmail.com',
     'A rh-', '7431 Candace Way #1 Louisville KY 40214', '17125141290'],
    [35, None, None, 495, 'Connor', 'Shelton', '1942/8/26', 78, 'Connor@gmail.com',
     'B rh+', '21950 Arnold Center Road Carson CA 90810', '19182519159'],
    [37, None, None, 615, 'Roman', 'Howarth', '1971/7/16', 49, 'Roman@gmail.com',
     '0 rh-', '1649 Timberridge Court Fayetteville AR 72704', '17152479654'],
    [39, None, None, 62, 'Zakariya', 'Graham', '1995/3/4', 25, 'Zakariya@gmail.com',
     'AB rh+', '109 Summit Street Burlington VT 05401', '13177445747'],
    [41, None, None, 692, 'Casey', 'Mccarthy', '1970/1/23', 50, 'Casey@gmail.com',
     'B rh+', '5108 Franklin Street Savannah GA 31405', '18110362118'],
    [43, None, None, 629, 'Roman', 'Olson', '1979/7/28', 41, 'Roman@gmail.com',
     'AB rh+', '5461 West Shades Valley Drive Montgomery AL 36108', '17157122873'],
    [46, None, None, 293, 'Leonard', 'Howarth', '2016/1/4', 4, 'Leonard@gmail.com',
     'B rh-', '87 Horseshoe Drive West Windsor VT 05037', '19159844899'],
    [47, None, None, 660, 'Dale', 'Fernandez', '1976/4/20', 44, 'Dale@gmail.com',
     'A rh-', '6231 North 67th Avenue #241 Glendale AZ 85301', '17138073047'],
    [49, None, None, 364, 'Isobelle', 'Mccoy', '2018/1/2', 2, 'Isobelle@gmail.com',
     'B rh+', '125 John Street Santa Cruz CA 95060', '13110421873'],
    [50, None, None, 505, 'Dale', 'Haynes', '1952/2/25', 68, 'Dale@gmail.com',
     'A rh+', '60 Desousa Drive Manchester CT 06040', '13135885953']
]

mycursor.executemany(sql, valuesBireyselMusteri)

sql = "INSERT IGNORE INTO kurumsal_musteri(musteri_no, kurum_ismi, kurum_adresi, kurum_tipi, kurumsal_telefon, kurumsal_mail) VALUES (%s, %s, %s, %s, %s, %s)"
valuesKurumsalMusteri = [
    [3, 'Barton, Watsica and Hills', '2409 Research Boulevard Fort Collins CO 80526',
     'Vakif', '18102553728', 'bartonwh@it.com'],
    [4, 'Kling, Roberts and Corwin', '210 Lacross Lane Westmore VT 05860',
     'Vakif', '13116791374', 'klingrcorwin@it.com'],
    [5, 'Bruen, Harber and Bosco', '5114 Greentree Drive Nashville TN 37211',
     'Ozel', '17197877326', 'bruenhbosco@it.com'],
    [7, 'Littel, Altenwerth and Fahey', '10826 Pointe Royal Drive Bakersfield CA 93311',
     'Ozel', '19144830386', 'littelafahey@it.com'],
    [9, 'West, Volkman and Blanda', '8398 West Denton Lane Glendale AZ 85305',
     'Vakif', '13101759336', 'westvblanda@it.com'],
    [12, 'Weber - Fay', '802 Madison Street Northwest Washington DC 20011',
     'Vakif', '13160181007', 'weber-fay@it.com'],
    [13, 'Ankunding - Swaniawski', '1 Kempf Drive Easton MA 02375',
     'Ozel', '19163615580', 'ankunding-swaniawski@it.com'],
    [15, 'Reynolds, Koss and Langworth', '4695 East Huntsville Road Fayetteville AR 72701',
     'Ticari', '17158780201', 'reynoldskworth@it.com'],
    [16, 'Osinski, Gleason and Gerlach', '416 McIver Street Nashville TN 37211',
     'Ticari', '17192131036', 'osinskigerlach@it.com'],
    [17, 'Schaden, Bergstrom and Williamson', '74 Ranch Drive Montgomery AL 36109',
     'Ozel', '19112959404', 'schadenbw@it.com'],
    [20, 'Vandervort - Wisozk', '3466 Southview Avenue Montgomery AL 36111',
     'Ozel', '19194504118', 'vandervort-wisozk@it.com'],
    [22, 'Kassulke - Hills', '23 Sable Run Lane Methuen MA 01844',
     'Vakif', '19116372529', 'kassulke-hills@it.com'],
    [23, 'Ziemann Group', '8505 Waters Avenue #66 Savannah GA 31406',
     'Vakif', '13155182607', 'ziemanngroup@it.com'],
    [25, 'Feest LLC', '1508 Massachusetts Avenue Southeast Washington DC 20003',
     'Ozel', '18110795411', 'feestllc@it.com'],
    [27, 'Thiel, Nolan and Zieme', '491 Arabian Way Grand Junction CO 81504',
     'Ticari', '13135577699', 'thielnzieme@it.com'],
    [31, 'O\'Keefe, Auer and Hegmann', '600 West 19th Avenue APT B Anchorage AK 99503',
     'Vakif', '13161120962', 'okeefehegmann@it.com'],
    [32, 'Waters and Sons', '1208 Elkader Court North Nashville TN 37013',
     'Ticari', '13148025954', 'watersandsons@it.com'],
    [36, 'Ondricka and Senger', '3162 Martin Luther King Junior Boulevard #2 Fayetteville AR 72704',
     'Ticari', '17180615699', 'ondrickasenger@it.com'],
    [38, 'Torphy Group', '308 Woodleaf Court Glen Burnie MD 21061',
     'Ticari', '18141797569', 'torphygroup@it.com'],
    [40, 'Brakus LLC', '5906 Milton Avenue Deale MD 20751',
     'Ticari', '17117384513', 'brakusllc@it.com'],
    [42, 'Beier Inc', '49548 Road 200 O\'Neals CA 93645',
     'Vakif', '15118944869', 'beierinc@it.com'],
    [44, 'Becker, Smitham and Rodriguez', '74 Springfield Street B Agawam MA 01001',
     'Ozel', '18191658713', 'beckersr@it.com'],
    [45, 'Littel, Barton and Aufderhar', '4 Old Colony Way Yarmouth MA 02664',
     'Ozel', '18115731125', 'littelba@it.com'],
    [48, 'Reilly and Sons', '310 Timrod Road Manchester CT 06040',
     'Ozel', '13128281008', 'reillyandsons@it.com']
]

mycursor.executemany(sql, valuesKurumsalMusteri)

sql = "INSERT IGNORE INTO rezervasyon(rezervasyon_no, baslangic_tarihi, bitis_tarihi, fiyat) VALUES (%s, %s, %s, %s)"
valuesRezervasyon = [
    [543, '1982/12/2', '1982/12/8', 3690],
    [532, '2007/9/15', '2007/9/18', 2556],
    [182, '2000/3/5', '2000/3/13', 2139],
    [439, '2012/5/3', '2012/5/5', 521],
    [503, '2009/8/16', '2009/8/22', 870],
    [353, '2005/6/11', '2005/6/15', 1441],
    [433, '2004/2/3', '2004/2/8', 2470],
    [79, '2008/7/8', '2008/7/15', 4143],
    [177, '2015/10/13', '2015/10/19', 1160],
    [53, '2018/2/22', '2018/2/25', 3318],
    [997, '1983/10/30', '1983/11/5', 2985],
    [502, '1983/10/12', '1983/10/18', 4272],
    [782, '2013/5/28', '2013/6/3', 1578],
    [440, '1983/12/21', '1983/12/26', 814],
    [236, '2019/5/20', '2019/5/28', 543],
    [179, '2010/1/17', '2010/1/19', 2787],
    [379, '1986/3/8', '1986/3/15', 2852],
    [381, '1995/5/27', '1995/6/1', 2428],
    [936, '2020/11/12', '2020/11/14', 1920],
    [407, '1984/10/10', '1984/10/13', 3801],
    [278, '1980/8/10', '1980/8/13', 2362],
    [469, '1993/12/30', '1994/1/7', 2870],
    [411, '1990/8/15', '1990/8/20', 3876],
    [89, '2009/1/22', '2009/1/29', 3456],
    [519, '1990/12/10', '1990/12/17', 1310],
    [347, '1985/3/30', '1985/3/7', 1020],
    [553, '2010/2/16', '2010/2/20', 2384],
    [438, '2000/2/14', '2000/2/18', 1144],
    [377, '2018/6/27', '2018/7/4', 1912],
    [27, '1993/10/4', '1993/10/7', 1850],
    [958, '1993/11/10', '1993/11/12', 1290],
    [907, '1988/3/7', '1988/3/14', 2892],
    [115, '1985/7/5', '1985/7/7', 2280],
    [456, '1981/11/22', '1981/11/29', 2846],
    [310, '1989/8/11', '1989/8/18', 1608]
]

mycursor.executemany(sql, valuesRezervasyon)

sql = "INSERT IGNORE INTO tesis(tesis_no, aktivite_no, kat, musteri_kapasitesi, personel_kapasitesi, faaliyet_baslangic_saati, faaliyet_bitis_saati, tesis_tipi, aktif_personel_sayisi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
valuesTesis = [
    [1, None, 2, 75, 10, "08:30", "11:30", "Breakfast Saloon", 6],
    [2, None, 1, 30, 5, "12:30", "18:30", "Game Saloon", 4],
    [3, None, 0, 100, 10, "08:30", "23:30", "Pool", 6],
    [4, None, 2, 40, 4, "19:00", "02:00", "Bar", 4],
    [5, None, 0, 44, 3, "08:30", "22:30", "Football Pitch", 1],
    [6, None, 2, 20, 10, "14:00", "18:00", "Massage Spa", 9],
    [7, None, 1, 50, 1, "20:30", "23:30", "Movie Theater", 1],
    [8, None, 3, 80, 20, "22:30", "03:30", "Disco", 16],
    [9, None, 0, 30, 5, "09:00", "17:00", "Golf Pitch", 5],
    [10, None, 3, 100, 30, "18:30", "21:30", "Diner Saloon", 27]
]

mycursor.executemany(sql, valuesTesis)

sql = "INSERT IGNORE INTO ticari_tesis(mulk_no, kat, kira, tip, vergi_no, kiralayan, sozlesme_baslangic_tarihi, sozlesme_bitis_tarihi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
valuesTicariTesis = [
    [1, 2, 3000, 'Conferance Room', 60069468,
     "Eco Focus", "2021/04/15", "2021/04/19"],
    [2, 0, 5000, 'Market', 24655609,
     "Migros Market", "2017/08/01", "2023/08/01"],
    [3, 2, 3000, 'Conferance Room', 41925201,
     "Inspire Fitness Co", "2016/01/22", "2016/01/24"],
    [4, 0, 8000, 'Market', 21116262,
     "Migros Market", "2019/03/1", "2025/03/1"],
    [5, 0, 8000, 'Market', 35309419, "A101", "2021/01/01", "2027/01/01"]
]

mycursor.executemany(sql, valuesTicariTesis)

sql = "INSERT IGNORE INTO personel(personel_no, yonetici_no, tesis_no, kimlik_no, isim, soyisim, dogum_tarihi, yas, telefon_no, adres, mail_adresi, kan_grubu, maas, gorev, departman, calisma_saati_baslangic, calisma_saati_bitis, izin_gunleri) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
valuesPersonel = [
    [0, None, None, 729125322, 'Harley', 'Briggs', '1958/09/23', 62, '13108165429', '4 Old Colony Way Yarmouth MA 02664',
     'Harley@gmail.com', '0 rh-', 7500, 'Hizmet Personeli', 'Spa', '20:00', '08:00', 'Cumartesi-Pazar'],
    [1, None, None, 531264693, 'Connor', 'Briggs', '1972/02/26', 48, '19128884766', '310 Timrod Road Manchester CT 06040',
     'Connor@gmail.com', 'AB rh-', 10000, 'Yönetici', 'Disco', '20:00', '08:00', 'Pazartesi-Cuma'],
    [2, None, None, 110648952, 'Amir', 'Shelton', '1971/09/02', 49, '17175209890', '8821 West Myrtle Avenue Glendale AZ 85305',
     'Amir@gmail.com', '0 rh-', 7500, 'Sekreter', 'Spa', '20:00', '08:00', 'Pazartesi-Perşembe'],
    [3, None, None, 580277414, 'Ellie', 'Edwards', '1944/02/27', 76, '19160455660', '5108 Franklin Street Savannah GA 31405',
     'Ellie@gmail.com', 'B rh+', 10000, 'Sekreter', 'Disco', '20:00', '08:00', 'Pazartesi-Cuma'],
    [4, None, None, 296972674, 'Kieron', 'Hunt', '1952/10/24', 68, '15167618280', '8376 Albacore Drive Pasadena MD 21122',
     'Kieron@gmail.com', 'AB rh+', 2800, 'Sekreter', 'Spor Salonu', '08:00', '20:00', 'Cumartesi-Pazar'],
    [5, None, None, 192782567, 'Farhan', 'Moreno', '1949/04/13', 71, '19161959041', '1770 Colony Way Fayetteville AR 72704',
        'Farhan@gmail.com', 'AB rh-', 2800, 'Sekreter', 'Golf', '09:00', '17:00', 'Pazar-Pazartesi'],
    [6, None, None, 616626592, 'Yasin', 'Meyer', '2006/12/07', 14, '19178909397', '109 Summit Street Burlington VT 05401',
     'Yasin@gmail.com', '0 rh+', 10000, 'Garson', 'Havuz', '09:00', '17:00', 'Pazartesi-Cuma'],
    [7, None, None, 560588915, 'Zakariya', 'Meyer', '1976/01/01', 44, '17152343579', '165 Saint John Street Manchester CT 06040',
     'Zakariya@gmail.com', 'AB rh-', 7500, 'Sekreter', 'Spa', '08:00', '20:00', 'Pazar-Pazartesi'],
    [8, None, None, 504847333, 'Kieron', 'Reid', '1942/05/12', 78, '13198280368', '5114 Greentree Drive Nashville TN 37211',
     'Kieron@gmail.com', 'A rh-', 5000, 'Yönetici', 'Disco', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [9, None, None, 697003440, 'Roman', 'Mccoy', '1979/01/09', 41, '18176849148', '132 Laurel Green Court Savannah GA 31419',
     'Roman@gmail.com', 'AB rh+', 10000, 'Hizmet Personeli', 'İdari', '09:00', '17:00', 'Pazartesi-Cuma'],
    [10, None, None, 832151819, 'Tristan', 'Carrillo1', '1991/11/09', 29, '15160775515', '5811 Crossings Boulevard Nashville TN 37013',
     'Tristan@gmail.com', 'B rh-', 10000, 'Yönetici', 'İdari', '08:00', '20:00', 'Cumartesi-Pazar'],
    [11, None, None, 698513933, 'Ellie', 'Phillips', '1995/07/04', 25, '15126686680', '519 West 75th Avenue #APT 000003 Anchorage AK 99518',
     'Ellie@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20:00', '08:00', 'Pazar-Pazartesi'],
    [12, None, None, 116807723, 'Jimmy', 'White', '1969/06/27', 51, '19126123165', '1407 Walden Court Crofton MD 21114',
     'Jimmy@gmail.com', 'B rh+', 5000, 'Muhasebeci', 'Disco', '09:00', '17:00', 'Cumartesi-Pazar'],
    [13, None, None, 748752853, 'Zakariya', 'Rodriguez', '1940/01/05', 80, '19160028698', '210 Lacross Lane Westmore VT 05860',
     'Zakariya@gmail.com', 'A rh-', 10000, 'Sekreter', 'Spa', '20:00', '08:00', 'Cumartesi-Pazar'],
    [14, None, None, 643186495, 'Anabelle', 'Mullins', '1993/09/25', 27, '18190245594', '150 Carter Street Manchester CT 06040',
     'Anabelle@gmail.com', '0 rh+', 3500, 'Hizmet Personeli', 'Spa', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [15, None, None, 509003644, 'Allen', 'Mccoy', '1955/06/22', 65, '18167980382', '81 Seaton Place Northwest Washington DC 20001',
     'Allen@gmail.com', '0 rh+', 10000, 'Yönetici', 'Spor Salonu', '20:00', '08:00', 'Pazartesi-Cuma'],
    [16, None, None, 252578980, 'Charles', 'Mccarthy', '1940/04/24', 80, '18178033897', '1364 Capri Drive Panama City FL 32405',
     'Charles@gmail.com', '0 rh-', 2800, 'Hizmet Personeli', 'Disco', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [17, None, None, 294881759, 'Allanah', 'Carrillo1', '2010/07/16', 10, '19180437403', '130 Old Route 103 Chester VT 05143',
     'Allanah@gmail.com', '0 rh-', 10000, 'Sekreter', 'Disco', '20:00', '08:00', 'Pazartesi-Cuma'],
    [18, None, None, 262866012, 'Antonia', 'Mccoy', '1995/07/13', 25, '19117444795', '1508 Massachusetts Avenue Southeast Washington DC 20003',
     'Antonia@gmail.com', 'A rh-', 10000, 'Hizmet Personeli', 'Golf', '08:00', '20:00', 'Cumartesi-Pazar'],
    [19, None, None, 628937564, 'Connor', 'Griffin', '1949/05/11', 71, '19163533345', '8800 Cordell Circle #APT 000003 Anchorage AK 99502',
     'Connor@gmail.com', 'B rh+', 3500, 'Garson', 'İdari', '09:00', '17:00', 'Cumartesi-Pazar'],
    [20, None, None, 427889126, 'Allen', 'Griffin', '1968/10/21', 52, '19125292925', '5461 West Shades Valley Drive Montgomery AL 36108',
     'Allen@gmail.com', 'B rh+', 5000, 'Sekreter', 'Havuz', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [21, None, None, 992165861, 'Charlotte', 'Shelton', '1984/07/23', 36, '15184552956', '4 Old Colony Way Yarmouth MA 02664',
     'Charlotte@gmail.com', 'A rh-', 10000, 'Garson', 'Mutfak', '20:00', '08:00', 'Pazartesi-Perşembe'],
    [22, None, None, 362179889, 'Caitlyn', 'Haynes', '2008/08/05', 12, '17152190173', '74 Ranch Drive Montgomery AL 36109',
     'Caitlyn@gmail.com', 'AB rh-', 5000, 'Hizmet Personeli', 'İdari', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [23, None, None, 826760466, 'Allanah', 'Olson', '1951/06/11', 69, '15171991394', '18 Densmore Drive Essex VT 05452',
     'Allanah@gmail.com', 'A rh+', 2800, 'Yönetici', 'Golf', '20:00', '08:00', 'Cumartesi-Pazar'],
    [24, None, None, 634953165, 'Leonard', 'Laing', '1993/03/17', 27, '13106770779', '8821 West Myrtle Avenue Glendale AZ 85305',
     'Leonard@gmail.com', '0 rh+', 10000, 'Muhasebeci', 'Disco', '08:00', '20:00', 'Cumartesi-Pazar'],
    [25, None, None, 22988038, 'Farhan', 'Carrillo1', '1975/10/16', 45, '15161565664', '232 Maine Avenue Panama City FL 32401',
     'Farhan@gmail.com', 'B rh+', 5000, 'Hizmet Personeli', 'Mutfak', '20:00', '08:00', 'Pazartesi-Perşembe'],
    [26, None, None, 368716417, 'Amir', 'Fernandez', '2019/10/15', 1, '19162422359', '210 Lacross Lane Westmore VT 05860',
     'Amir@gmail.com', '0 rh-', 7500, 'Yönetici', 'Golf', '09:00', '17:00', 'Pazartesi-Perşembe'],
    [27, None, None, 754470286, 'Kieron', 'White', '1972/12/03', 48, '19125561305', '913 Fallview Trail Nashville TN 37211',
     'Kieron@gmail.com', '0 rh-', 3500, 'Sekreter', 'Spor Salonu', '08:00', '20:00', 'Pazartesi-Cuma'],
    [28, None, None, 611845998, 'Kieron', 'Shelton', '1990/06/13', 30, '17108941379', '1508 Massachusetts Avenue Southeast Washington DC 20003',
     'Kieron@gmail.com', 'A rh-', 2800, 'Hizmet Personeli', 'Spa', '20:00', '08:00', 'Pazar-Pazartesi'],
    [29, None, None, 884901187, 'Farhan', 'Edwards', '1953/02/15', 67, '18138491711', '232 Maine Avenue Panama City FL 32401', 'Farhan@gmail.com', '0 rh+', 10000, 'Sekreter', 'İdari', '20:00', '08:00', 'Cumartesi-Pazar']]

mycursor.executemany(sql, valuesPersonel)

sql = "INSERT IGNORE INTO oda(oda_no, rezervasyon_no, yatak_sayisi, oda_tipi, fiyat, kat, cephe) VALUES (%s, %s, %s, %s, %s, %s, %s)"
valuesOda = [
    [1, None, 1, 'Normal', 4000, 1, 'Doğu'],
    [2, None, 6, 'Ultra Deluxe', 750, 3, 'Doğu'],
    [3, None, 4, 'Family Room', 15000, 4, 'Kuzey'],
    [4, None, 6, 'Ultra Deluxe', 500, 2, 'Kuzey'],
    [5, None, 1, 'Suite', 2000, 3, 'Kuzey'],
    [6, None, 3, 'Deluxe', 15000, 1, 'Güney'],
    [7, None, 3, 'Normal', 1000, 1, 'Güney'],
    [8, None, 3, 'Ultra Deluxe', 4000, 4, 'Doğu'],
    [9, None, 1, 'Deluxe', 1000, 2, 'Güney'],
    [10, None, 5, 'Ultra Deluxe', 4000, 1, 'Güney'],
    [11, None, 2, 'Normal', 15000, 3, 'Güney'],
    [12, None, 4, 'Normal', 2000, 4, 'Kuzey'],
    [13, None, 5, 'Ultra Deluxe', 1000, 4, 'Güney'],
    [14, None, 1, 'Deluxe', 2000, 2, 'Güney'],
    [15, None, 2, 'Normal', 750, 3, 'Kuzey'],
    [16, None, 5, 'King Suite', 4000, 3, 'Güney'],
    [17, None, 2, 'King Suite', 15000, 5, 'Doğu'],
    [18, None, 2, 'Suite', 15000, 1, 'Kuzey'],
    [19, None, 2, 'King Suite', 2000, 5, 'Batı'],
    [20, None, 1, 'Deluxe', 15000, 4, 'Kuzey'],
    [21, None, 1, 'Normal', 4000, 2, 'Güney'],
    [22, None, 5, 'Suite', 4000, 5, 'Kuzey'],
    [23, None, 2, 'Normal', 750, 5, 'Batı'],
    [24, None, 4, 'Deluxe', 2000, 3, 'Batı'],
    [25, None, 6, 'King Suite', 2000, 2, 'Doğu'],
    [26, None, 4, 'Family Room', 1000, 4, 'Doğu'],
    [27, None, 3, 'King Suite', 750, 1, 'Batı'],
    [28, None, 2, 'Suite', 4000, 5, 'Kuzey'],
    [29, None, 1, 'Family Room', 750, 3, 'Batı'],
    [30, None, 2, 'Normal', 750, 4, 'Batı'],
    [31, None, 2, 'Deluxe', 500, 3, 'Doğu'],
    [32, None, 3, 'Suite', 750, 4, 'Batı'],
    [33, None, 4, 'Suite', 2000, 5, 'Kuzey'],
    [34, None, 1, 'Normal', 1000, 2, 'Kuzey'],
    [35, None, 6, 'King Suite', 15000, 3, 'Doğu'],
    [36, None, 5, 'King Suite', 15000, 4, 'Doğu'],
    [37, None, 2, 'Family Room', 2000, 2, 'Güney'],
    [38, None, 3, 'Deluxe', 2000, 1, 'Batı'],
    [39, None, 2, 'Ultra Deluxe', 1000, 3, 'Güney'],
    [40, None, 3, 'Normal', 4000, 4, 'Batı'],
    [41, None, 2, 'Suite', 500, 4, 'Güney'],
    [42, None, 6, 'King Suite', 500, 5, 'Batı'],
    [43, None, 5, 'Ultra Deluxe', 4000, 2, 'Batı'],
    [44, None, 6, 'Family Room', 1000, 4, 'Güney'],
    [45, None, 4, 'Ultra Deluxe', 1000, 5, 'Batı'],
    [46, None, 2, 'King Suite', 2000, 1, 'Doğu'],
    [47, None, 3, 'Suite', 4000, 3, 'Doğu'],
    [48, None, 6, 'Family Room', 4000, 2, 'Batı'],
    [49, None, 3, 'Family Room', 2000, 1, 'Güney'],
    [50, None, 2, 'Deluxe', 2000, 5, 'Güney'],
    [51, None, 2, 'Deluxe', 500, 1, 'Güney'],
    [52, None, 4, 'Suite', 1000, 1, 'Güney'],
    [53, None, 4, 'Family Room', 1000, 4, 'Batı'],
    [54, None, 3, 'Deluxe', 500, 4, 'Güney'],
    [55, None, 3, 'Normal', 15000, 3, 'Batı'],
    [56, None, 1, 'Deluxe', 500, 4, 'Kuzey'],
    [57, None, 3, 'Normal', 500, 5, 'Kuzey'],
    [58, None, 6, 'King Suite', 1000, 1, 'Doğu'],
    [59, None, 5, 'Suite', 750, 1, 'Batı'],
    [60, None, 5, 'Ultra Deluxe', 1000, 5, 'Batı'],
    [61, None, 4, 'King Suite', 15000, 2, 'Kuzey'],
    [62, None, 4, 'Suite', 15000, 3, 'Doğu'],
    [63, None, 5, 'Family Room', 15000, 3, 'Kuzey'],
    [64, None, 2, 'Normal', 15000, 4, 'Doğu'],
    [65, None, 1, 'Family Room', 500, 4, 'Güney'],
    [66, None, 5, 'Deluxe', 500, 1, 'Batı'],
    [67, None, 5, 'Normal', 750, 1, 'Batı'],
    [68, None, 1, 'Deluxe', 4000, 3, 'Batı'],
    [69, None, 4, 'Deluxe', 15000, 4, 'Kuzey'],
    [70, None, 3, 'Suite', 15000, 1, 'Kuzey'],
    [71, None, 6, 'Normal', 500, 1, 'Batı'],
    [72, None, 3, 'King Suite', 4000, 4, 'Batı'],
    [73, None, 5, 'King Suite', 500, 1, 'Doğu'],
    [74, None, 3, 'Normal', 4000, 4, 'Güney'],
    [75, None, 1, 'Normal', 4000, 3, 'Kuzey'],
]

mycursor.executemany(sql, valuesOda)

sql = "INSERT IGNORE INTO aktivite(aktivite_no, musteri_no, aktivite_baslangic_tarihi, aktivite_bitis_tarihi, aktivite_ismi, ucret) VALUES (%s, %s, %s, %s, %s, %s)"
valuesAktivite = [
    [0, None, '1957/01/28', '1957/01/30', 'Dans Gösterisi', 100],
    [1, None, '1959/08/26', '1959/08/27', 'Dans Gösterisi', 1000],
    [2, None, '1987/05/05', '1987/05/08', 'Paintball', 0],
    [3, None, '1997/02/18', '1997/02/21', 'Egzotik Masaj', 0],
    [4, None, '1987/02/07', '1987/02/07', 'Golf', 50],
    [5, None, '1956/04/29', '1956/04/30', 'Dans Gösterisi', 500],
    [6, None, '1970/03/30', '1970/04/04', 'Diving Yarismasi', 0],
    [7, None, '1982/08/30', '1982/08/30', 'Golf', 250],
    [8, None, '2002/08/02', '2002/08/04', 'Su Topu', 100],
    [9, None, '1959/01/20', '1959/01/23', 'Dans Gösterisi', 1000]
]

mycursor.executemany(sql, valuesAktivite)

resAmount = {543: 1,  532: 5,  182: 4,  439: 5,  503: 5,  353: 1,  433: 2,  79: 3,  177: 3,  53: 4,  997: 5,  502: 3,  782: 7, 440: 6,  236: 6,  179: 4,  379: 4,
             381: 4,  936: 3,  407: 1,  278: 4,  469: 7,  411: 7,  89: 3,  519: 3,  347: 6,  553: 6, 438: 2,  377: 1,  27: 1,  958: 2,  907: 6,  115: 3,  456: 4,  310: 2}

resCustomer = {}

for i in range(len(valuesMusteri)):

    if(valuesMusteri[i][1] == 1):

        roomNumber = random.randint(1, 75)
        randomIndex = random.randint(0, len(valuesRezervasyon)-1)
        rezNumber = valuesRezervasyon[randomIndex][0]

        while(resAmount[rezNumber] == 0):

            randomIndex = random.randint(0, len(valuesRezervasyon)-1)
            rezNumber = valuesRezervasyon[randomIndex][0]

        resAmount[rezNumber] = resAmount[rezNumber] - 1
        resCustomer.update({valuesMusteri[i][0]: rezNumber})

        sql = "UPDATE bireysel_musteri SET oda_no = " + str(roomNumber) + \
            ", rezervasyon_no = " + str(rezNumber) + \
            " WHERE musteri_no = " + str(valuesMusteri[i][0])

        mycursor.execute(sql)

for i in range(1, 11):

    aktiviteNo = random.randint(0, 9)

    sql = "UPDATE tesis SET aktivite_no = " + \
        str(aktiviteNo) + " WHERE tesis_no = " + str(i)

    mycursor.execute(sql)

for i in range(30):

    tesisNo = random.randint(1, 10)
    yoneticiNo = random.randint(0, 29)

    while (yoneticiNo == i):
        yoneticiNo = random.randint(0, 29)

    sql = "UPDATE personel SET tesis_no = " + \
        str(tesisNo) + " ,yonetici_no = " + \
        str(yoneticiNo) + " WHERE personel_no = " + str(i)

    mycursor.execute(sql)

sql = "UPDATE aktivite SET musteri_no = 2 WHERE aktivite_no IN (0,1,5,6,8,9)"

mycursor.execute(sql)

sql = "SELECT oda_no, rezervasyon_no FROM bireysel_musteri"

mycursor.execute(sql)

result = mycursor.fetchall()

for i in result:

    strResult = str(i)

    roomNumber = strResult[1: strResult.index(',')]

    rezNumber = strResult[strResult.index(',') + 2: strResult.index(')')]

    sql = "UPDATE oda SET rezervasyon_no = " + \
        rezNumber + " WHERE oda_no = " + roomNumber

    mycursor.execute(sql)

sql = "INSERT IGNORE INTO musteri VALUES (%s, %s)"

valuesMusteri = [
    [63, 1],
    [64, 1],
    [65, 1],
    [66, 1],
    [67, 1],
    [68, 1],
    [69, 1],
    [70, 1],
    [71, 1],
    [72, 1],
    [73, 1],
    [74, 1],
    [75, 1],
    [76, 1],
    [77, 1],
    [78, 1],
    [79, 1],
    [80, 1],
    [81, 1],
    [82, 1],
    [83, 1],
    [51, 2],
    [52, 2],
    [53, 2],
    [54, 2],
    [55, 2],
    [56, 2],
    [57, 2],
    [58, 2],
    [59, 2],
    [60, 2],
    [84, 2],
    [85, 2],
    [86, 2],
    [87, 2],
    [88, 2],
    [89, 2],
    [90, 2],
    [91, 2],
    [92, 2],
    [93, 2]
]

mycursor.executemany(sql, valuesMusteri)

sql = "INSERT IGNORE INTO rezervasyon VALUES (%s, %s, %s, %s)"

valuesRezervasyon = [
    [1, "2000/07/12", "2000/07/15",	1000],
    [2,	"2001/03/11", "2001/03/14",	2500],
    [3,	"2001/03/12", "2001/03/14",	2500],
    [4,	"2001/03/11", "2001/03/12",	2000],
    [5, "2000/07/12", "2000/07/15",	1000],
    [1000, '2020/03/13', '2020/03/18', 5500],
    [1001, '2020/08/14', '2020/08,16', 2483],
    [1002, '2020/03/13', '2020/03/18', 4900],
    [1003, '2020/08/14', '2020/08/20', 4532],
    [1004, '2020/08/14', '2020/08/20', 6000],
    [1005, '2020/10/10', '2020/10/15', 7500],
    [1006, '2020/10/5', '2020/10/15', 15000],
    [1007, '2020/10/10', '2020/10/24', 10800],
    [1008, '2020/07/29', '2020/08/16', 9700],
    [1009, '2020/08/14', '2020/08/24', 6800]
]

mycursor.executemany(sql, valuesRezervasyon)

sql = "INSERT IGNORE INTO oda VALUES (%s, %s, %s, %s, %s, %s, %s)"

valuesOda = [
    [76, 1,	2, "Normal", 3000, 1, "Doğu"],
    [77, 5,	3, "Normal", 2000, 1, "Batı"],
    [78, 3,	2, "Deluxe", 1000, 2, "Kuzey"],
    [79, 4,	1, "Deluxe", 1000, 3, "Kuzey"],
    [80, 1,	1, "King Suite", 2000, 2, "Batı"],
    [81, None, 4, "King Suite", 4000, 2, "Güney"],
    [82, 1,	2, "Normal", 3000, 1, "Doğu"],
    [83, None, 4, "King Suite", 4000, 3, "Güney"],
    [84, 2,	1, "Normal", 1000,	3, "Kuzey"],
    [85, 1,	3, "Deluxe", 2000,	2, "Doğu"],
    [90, 1000, 2, 'Ultra Deluxe', 3000, 4, 'Kuzey'],
    [91, 1006, 1, 'Family Room', 2000, 2, 'Güney'],
    [92, 1000, 4, 'Normal', 1000, 4, 'Kuzey'],
    [93, 1007, 3, 'Deluxe', 2000, 3, 'Doğu'],
    [94, 1007, 3, 'Ultra Suite', 1000, 3, 'Güney'],
    [95, 1005, 1, 'Normal', 1000, 4, 'Batı'],
    [96, 1005, 3, 'Family Room', 1500, 2, 'Güney'],
    [97, 1005, 2, 'Normal', 2000, 1, 'Güney'],
    [98, 1008, 4, 'Suite', 10000, 1, 'Batı'],
    [99, 1008, 3, 'Normal', 2000, 2, 'Doğu']
]

mycursor.executemany(sql, valuesOda)

sql = "INSERT IGNORE INTO bireysel_musteri VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

valuesBireyselMusteri = [
    [63, 1, 76,	770, "Ali", "Durmaz", "1982/06/05", 39,
        "ali@gmail.com", "AB rh-", "İstanbul", 12345678901],
    [64, 3,	78,	771, "Ahmet", "Yilmaz", "1982/03/07", 39,
        "ahmet@gmail.com", "0 rh+", "İstanbul", 12345678902],
    [65, 2,	84,	772, "Ali", "Demir", "2001/05/07", 20,
        "ali@gmail.com", "A rh+", "İstanbul", 12345678903],
    [66, 1,	76,	773, "Ali", "Yilmaz", "1990/12/06", 31,
        "ali@gmail.com"	, "AB rh-", "İstanbul", 12345678904],
    [67, 3,	78,	774, "Ahmet", "Yildirim", "2000/07/12",	21,
        "ahmet@gmail.com", "B rh+", "İstanbul", 12345678905],
    [68, 4,	79,	775, "Kerem", "Yilmaz", "2001/03/11", 20,
        "kerem@gmail.com", "A rh+", "İstanbul", 12345678906],
    [69, 1,	80,	776, "Omer", "Simsek", "1973/03/22", 48,
        "omer@gmail.com", "0 rh+", "İstanbul", 12345678907],
    [70, 1000, 90, 111111111, 'Ali', 'Durmuş', '1988/07/12',
        33, 'Ali@gmail.com', '0 rh+', 'Ankara', 123456789],
    [71, 1000, 92, 222222222, 'Mustafa', 'Yetmez', '1992/07/12',
        29, 'mustafa@gmail.com', 'A rh-', 'İstanbul', 777777788],
    [72, 1005, 95, 333333333, 'James', 'Rodriguez', '1988/03/26', 33,
        'james@gmail.com', 'AB rh+', 'Mexico City', 888888887],
    [73, 1005, 97, 444444444, 'Michael', 'Bay', '1970/10/17', 51,
        'Michael@gmail.com', '0 rh-', 'Toronto', 66666666777],
    [74, 1000, 90, 555555555, 'Osman', 'Yılmaz', '2000/07/15', 21,
        'Osman@gmail.com', 'B rh+', 'Konya', 7777777776666],
    [75, 1008, 99, 666666666, 'Selin', 'Arıcıoğlu', '1990/03/29',
        31, 'Selin@gmail.com', 'A rh+', 'Muğla', 555555555],
    [76, 1006, 91, 77777777, 'Suat', 'Keskin', '1976/07/29',
        45, 'Suat@gmail.com', '0 rh-', 'Ankara', 666666665],
    [77, 1007, 93, 88888888, 'Burak', 'İnan', '1985/09/20', 36,
        'Burak@gmail.com', 'A rh+', 'Ankara', 4444444445],
    [78, 1007, 93, 99999999, 'Maria', 'Sharapova', '1998/09/30',
        23, 'Maria@gmail.com', '0 rh-', 'Moskova', 5555555544],
    [79, 1007, 94, 10000000, 'Murat', 'Peker', '1969/03/06', 52,
        'Murat@gmail.com', 'AB rh+', 'Mardin', 33333333344],
    [80, 5,	77,	777, "Mehmet", "Durmaz", "1982/01/22", 39,
        "mehmet@gmail.com", "AB rh-", "İstanbul", 12345678908],
    [81, 5,	77,	778, "Kerem", "Celik", "2001/08/16", 20,
        "kerem@gmail.com", "AB rh-", "İstanbul", 12345678909],
    [82, 5,	77,	779, "Yusuf", "Kara", "1973/08/27",	48,
        "yusuf@gmail.com", "B rh+", "İstanbul", 12345678910],
    [83, 1,	85,	780, "Yusuf", "Demir", "1996/05/29", 25,
        "yusuf@gmail.com", "B rh-", "İstanbul", 12345678911]
]

mycursor.executemany(sql, valuesBireyselMusteri)

sql = "INSERT IGNORE INTO kurumsal_musteri VALUES (%s, %s, %s, %s, %s, %s)"

valuesKurumsalMusteri = [
    [51, "Orbay and Özbir", "İstanbul", "Vakif", 12345680, "kurumsal3@gmail.com"],
    [52, "Erbulak - Durak", "İstanbul", "Ticari", 12345681,	"kurumsal4@gmail.com"],
    [53, "Kahveci - Erkekli", "İstanbul", "Ozel", 12345682, "kurumsal5@gmail.com"],
    [54, "Ozansoy and Sons", "İstanbul", "Vakif", 12345683, "kurumsal6@gmail.com"],
    [55, "Atan and Aykaç", "İstanbul", "Ticari", 12345684, "kurumsal7@gmail.com"],
    [56, "Duygulu and Öztonga", "İstanbul",
        "Vakif", 12345685, "kurumsal8@gmail.com"],
    [57, "Kocabıyık and Sons", "İstanbul", "Ozel", 12345686, "kurumsal9@gmail.com"],
    [58, "Denkel and Sons", "İstanbul", "Ozel", 12345687, "kurumsal10@gmail.com"],
    [59, "Ayverdi Inc", "İstanbul", "Vakif", 12345678, "kurumsal1@gmail.com"],
    [60, "Kunt LLC", "İstanbul", "Ozel", 12345679, "kurumsal2@gmail.com"],
    [84, 'Bim Holding', 'Ankara', 'Ticari', '77777777777', 'bim@gmail.com'],
    [85, 'A101 Holding', 'Ankara', 'Ticari', '88888888888', 'a101@gmail.com'],
    [86, 'Google', 'Los Angeles', 'Ozel', '11111111111111', 'google@gmail.com'],
    [87, 'B Holding', 'İstanbul', 'Vakıf', '2222222222222',  'b@gmail.com'],
    [88, 'Facebook', 'San Francisco', 'Ozel', '3333333333', 'facebook@gmail.com'],
    [89, 'Instagram', 'San Francisco', 'Ozel', '111115555555', 'ig@gmail.com'],
    [90, 'X Holding', 'Chicago', 'Ozel', '444444444444', 'X@gmail.com'],
    [91, 'Tesla Company', 'New York', 'Ozel', '9999999999999', 'tesla@gmail.com'],
    [92, 'Koç Holding', 'İstanbul', 'Vakıf', '5555555555', 'koc@gmail.com'],
    [93, 'Sabancı Holding', 'İstanbul', 'Vakıf',
        '66666666666', 'sabancı@gmail.com']
]

mycursor.executemany(sql, valuesKurumsalMusteri)

sql = "INSERT IGNORE INTO aktivite VALUES (%s, %s, %s, %s, %s, %s)"

valuesAktivite = [
    [10, 53, "2000/07/12", "2000/07/16", "Aktivite1", 2000],
    [11, None, "2001/03/11", "2001/03/14", "Aktivite2",	3000],
    [12, 51, "2001/03/12", "2001/03/18", "Aktivite3", 3500],
    [13, None, "2001/03/11", "2001/03/12", "Aktivite4", 2000],
    [14, 53, "2000/07/12", "2000/07/16", "Aktivite5", 2000],
    [15, None, "1982/01/22", "1982/06/05", "Aktivite6", 3000],
    [16, None, "2001/03/13", "2001/03/14", "Aktivite7", 2000],
    [17, 52, "1973/08/27", "1973/08/29", "Aktivite8", 2000],
    [18, None, "1990/12/09", "1990/12/12", "Aktivite9",	3500],
    [19, 60, "2000/07/16", "2000/07/12", "Aktivite10", 3000],
    [20, None, '2021/08/23', '2021/08/24', 'Sirk', 100],
    [21, None, '2021/06/21', '2021/06/21', 'Havuz Partisi', 0],
    [22, 92, '2021/05/18', '2021/05/22', 'Şirket Toplantısı', 0],
    [23, 85, '2020/07/02', '2020/07/02', 'Golf', 200],
    [24, None, '2021/08/23', '2021/08/24', 'Açıkhava Sineması', 0],
    [25, 87, '2021/05/18', '2021/05/22', 'Çin Yemeği', 150],
    [26, 92, '2020/07/01', '2020/07/02', 'Dans Gösterisi', 300],
    [27, None, '2021/11/12', '2021/11,13', 'Su Topu', 500],
    [28, 89, '2021/11/10', '2021/11/13', 'Deniz Partisi', 0],
    [29, 89, '2021/12/07', '2021/12/09', 'Masaj', 250]
]

mycursor.executemany(sql, valuesAktivite)

sql = "INSERT IGNORE INTO tesis VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

valuesTesis = [
    [11, 10, 2,	50, 10,	"08:30", "12:00", "Type1", 8],
    [12, 11, 1,	100, 20, "11:30", "13:30", "Type2", 5],
    [13, 12, 2,	50, 10, "08:30", "12:00", "Type1", 8],
    [14, 13, 0,	75, 5, "10:30",	"12:00", "Type1", 5],
    [15, 14, 1,	75, 20, "11:30", "14:00", "Type3", 10],
    [16, 15, 0,	100, 10, "12:30", "13:30", "Type3", 10],
    [17, 16, 0,	100, 5,	"10:30", "13:30", "Type1", 5],
    [18, 17, 1,	50, 5, "11:30",	"14:00", "Type3", 10],
    [19, 18, 2,	75, 10, "12:30", "13:30", "Type2", 8],
    [20, 23, 2, 150, 50, '08:00', '12:00', 'Golf Sahası', 35],
    [21, 26, 4, 200, 50, '14:30', '17:30', 'Snack Bar', 10],
    [22, 23, 1, 70, 10, '20:00',  '22:00', 'Tenis Kortu', 10],
    [23, 25, 2, 200, 50, '19:00',  '22:00', 'Yemek Salonu', 20],
    [24, 27, 1, 50, 50, '08:00',  '09:30', 'Voleyball Sahası', 23],
    [25, 26, 4, 500, 50, '14:30', '17:30', 'Mini Disco', 10],
    [26, 26, 1, 150, 50, '15:30', '17:30', 'Futbol Sahası', 20],
    [27, 25, 2, 100, 40, '00:00', '05:00', 'Disko', 20],
    [28, 25, 3, 100, 10, '16:00', '19:00', 'Bilardo Salonu', 5],
    [29, 24, 3, 100, 30, '18:00', '22:00', 'Bowling Salonu', 20],
    [30, 19, 1,	100, 20, "12:30", "14:00", "Type2",	5]
]

mycursor.executemany(sql, valuesTesis)

sql = "INSERT IGNORE INTO personel VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

valuesPersonel = [
    [30, None, 11, 123456789, "Ozan", "Yildirim", "2000/07/12",	21,	234567890, "İstanbul", "test@gmail.com",
        "B rh+", 5000, "Yönetici", "İdari", "08:00", "17:30", "Cumartesi-Pazar"],
    [31, 30, 12, 123456780,	"Deniz", "Yilmaz", "2001/03/11", 20, 234567891, "İstanbul", "test@gmail.com",
        "A rh+", 2000, "Sekreter", "İdari",	"08:00", "17:30", "Pazartesi-Salı"],
    [32, 30, 13, 123456771,	"Ozan", "Simsek", "1973/03/22",	48, 234567892,	"İstanbul", "test@gmail.com",
        "0 rh+", 2000, "Sekreter", "İdari",	"09:00", "17:30", "Pazartesi-Salı"],
    [33, None, 14, 123456762, "Hakan", "Durmaz", "1982/01/22", 39, 234567893, "İstanbul", "test@gmail.com",
        "AB rh-", 1500, "Sekreter", "İdari", "10:00", "20:30", "Cumartesi-Pazar"],
    [34, 33, 12, 123456753,	"Kuzey", "Celik", "2001/08/16",	20,	234567894, "İstanbul", "test@gmail.com",
        "AB rh-", 2500, "Muhasebeci", "İdari", "11:00", "17:30", "Cuma-Cumartesi"],
    [35, 33, 13, 123456744,	"Kuzey", "Demir", "1973/08/27",	48,	234567895, "İstanbul", "test@gmail.com",
        "B rh+", 2500, "Hizmet P.", "Mutfak", "11:00", "17:30", "Cuma-Cumartesi"],
    [36, None, 14, 123456735, "Okan", "Evren", "1996/05/29", 25, 234567896, "İstanbul", "test@gmail.com",
        "B rh-", 3000, "Garson", "Mutfak", "13:00", "20:30", "Cumartesi-Pazar"],
    [38, None, 11, 123456717, "Ozan", "Atalay", "1994/08/27", 27, 234567898, "İstanbul", "test@gmail.com",
        "AB rh-", 5000, "Yönetici", "İdari", "08:00", "17:30", "Cumartesi-Pazar"],
    [37, 38, 15, 123456726,	"Doruk", "Kıraç", "1980/08/16",	41, 234567897, "İstanbul", "test@gmail.com",
     "0 rh+", 3000, "Muhasebeci",	"İdari", "14:00", "20:00", "Pazar-Pazartesi"],
    [39, 38, 15, 123456708,	"Arda", "Kaya", "2000/05/29", 21, 234567899, "İstanbul", "test@gmail.com",
        "AB rh-", 4000, "Garson", "Mutfak", "14:00", "14:30", "Pazar-Pazartesi"],
    [50, 39, 20, 11111111, 'Ali', 'Yılmaz', '1985/07/06', 36, '123456789', 'Ankara',
        'Ali@gmail.com', 'A rH-', 5000, 'Yönetici', 'Mutfak', '09:00', '17:00', 'Cumartesi-Pazar'],
    [51, 50, 20, 22222222, 'Yasin', 'Kırıcı', '1990/08/14', 31, '77777777', 'Adana',
        'Yasin@gmail.com', '0 rh+', 3000, 'Garson', 'Mutfak', '09:00', '17:00', 'Pazar-Pazartesi'],
    [52, None, 24, 33333333, 'Michael', 'Jackson', '1990/08/14', 31, '66666666', 'İstanbul',
        'Michael@gmail.com', '0 rh-', 3000, 'Garson', 'Bar', '00:00', '05:00', 'Pazar-Pazartesi'],
    [53, 51, 24, 44444444, 'Tony', 'Stark', '1976/07/14', 44, '5555555555', 'Mersin', 'Tony@gmail.com',
        'AB rh+', 4000, 'Temizlik Görevlisi', 'Lobby', '09:00', '17:00', 'Pazar-Pazartesi'],
    [54, 51, 24, 55555555, 'Ayşe', 'Demir', '2000/03/22', 21, '888888888', 'Antalya',
        'Ayşe@gmail.com', '0 rh+', 2000, 'Sekreter', 'Lobby', '09:00', '20:00', 'Cuma-Cumartesi'],
    [55, 51, 24, 66666666, 'Ali', 'Bakır', '1992/05/14', 29, '777788888', 'Adana',
        'Ali@gmail.com', 'B rh+', 5000, 'Baş Görevli', 'Lobby', '20:00', '08:00', 'Pazartesi-Perşembe'],
    [56, 52, 20, 77777777, 'Mustafa', 'Jason', '2002/11/14', 19, '66666777777', 'Ankara',
        'Mustafa@gmail.com', '0 rh+', 2700, 'Aşçı', 'Mutfak', '09:00', '17:00', 'Cuma-Cumartesi'],
    [57, 50, 20, 88888888, 'Abdullah', 'Bozar', '1990/08/14', 31, '33333333', 'Adana',
        'Abdullah@gmail.com', '0 rh-', 2000, 'Bulaşıkçı', 'Mutfak', '09:00', '20:00', 'Salı-Çarşamba'],
    [58, 52, 24, 99999999, 'Mert', 'Yazıcı', '1980/08/14', 41, '4444444444', 'Hatay',
        'Mert@gmail.com', 'AB rh+', 5000, 'Havuz', 'Animatör', '09:00', '17:00', 'Pazar-Pazartesi'],
    [59, 52, 24, 100000000, 'Ozan', 'Yasan', '1965/08/14', 55, '111111222222', 'Konya',
        'Ozan@gmail.com', '0 rh+', 3000, 'Havuz', 'Cankurtaran', '09:00', '17:00', 'Pazartesi-Salı']
]

mycursor.executemany(sql, valuesPersonel)

sql = "INSERT IGNORE INTO ticari_tesis VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

valuesTicariTesis = [
    [10, 2, 3000, 'Toplantı Salonu', 1111111,
        'A Holding', '2021/04/12', '2021/09/12'],
    [11, 1, 3000, 'Market', 22222222, 'Çağdaş', '2017/01/01', '2020/01/01'],
    [12, 4, 2500, 'Oyun Salonu', 33333333,
        'Joy Holding', '2017/01/01', '2020/01/01'],
    [13, 2, 1000, 'Sinema Salonu', 4444444,
        'Cinemaximum', '2015/01/01', '2020/01/01'],
    [14, 3, 1000, 'Ala Carte Restoran', 55555555,
        'Thai Foods', '2021/04/12', '2021/09/12'],
    [15, 1, 3500, 'Dalış Marketi', 66666666,
        'Decathlon', '2017/01/01', '2020/01/01']
]

mycursor.executemany(sql, valuesTicariTesis)


con.commit()
