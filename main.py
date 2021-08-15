from logging import error
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="1234",
    database="hoteldb"
)

mycursor = con.cursor()


def goToMain():
    widget.setCurrentIndex(0)


def goToQueryMain():
    widget.setCurrentIndex(1)


def goToBireyselInsertion():
    widget.setCurrentIndex(2)


def goToKurumsalInsertion():
    widget.setCurrentIndex(3)


def goToPersonelInsertion():
    widget.setCurrentIndex(4)


def goToOdaInsertion():
    widget.setCurrentIndex(5)


def goToRezervasyonInsertion():
    widget.setCurrentIndex(6)


def goToTesisInsertion():
    widget.setCurrentIndex(7)


def goToTicariTesisInsertion():
    widget.setCurrentIndex(8)


def goToAktiviteInsertion():
    widget.setCurrentIndex(9)


def goToBireyselQuery():
    widget.setCurrentIndex(10)


def goToKurumsalQuery():
    widget.setCurrentIndex(11)


def goToPersonelQuery():
    widget.setCurrentIndex(12)


def goToOdaQuery():
    widget.setCurrentIndex(13)


def goToRezervasyonQuery():
    widget.setCurrentIndex(14)


def goToTesisQuery():
    widget.setCurrentIndex(15)


def goToTicariTesisQuery():
    widget.setCurrentIndex(16)


