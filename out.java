import java.util.ArrayList;
import java.util.Random;

public class out {

    public static void main(String[] args)

    {

        int[][] val = { { 1, 1 }, { 2, 1 }, { 3, 2 }, { 4, 2 }, { 5, 2 }, { 6, 1 }, { 7, 2 }, { 8, 1 }, { 9, 2 },
                { 10, 1 }, { 11, 1 }, { 12, 2 }, { 13, 2 }, { 14, 1 }, { 15, 2 }, { 16, 2 }, { 17, 2 }, { 18, 1 },
                { 19, 1 }, { 20, 2 }, { 21, 1 }, { 22, 2 }, { 23, 2 }, { 24, 1 }, { 25, 2 }, { 26, 1 }, { 27, 2 },
                { 28, 1 }, { 29, 1 }, { 30, 1 }, { 31, 2 }, { 32, 2 }, { 33, 1 }, { 34, 1 }, { 35, 1 }, { 36, 2 },
                { 37, 1 }, { 38, 2 }, { 39, 1 }, { 40, 2 }, { 41, 1 }, { 42, 2 }, { 43, 1 }, { 44, 2 }, { 45, 2 },
                { 46, 1 }, { 47, 1 }, { 48, 2 }, { 49, 1 }, { 50, 1 } };

        String[][] namesList = { { "Maxwell", "Ryan" }, { "Conor", "Briggs" }, { "Farhan", "Hunt" },
                { "Allen", "Rice" }, { "Harley", "Leonard" }, { "Erik", "Graham" }, { "Jeremy", "Walker" },
                { "Charles", "Reid" }, { "Robbie", "Cole" }, { "Omar", "Wagner" }, { "Oliver", "Mullins" },
                { "Julia", "Stanley" }, { "Jimmy", "Gomez" }, { "Yasin", "Williamson" }, { "Ellis", "Watson" },
                { "Kieron", "King" }, { "Anas", "Holt" }, { "Hamish", "Haynes" }, { "Leonard", "Phillips" },
                { "Roman", "Edwards" }, { "Connor", "Weaver" }, { "Max", "Shelton" }, { "Zakariya", "Griffin" },
                { "Dale", "Ford" }, { "Owain", "Rogers" }, { "Tristan", "Olson" }, { "Clayton", "White" },
                { "Theodore", "Moreno" }, { "Amir", "Ortiz" }, { "Osman", "Rodriguez" }, { "Katy", "Howarth" },
                { "Rachel", "Hammond" }, { "Rhonda", "Norris" }, { "Caitlyn", "Lovell" }, { "Antonia", "Drew" },
                { "Ellie", "Bird" }, { "Isobelle", "Mccarthy" }, { "Anabelle", "Fernandez" }, { "Charlotte", "Mccoy" },
                { "Lana", "Meyer" }, { "Allanah", "Solis" }, { "Lauren", "Laing" }, { "Joel", "Gonzales" },
                { "Tia", "Bailey" }, { "Casey", "Carrillo1" } };

        String[] adressList = { "1745 T Street Southeast Washington DC 20020",
                "6007 Applegate Lane Louisville KY 40219", "560 Penstock Drive Grass Valley CA 95945",
                "150 Carter Street Manchester CT 06040", "2721 Lindsay Avenue Louisville KY 40206",
                "18 Densmore Drive Essex VT 05452", "637 Britannia Drive Vallejo CA 94591",
                "5601 West Crocus Drive Glendale AZ 85306", "5403 Illinois Avenue Nashville TN 37209",
                "8821 West Myrtle Avenue Glendale AZ 85305", "2203 7th Street Road Louisville KY 40208",
                "6463 Vrain Street Arvada CO 80003", "87 Horseshoe Drive West Windsor VT 05037",
                "60 Desousa Drive Manchester CT 06040", "4 Old Colony Way Yarmouth MA 02664",
                "314 South 17th Street Nashville TN 37206", "1649 Timberridge Court Fayetteville AR 72704",
                "5461 West Shades Valley Drive Montgomery AL 36108", "629 Debbie Drive Nashville TN 37076",
                "22572 Toreador Drive Salinas CA 93908", "3034 Mica Street Fayetteville AR 72704",
                "3729 East Mission Boulevard Fayetteville AR 72703", "5114 Greentree Drive Nashville TN 37211",
                "3466 Southview Avenue Montgomery AL 36111", "1513 Cathy Street Savannah GA 31415",
                "600 West 19th Avenue APT B Anchorage AK 99503", "1208 Elkader Court North Nashville TN 37013",
                "210 Green Road Manchester CT 06042", "49548 Road 200 O'Neals CA 93645",
                "81 Seaton Place Northwest Washington DC 20001", "1267 Martin Street #203 Nashville TN 37203",
                "7431 Candace Way #1 Louisville KY 40214", "1407 Walden Court Crofton MD 21114",
                "5906 Milton Avenue Deale MD 20751", "74 Springfield Street B Agawam MA 01001",
                "2905 Stonebridge Court Norman OK 73071", "20930 Todd Valley Road Foresthill CA 95631",
                "5928 West Mauna Loa Lane Glendale AZ 85306", "802 Madison Street Northwest Washington DC 20011",
                "2811 Battery Place Northwest Washington DC 20016", "210 Lacross Lane Westmore VT 05860",
                "2010 Rising Hill Drive Norman OK 73071", "388 East Main Street VT 05753",
                "450 Kinhawk Drive Nashville TN 37211", "131 Westerly Street Manchester CT 06042",
                "308 Woodleaf Court Glen Burnie MD 21061", "8502 Madrone Avenue Louisville KY 40258",
                "23 Sable Run Lane Methuen MA 01844", "716 Waller Road Brentwood TN 37027",
                "416 McIver Street Nashville TN 37211", "1508 Massachusetts Avenue Southeast Washington DC 20003",
                "5615 West Villa Maria Drive Glendale AZ 85308",
                "3162 Martin Luther King Junior Boulevard #2 Fayetteville AR 72704",
                "5306 Ritchie Highway Baltimore MD 21225", "109 Summit Street Burlington VT 05401",
                "816 West 19th Avenue Anchorage AK 99503", "172 Alburg Springs Road Alburgh VT 05440",
                "159 Downey Drive A Manchester CT 06040", "125 John Street Santa Cruz CA 95060",
                "1101 Lotus Avenue Glen Burnie MD 21061", "8376 Albacore Drive Pasadena MD 21122",
                "491 Arabian Way Grand Junction CO 81504", "12245 West 71st Place Arvada CO 80004",
                "80 North East Street #4 Holyoke MA 01040", "4695 East Huntsville Road Fayetteville AR 72701",
                "310 Timrod Road Manchester CT 06040", "1364 Capri Drive Panama City FL 32405",
                "132 Laurel Green Court Savannah GA 31419", "6657 West Rose Garden Lane Glendale AZ 85308",
                "519 West 75th Avenue #APT 000003 Anchorage AK 99518", "31353 Santa Elena Way Union City CA 94587",
                "8398 West Denton Lane Glendale AZ 85305", "700 Winston Place Anchorage AK 99504",
                "232 Maine Avenue Panama City FL 32401", "1 Kempf Drive Easton MA 02375",
                "5811 Crossings Boulevard Nashville TN 37013", "5108 Franklin Street Savannah GA 31405",
                "913 Fallview Trail Nashville TN 37211", "270 Chrissy's Court VT 05443",
                "130 Old Route 103 Chester VT 05143", "10826 Pointe Royal Drive Bakersfield CA 93311",
                "74 Ranch Drive Montgomery AL 36109", "6601 West Ocotillo Road Glendale AZ 85301",
                "19416 Barclay Road Castro Valley CA 94546", "1347 Blackwalnut Court Annapolis MD 21403",
                "1770 Colony Way Fayetteville AR 72704", "165 Saint John Street Manchester CT 06040",
                "2409 Research Boulevard Fort Collins CO 80526", "1903 Bashford Manor Lane Louisville KY 40218",
                "8315 Surf Drive Panama City Beach FL 32408", "3301 Old Muldoon Road Anchorage AK 99504",
                "8800 Cordell Circle #APT 000003 Anchorage AK 99502", "117 East Cook Avenue Anchorage AK 99501",
                "6231 North 67th Avenue #241 Glendale AZ 85301", "8505 Waters Avenue #66 Savannah GA 31406",
                "7 Underwood Place Northwest Washington DC 20012", "21950 Arnold Center Road Carson CA 90810",
                "1427 South Carolina Avenue Southeast Washington DC 20003",
                "1420 Turtleback Trail Panama City FL 32413" };

        String[] bloodList = { "A rh+", "A rh-", "B rh+", "B rh-", "AB rh+", "AB rh-", "0 rh+", "0 rh-" };

        String[] num = "13,15,17,18,19".split(",");

        int count = 1;

        ArrayList<Integer> listForID = new ArrayList<Integer>();

        ArrayList<Integer> listForAdress = new ArrayList<Integer>();

        ArrayList<String> listForPhoneNumber = new ArrayList<String>();

        int randomForID = 0;

        int randomForAdress = 0;

        String randomForPhoneNumber = "";

        for (int i = 0; i < 50; i++) {

            if (val[i][1] == 1) {

                randomForID = (int) (Math.random() * 750 + 25);

                randomForAdress = (int) (Math.random() * adressList.length);

                Random r = new Random();

                randomForPhoneNumber = num[r.nextInt(5)] + (int) ((Math.random() + 1) * 100000000);

                while (listForID.contains(randomForID)) {

                    randomForID = (int) (Math.random() * 900000000 + 100000000);
                }

                while (listForAdress.contains(randomForAdress)) {

                    randomForAdress = (int) (Math.random() * adressList.length);
                }

                while (listForPhoneNumber.contains(randomForPhoneNumber)) {

                    randomForPhoneNumber = num[r.nextInt(5)] + (int) ((Math.random() + 1) * 100000000);
                }

                listForID.add(randomForID);
                listForAdress.add(randomForAdress);
                listForPhoneNumber.add(randomForPhoneNumber);

                int randomName = (int) (Math.random() * namesList.length);
                int randomSurname = (int) (Math.random() * namesList.length);

                int randomDay = (int) (Math.random() * 30 + 1);
                int randomMonth = (int) (Math.random() * 12 + 1);
                int randomYear = (int) (Math.random() * 80 + 1940);

                int randomBloodType = (int) (Math.random() * bloodList.length);

                String email = namesList[randomName][0] + "@gmail.com";

                String date = "TO_DATE(" + randomDay + "/" + randomMonth + "/" + randomYear + "', 'DD/MM/YYYY'";

                System.out.println("[" + val[i][0] + ", " + (int) (Math.random() * 750 + 25) + ", " + count++ + ", "
                        + randomForID + ", " + namesList[randomName][0] + ", " + namesList[randomSurname][1] + ", "
                        + date + ", " + (2020 - randomYear) + ", " + email + ", " + bloodList[randomBloodType] + ", "
                        + adressList[randomForAdress] + ", " + randomForPhoneNumber);
            }
        }

    }
}