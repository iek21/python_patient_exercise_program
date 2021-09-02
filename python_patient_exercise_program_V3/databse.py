##library
import sqlite3


class data(object):

    def __init__(self):
        self.con = sqlite3.connect("Kayit_Listesi.db")
        self.cursor = self.con.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Kayit_Listesi(Tarih INT, Kullanici_Adi TEXT, Ad TEXT, Soyad TEXT, Tc INT, Yas INT, Boy INT, Kilo INT, Email TEXT, Sifre TEXT, Doktor_Email TEXT)")

        self.con_e = sqlite3.connect("Egzersiz_Tablosu.db")
        self.cursor_e = self.con_e.cursor()
        self.cursor_e.execute(
            "CREATE TABLE IF NOT EXISTS Egzersiz_Tablosu(Kullanici_Adi TEXT, Tarih INT, A_Egzersizi TEXT, B_Egzerisizi TEXT, C_Egzersizi TEXT)")

    def add_data(self, Tarih, Kullanici_Adi, Ad, Soyad, TC, Yas, Boy, Kilo, Email, Sifre, Doktor_Email):
        self.cursor.execute(
            "INSERT INTO Kayit_Listesi (Tarih, Kullanici_Adi, Ad, Soyad, Tc, Yas, Boy, Kilo, Email, Sifre, Doktor_Email) VALUES (?,?,?,?,?,?,?,?,?,?,?) ",
            (Tarih, Kullanici_Adi, Ad, Soyad, TC, Yas, Boy, Kilo, Email, Sifre, Doktor_Email))
        self.con.commit()
        self.con.close()

    def update_data(self, Ad, Soyad, TC, Yas, Boy, Kilo, Email, Sifre, Doktor_Email,
                    Ad_yd, Soyad_yd, TC_yd, Yas_yn, Boy_yn, Kilo_yd, Email_yd, Sifre_yd, Doktor_Email_yd):
        self.cursor.execute("UPDATE Kayit_Listesi SET Ad=? WHERE Ad=? ", (Ad_yd, Ad))
        self.cursor.execute("UPDATE Kayit_Listesi SET Soyad=? WHERE Soyad=? ", (Soyad_yd, Soyad))
        self.cursor.execute("UPDATE Kayit_Listesi SET Tc=? WHERE Tc=? ", (TC_yd, TC))
        self.cursor.execute("UPDATE Kayit_Listesi SET Yas=? WHERE Yas=? ", (Yas_yn, Yas))
        self.cursor.execute("UPDATE Kayit_Listesi SET Boy=? WHERE Boy=? ", (Boy_yn, Boy))
        self.cursor.execute("UPDATE Kayit_Listesi SET Kilo=? WHERE Kilo=? ", (Kilo_yd, Kilo))
        self.cursor.execute("UPDATE Kayit_Listesi SET Email=? WHERE Email=? ", (Email_yd, Email))
        self.cursor.execute("UPDATE Kayit_Listesi SET Sifre=? WHERE Sifre=? ", (Sifre_yd, Sifre))
        self.cursor.execute("UPDATE Kayit_Listesi SET Doktor_Email=? WHERE Doktor_Email=? ",
                            (Doktor_Email_yd, Doktor_Email))
        self.con.commit()
        self.con.close()

    def delete_data(self, user_name):
        self.cursor.execute("DELETE FROM Kayit_Listesi WHERE Kullanici_Adi = ?", [user_name])
        self.con.commit()
        self.con.close()

    def add_exercise_data(self, Kullanici_Adi, Tarih, A_Egzersizi, B_Egzerisizi, C_Egzersizi):
        self.cursor_e.execute(
            "INSERT INTO Egzersiz_Tablosu (Kullanici_Adi, Tarih, A_Egzersizi, B_Egzerisizi, C_Egzersizi) VALUES (?,?,?,?,?) ",
            (Kullanici_Adi, Tarih, A_Egzersizi, B_Egzerisizi, C_Egzersizi))
        self.con_e.commit()
        self.con_e.close()

    def delete_exercise_data(self, user_name):
        self.cursor_e.execute("DELETE FROM Egzersiz_Tablosu WHERE Kullanici_Adi = ?", [user_name])
        self.con_e.commit()
        self.con_e.close()


class return_data(data):

    def __init__(self):
        super().__init__()

    def return_user_data(self):
        self.cursor.execute(
            (
                "SELECT Tarih, Kullanici_Adi, Ad, Soyad, Tc, Yas, Boy, Kilo, Email, Sifre, Doktor_Email FROM Kayit_Listesi"))
        data = self.cursor.fetchall()
        self.con.commit()
        self.con.close()

        return data

    def username_data(self):
        self.cursor.execute(("SELECT Kullanici_Adi FROM Kayit_Listesi"))
        data = self.cursor.fetchall()
        self.con.commit()
        self.con.close()

        return data

    def return_exercise_data(self):
        self.cursor_e.execute(
            ("SELECT Kullanici_Adi, Tarih, A_Egzersizi, B_Egzerisizi, C_Egzersizi FROM Egzersiz_Tablosu"))
        data = self.cursor_e.fetchall()
        self.con_e.commit()
        self.con_e.close()

        return data