def goToAktiviteQuery():
    widget.setCurrentIndex(17)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("components/insertionMainFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_3.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(3))
        self.pushButton_5.clicked.connect(lambda: self.navigate(4))
        self.pushButton_6.clicked.connect(lambda: self.navigate(5))
        self.pushButton_7.clicked.connect(lambda: self.navigate(6))
        self.pushButton_8.clicked.connect(lambda: self.navigate(7))
        self.pushButton_9.clicked.connect(lambda: self.navigate(8))
        self.pushButton_10.clicked.connect(lambda: self.navigate(9))
        self.pushButton_11.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToBireyselInsertion()
        elif(navigateTo == 3):
            goToKurumsalInsertion()
        elif(navigateTo == 4):
            goToPersonelInsertion()
        elif(navigateTo == 5):
            goToOdaInsertion()
        elif(navigateTo == 6):
            goToRezervasyonInsertion()
        elif(navigateTo == 7):
            goToTesisInsertion()
        elif(navigateTo == 8):
            goToTicariTesisInsertion()
        elif(navigateTo == 9):
            goToAktiviteInsertion()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class queryMain(QMainWindow):
    def __init__(self):
        super(queryMain, self).__init__()
        loadUi("components/queryMainFrame.ui", self)
        self.pushButton_2.clicked.connect(lambda: self.navigate(1))
        self.pushButton_3.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(3))
        self.pushButton_5.clicked.connect(lambda: self.navigate(4))
        self.pushButton_6.clicked.connect(lambda: self.navigate(5))
        self.pushButton_7.clicked.connect(lambda: self.navigate(6))
        self.pushButton_8.clicked.connect(lambda: self.navigate(7))
        self.pushButton_9.clicked.connect(lambda: self.navigate(8))
        self.pushButton_10.clicked.connect(lambda: self.navigate(9))
        self.pushButton_11.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToMain()
        elif(navigateTo == 2):
            goToBireyselQuery()
        elif(navigateTo == 3):
            goToKurumsalQuery()
        elif(navigateTo == 4):
            goToPersonelQuery()
        elif(navigateTo == 5):
            goToOdaQuery()
        elif(navigateTo == 6):
            goToRezervasyonQuery()
        elif(navigateTo == 7):
            goToTesisQuery()
        elif(navigateTo == 8):
            goToTicariTesisQuery()
        elif(navigateTo == 9):
            goToAktiviteQuery()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class bireyselInsertionWindow(QMainWindow):

    def __init__(self):
        super(bireyselInsertionWindow, self).__init__()
        loadUi("components/bireyselMusteriInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        musteriNo = self.lineEdit.text()
        rezervasyonNo = self.lineEdit_2.text()
        odaNo = self.lineEdit_3.text()
        kimlikNo = self.lineEdit_4.text()
        isim = self.lineEdit_5.text()
        soyisim = self.lineEdit_6.text()
        dogumTarihi = self.lineEdit_7.text()
        yas = self.lineEdit_8.text()
        mailAdresi = self.lineEdit_9.text()
        kanGrubu = self.lineEdit_10.text()
        adres = self.lineEdit_11.text()
        telefonNo = self.lineEdit_12.text()

        sql = "INSERT INTO bireysel_musteri VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)"
        values = [musteriNo, rezervasyonNo, odaNo, kimlikNo, isim, soyisim,
                  dogumTarihi, yas, mailAdresi, kanGrubu, adres, telefonNo]

        secondSQL = "INSERT INTO musteri VALUES (%s, %s)"
        secondValues = [musteriNo, 1]

        try:
            if rezervasyonNo == "":
                raise Exception("Please enter a valid reservation number.")
            if odaNo == "":
                raise Exception("Please enter a valid room number.")
            mycursor.execute(secondSQL, secondValues)
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Bireysel Musteri entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

        except Exception as err:
            self.textEdit_3.setPlainText(str(err))

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class kurumsalInsertionWindow(QMainWindow):

    def __init__(self):
        super(kurumsalInsertionWindow, self).__init__()
        loadUi("components/kurumsalMusteriInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        musteriNo = self.lineEdit.text()
        kurumIsmi = self.lineEdit_2.text()
        kurumAdresi = self.lineEdit_3.text()
        kurumTipi = self.lineEdit_4.text()
        kurumsalTelefon = self.lineEdit_5.text()
        mail = self.lineEdit_6.text()

        sql = "INSERT INTO kurumsal_musteri VALUES (%s, %s, %s, %s, %s, %s)"
        values = [musteriNo, kurumIsmi, kurumAdresi,
                  kurumTipi, kurumsalTelefon, mail]

        secondSQL = "INSERT INTO musteri VALUES (%s, %s)"
        secondValues = [musteriNo, 2]

        try:
            mycursor.execute(secondSQL, secondValues)
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Kurumsal Musteri entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class PersonelInsertionWindow(QMainWindow):

    def __init__(self):
        super(PersonelInsertionWindow, self).__init__()
        loadUi("components/personelInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        personelNo = self.lineEdit.text()
        yoneticiNo = self.lineEdit_2.text()
        if yoneticiNo == "":
            yoneticiNo = None
        calistigiTesisNo = self.lineEdit_3.text()
        kimlikNo = self.lineEdit_4.text()
        isim = self.lineEdit_5.text()
        soyisim = self.lineEdit_6.text()
        dogumTarihi = self.lineEdit_7.text()
        yas = self.lineEdit_8.text()
        telefonNo = self.lineEdit_9.text()
        kanGrubu = self.lineEdit_10.text()
        adres = self.lineEdit_11.text()
        mailAdresi = self.lineEdit_12.text()
        maas = self.lineEdit_13.text()
        gorev = self.lineEdit_14.text()
        departman = self.lineEdit_15.text()
        calismaSaatleri = self.lineEdit_16.text()
        izinGunleri = self.lineEdit_17.text()

        try:
            if calistigiTesisNo == "":
                raise Exception("Please enter a valid facility number.")
            if yoneticiNo == personelNo:
                raise Exception(
                    "Manager number can not be the same with Employee number.")

            calismaSaatleriBaslangic, calismaSaatleriBitis = calismaSaatleri.split(
                "-")

            sql = "INSERT INTO personel VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)"
            values = [personelNo, yoneticiNo, calistigiTesisNo, kimlikNo, isim, soyisim,
                      dogumTarihi, yas, telefonNo, adres, mailAdresi, kanGrubu, maas, gorev, departman, calismaSaatleriBaslangic, calismaSaatleriBitis, izinGunleri]

            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Personel entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

        except Exception as err:
            self.textEdit_3.setPlainText(str(err))

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.lineEdit_17.setText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class odaInsertionWindow(QMainWindow):

    def __init__(self):
        super(odaInsertionWindow, self).__init__()
        loadUi("components/odaInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        odaNo = self.lineEdit.text()
        rezervasyonNo = self.lineEdit_2.text()
        if(rezervasyonNo == ""):
            rezervasyonNo = None
        yatakSayisi = self.lineEdit_3.text()
        odaTipi = self.lineEdit_4.text()
        fiyat = self.lineEdit_5.text()
        kat = self.lineEdit_6.text()
        cephe = self.lineEdit_7.text()

        try:
            sql = "INSERT INTO oda VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [odaNo, rezervasyonNo,
                      yatakSayisi, odaTipi, fiyat, kat, cephe]
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Oda entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class rezervasyonInsertionWindow(QMainWindow):

    def __init__(self):
        super(rezervasyonInsertionWindow, self).__init__()
        loadUi("components/rezervasyonInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        rezervasyonNo = self.lineEdit.text()
        odaSayisi = self.lineEdit_2.text()
        kisiSayisi = self.lineEdit_3.text()
        baslangicTarihi = self.lineEdit_4.text()
        bitisTarihi = self.lineEdit_5.text()
        fiyat = self.lineEdit_6.text()

        try:
            sql = "INSERT INTO rezervasyon VALUES (%s, %s, %s, %s, %s, %s)"
            values = [rezervasyonNo, odaSayisi,
                      kisiSayisi, baslangicTarihi, bitisTarihi, fiyat]
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Rezervasyon entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class tesisInsertionWindow(QMainWindow):

    def __init__(self):
        super(tesisInsertionWindow, self).__init__()
        loadUi("components/tesisInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        tesisNo = self.lineEdit.text()
        aktiviteNo = self.lineEdit_2.text()
        if(aktiviteNo == ""):
            aktiviteNo = None
        kat = self.lineEdit_3.text()
        musteriKapasitesi = self.lineEdit_4.text()
        personelKapasitesi = self.lineEdit_5.text()
        faaliyetBaslangic = self.lineEdit_6.text()
        faaliyetBitis = self.lineEdit_7.text()
        tesisTipi = self.lineEdit_8.text()
        aktifPersonelSayisi = self.lineEdit_9.text()

        try:
            sql = "INSERT INTO tesis VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = [tesisNo, aktiviteNo,
                      kat, musteriKapasitesi, personelKapasitesi, faaliyetBaslangic, faaliyetBitis, tesisTipi, aktifPersonelSayisi]
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Tesis entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class ticariTesisInsertionWindow(QMainWindow):

    def __init__(self):
        super(ticariTesisInsertionWindow, self).__init__()
        loadUi("components/ticariTesisInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        mulkNo = self.lineEdit.text()
        kat = self.lineEdit_2.text()
        kira = self.lineEdit_3.text()
        tip = self.lineEdit_4.text()
        vergiNo = self.lineEdit_5.text()
        kiralayan = self.lineEdit_6.text()
        sozlesmeBaslangicTarihi = self.lineEdit_7.text()
        sozlesmeBitisTarihi = self.lineEdit_8.text()

        try:
            sql = "INSERT INTO ticari_tesis VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = [mulkNo, kat,
                      kira, tip, vergiNo, kiralayan, sozlesmeBaslangicTarihi, sozlesmeBitisTarihi]
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Ticari Tesis entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class aktiviteInsertionWindow(QMainWindow):

    def __init__(self):
        super(aktiviteInsertionWindow, self).__init__()
        loadUi("components/aktiviteInsertionFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.insert)
        self.pushButton_4.clicked.connect(lambda: self.navigate(2))
        self.pushButton_5.clicked.connect(self.setText)

    def insert(self):
        aktiviteNo = self.lineEdit.text()
        musteriNo = self.lineEdit_2.text()
        if musteriNo == "":
            musteriNo = None
        aktiviteBaslangic = self.lineEdit_3.text()
        aktiviteBitis = self.lineEdit_4.text()
        aktiviteIsmi = self.lineEdit_5.text()
        ucret = self.lineEdit_6.text()

        try:
            sql = "INSERT INTO aktivite VALUES (%s, %s, %s, %s, %s, %s)"
            values = [aktiviteNo, musteriNo,
                      aktiviteBaslangic, aktiviteBitis, aktiviteIsmi, ucret]
            mycursor.execute(sql, values)
            con.commit()
            self.clearFields()
            self.textEdit_3.setPlainText(
                'Aktivite entry added successfully.')

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        self.clearFields()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class bireyselQueryWindow(QMainWindow):

    def __init__(self):
        super(bireyselQueryWindow, self).__init__()
        loadUi("components/bireyselMusteriQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_3.clicked.connect(self.query)
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def query(self):

        sql = "SELECT * FROM bireysel_musteri "
        whereCondition = "WHERE "
        changed = False

        musteriNo = self.lineEdit.text()
        if musteriNo != "":
            whereCondition = whereCondition + "musteri_no = " + musteriNo
            changed = True

        rezervasyonNo = self.lineEdit_2.text()
        if rezervasyonNo != "":
            if changed == False:
                whereCondition = whereCondition + \
                    "bireysel_musteri.rezervasyon_no = " + rezervasyonNo
                changed = True
            else:
                whereCondition = whereCondition + \
                    " AND bireysel_musteri.rezervasyon_no = " + rezervasyonNo

        odaNo = self.lineEdit_3.text()
        if odaNo != "":
            if changed == False:
                whereCondition = whereCondition + "oda_no = " + odaNo
                changed = True
            else:
                whereCondition = whereCondition + " AND oda_no = " + odaNo

        isim = self.lineEdit_4.text()
        if isim != "":
            if changed == False:
                whereCondition = whereCondition + "isim = \"" + isim + "\""
                changed = True
            else:
                whereCondition = whereCondition + " AND isim = \"" + isim + "\""

        yas = self.lineEdit_5.text()
        if yas != "":
            if changed == False:
                whereCondition = whereCondition + "yas = " + yas
                changed = True
            else:
                whereCondition = whereCondition + " AND yas = " + yas

        kanGrubu = self.lineEdit_6.text()
        if kanGrubu != "":
            if changed == False:
                whereCondition = whereCondition + "kan_grubu = \"" + kanGrubu + "\""
                changed = True
            else:
                whereCondition = whereCondition + " AND kan_grubu = \"" + kanGrubu + "\""

        kat = self.lineEdit_7.text()
        if kat != "":
            sql = sql + ", oda "
            if changed == False:
                whereCondition = whereCondition + \
                    "bireysel_musteri.oda_no =oda.oda_no AND kat = " + kat
                changed = True
            else:
                whereCondition = whereCondition + \
                    " AND bireysel_musteri.oda_no =oda.oda_no AND kat = " + kat

        girisTarihi = self.lineEdit_8.text()
        if girisTarihi != "":
            sql = sql + ", rezervasyon "
            if changed == False:
                whereCondition = whereCondition + \
                    "bireysel_musteri.rezervasyon_no = rezervasyon.rezervasyon_no AND baslangic_tarihi = \"" + \
                    girisTarihi + "\""
                changed = True
            else:
                whereCondition = whereCondition + \
                    " AND bireysel_musteri.rezervasyon_no = rezervasyon.rezervasyon_no AND baslangic_tarihi = \"" + girisTarihi + "\""

        cikisTarihi = self.lineEdit_9.text()
        if cikisTarihi != "":
            sql = sql + ", rezervasyon "
            if changed == False:
                whereCondition = whereCondition + \
                    "bireysel_musteri.rezervasyon_no = rezervasyon.rezervasyon_no AND bitis_tarihi = \"" + \
                    cikisTarihi + "\""
            else:
                whereCondition = whereCondition + \
                    " AND bireysel_musteri.rezervasyon_no = rezervasyon.rezervasyon_no AND bitis_tarihi = \"" + cikisTarihi + "\""

        sqlComplete = sql + whereCondition

        print(sqlComplete)

        try:
            mycursor.execute(sqlComplete)
            result = mycursor.fetchall()
            self.textEdit_3.setPlainText("")
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_3.append(str(count) + ") " + stringI)

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_3.setPlainText(message)

    def navigate(self, navigateTo):
        self.clearFields()
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class kurumsalQueryWindow(QMainWindow):

    def __init__(self):
        super(kurumsalQueryWindow, self).__init__()
        loadUi("components/kurumsalMusteriQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class PersonelQueryWindow(QMainWindow):

    def __init__(self):
        super(PersonelQueryWindow, self).__init__()
        loadUi("components/PersonelQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class odaQueryWindow(QMainWindow):

    def __init__(self):
        super(odaQueryWindow, self).__init__()
        loadUi("components/odaQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class rezervasyonQueryWindow(QMainWindow):

    def __init__(self):
        super(rezervasyonQueryWindow, self).__init__()
        loadUi("components/rezervasyonQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class tesisQueryWindow(QMainWindow):

    def __init__(self):
        super(tesisQueryWindow, self).__init__()
        loadUi("components/tesisQueryFrame.ui", self)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class ticariTesisQueryWindow(QMainWindow):

    def __init__(self):
        super(ticariTesisQueryWindow, self).__init__()
        loadUi("components/ticariTesisQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


class aktiviteQueryWindow(QMainWindow):

    def __init__(self):
        super(aktiviteQueryWindow, self).__init__()
        loadUi("components/aktiviteQueryFrame.ui", self)
        self.pushButton.clicked.connect(goToQueryMain)
        self.pushButton.clicked.connect(lambda: self.navigate(1))
        self.pushButton_2.clicked.connect(lambda: self.navigate(2))
        self.pushButton_4.clicked.connect(lambda: self.navigate(1))
        self.pushButton_5.clicked.connect(self.setText)

    def navigate(self, navigateTo):
        self.clearTextAreas()
        if(navigateTo == 1):
            goToQueryMain()
        elif(navigateTo == 2):
            goToMain()

    def clearTextAreas(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")

    def setText(self):
        self.textEdit_2.setPlainText("")
        text = self.textEdit.toPlainText()
        try:
            mycursor.execute(text)
            result = mycursor.fetchall()
            count = 0
            for i in result:
                stringI = ""
                for j in i:
                    stringI = stringI + ", " + str(j)

                stringI = stringI[1:]
                stringI = stringI + "\n\n"
                count += 1
                self.textEdit_2.append(str(count) + ") " + stringI)
            con.commit()

        except mysql.connector.Error as err:
            message = ""
            message = message + "Error Code: " + str(err.errno) + "\n"
            message = message + "SQLSTATE: " + str(err.sqlstate) + "\n"
            message = message + "Message: " + str(err.msg) + "\n"
            self.textEdit_2.setPlainText(message)


app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
mainWindow = MainWindow()
queryMainWindow = queryMain()
bireyselInsertion = bireyselInsertionWindow()
kurumsalInsertion = kurumsalInsertionWindow()
personelInsertion = PersonelInsertionWindow()
odaInsertion = odaInsertionWindow()
rezervasyonInsertion = rezervasyonInsertionWindow()
tesisInsertion = tesisInsertionWindow()
ticariTesisInsertion = ticariTesisInsertionWindow()
aktiviteInsertion = aktiviteInsertionWindow()
bireyselQuery = bireyselQueryWindow()
kurumsalQuery = kurumsalQueryWindow()
personelQuery = PersonelQueryWindow()
odaQuery = odaQueryWindow()
rezervasyonQuery = rezervasyonQueryWindow()
tesisQuery = tesisQueryWindow()
ticariTesisQuery = ticariTesisQueryWindow()
aktiviteQuery = aktiviteQueryWindow()
widget.addWidget(mainWindow)
widget.addWidget(queryMainWindow)
widget.addWidget(bireyselInsertion)
widget.addWidget(kurumsalInsertion)
widget.addWidget(personelInsertion)
widget.addWidget(odaInsertion)
widget.addWidget(rezervasyonInsertion)
widget.addWidget(tesisInsertion)
widget.addWidget(ticariTesisInsertion)
widget.addWidget(aktiviteInsertion)
widget.addWidget(bireyselQuery)
widget.addWidget(kurumsalQuery)
widget.addWidget(personelQuery)
widget.addWidget(odaQuery)
widget.addWidget(rezervasyonQuery)
widget.addWidget(tesisQuery)
widget.addWidget(ticariTesisQuery)
widget.addWidget(aktiviteQuery)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print('Exiting')
