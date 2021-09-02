class Variables:
    def __init__(self):
        self.excel_file_name = "Egzersiz_Verileri.xlsx"

        ##Genel Ayarlar
        self.program_name = "Egzersiz Arayuz"
        self.program_size = "1100x740"
        self.program_background = "white"
        self.program_label_color = '#add8e6'

        ##Baslık Dizayn
        self.program_tittle = "FİZİK TEDAVİ"
        self.tittle_write_type = 'Verdana 30 bold'
        self.padx = 10
        self.pady = 10

        #########ANA SAYFA#############
        ##Kayıt Butonu
        self.record_buton_name = "YENİ KAYIT \n OLUŞTUR"
        self.record_buton_color = '#add8e6'
        self.record_buton_height = 4
        self.record_buton_width = 15
        self.record_buton_write_type = 'Verdana 30 bold'

        ##Giris Butonu
        self.login_buton_name = " GİRİŞ YAP"
        self.login_buton_color = '#add8e6'
        self.login_buton_height = 4
        self.login_buton_width = 15
        self.login_buton_write_type = 'Verdana 30 bold'

        ##Kullanıcı İşlemleri Butonu
        self.delete_buton_name = "KULLANICI \n İŞLEMLERİ"
        self.delete_buton_color = '#add8e6'
        self.delete_buton_height = 4
        self.delete_buton_width = 15
        self.delete_buton_write_type = 'Verdana 30 bold'

        ##Görüntüle Butonu %
        self.view_buton_name = "GÖRÜNTÜLE \n SONUÇ AL"
        self.view_buton_color = '#add8e6'
        self.view_buton_height = 4
        self.view_buton_width = 15
        self.view_buton_write_type = 'Verdana 30 bold'

        #########KAYIT & GÖRÜNTÜLE % GÜNCELLE#################
        ##Kayıt Sayfasında ve Görüntüle Sayfasında ortak tool ayarları kullanulmıştır.

        self.back_buton_rec_name = "GERİ"
        self.back_buton_rec_color = 'red'
        self.back_buton_rec_height = 1
        self.back_buton_rec_width = 7
        self.back_buton_rec_write_type = 'Verdana 30 bold'

        self.record_buton_rec_name = " KAYIT"
        self.update_buton_rec_name = " GÜNCELLE"
        self.record_buton_rec_color = '#57f522'
        self.record_buton_rec_height = 1
        self.record_buton_rec_width = 7
        self.record_buton_rec_write_type = 'Verdana 30 bold'

        self.x_distance = 80  ##Kayıt Sayfası
        self.y_space = 150
        self.x_distance_s = 60  ## Görüntüle Sayfası
        self.y_space_s = 180

        self.tool_rec_bg = "grey"
        self.tool_rec_fg = None
        self.tool_date_rec_fg = "black"
        self.tool_rec_width = 30
        self.tool_write_type = 'Verdana 10 bold'
        self.tool_title_write_type = 'Verdana 20 bold'
        self.table_title_write_type = 'Verdana 12 bold'

        self.tool_title_date_name = "|     EGZERSİZ TARİHİ     |"
        self.tool_title_exercise1_name = "|     A EGZERSİZİ     |"
        self.tool_title_exercise2_name = "|     B EGZERSİZİ     |"
        self.tool_title_exercise3_name = "|     C EGZERSİZİ     |"
        self.tool_title_name = "GEÇMİŞ EGZERSİZ KAYITLARI"
        self.tool_subtitle_name = "Kullanıcı Bilgileri :"
        self.username_name = "Kullanıcı \n   Adı :"
        self.name_name = "İsim :"
        self.surname_name = "Soyisim:"
        self.tc_name = "TC :"
        self.age_name = "Yaş :"
        self.height_name = "Boy :"
        self.height_name = "Boy :"
        self.weight_name = "Kilo :"
        self.mail_name = "Email :"
        self.password_name = "Sifre :"
        self.doc_mail_name = "Doktor \n Email :"
        self.date_name = "Tarih :"
        self.date_sc_name = "Kayıt\nTarihi :"
        self.game_name = "Oyun :"
        self.mail_name = "Email :"
        self.doctor_send_mail_name = " Doktor Email :"  ## Mail Gönder Sekmesi
        self.other_send_mail_name = "Mail Adresi Ekle :"  ## Mail Gönder Sekmesi

        #########KULLANCC İŞLEMLERİ & GÖRÜNTÜLE #################
        ##Kayıt Kullanıcı İşlemleri Sayfasında ve Görüntüle Sayfasında ortak buton ayarları kullanulmıştır.

        self.scan_buton_name = "EGZERSİZ\nKAYITLARI"
        self.update_buton_name = "GÜNCELLE"
        self.update_buton_color = '#57f522'
        self.update_buton_height = 2
        self.update_buton_width = 10
        self.update_buton_write_type = 'Verdana 30 bold'

        self.mail_buton_name = "EMAİL\nGÖNDER"
        self.delete_tab_buton_name = "VERİLERİ\nTEMİZLE"
        self.delete_tab_buton_color = 'red'
        self.delete_tab_buton_height = 2
        self.delete_tab_buton_width = 10
        self.delete_tab_buton_write_type = 'Verdana 30 bold'

        self.delete_back_buton_name = "GERİ"
        self.delete_back_buton_color = 'red'
        self.delete_back_buton_height = 1
        self.delete_back_buton_width = 7
        self.delete_back_buton_write_type = 'Verdana 30 bold'

        self.delete_continue_buton_name = "DEVAM ET"
        self.delete_continue_buton_color = '#add8e6'
        self.delete_continue_buton_write_type = 'Verdana 13 bold'
        # self.delete_back_buton_height = 1
        # self.delete_back_buton_width = 7

        self.send_buton_name = "MAİL GÖNDER"
        self.send_buton_color = '#add8e6'
        self.send_buton_write_type = 'Verdana 13 bold'
        # self.delete_back_buton_height = 1
        # self.delete_back_buton_width = 7

        self.update_buton2_name = "GÜNCELLE"
        self.update_buton2_color = '#57f522'
        self.update_buton2_height = 1
        self.update_buton2_width = 9
        self.update_buton2_write_type = 'Verdana 30 bold'

        self.label_del_name = "Kullanıcı Adı"
        self.label_del_bg = "white"
        self.label_del_fg = None
        self.label_del_write_type = 'Verdana 20 bold'

        self.tool_del_bg = "white"
        self.tool_del_write_type = 'Verdana 13 bold'

        #########GİRİŞ YAP#################
        self.continue_back_buton_name = "GERİ"
        self.continue_back_buton_color = 'red'
        self.continue_back_buton_height = 1
        self.continue_back_buton_width = 7
        self.continue_back_buton_write_type = 'Verdana 30 bold'

        self.continue_continue_buton_name = "DEVAM ET"
        self.continue_continue_buton_color = '#add8e6'
        self.continue_continue_buton_write_type = 'Verdana 13 bold'
        # self.delete_back_buton_height = 1
        # self.delete_back_buton_width = 7

        self.x_distance_c = 20
        self.y_space_c = 300

        self.label_con_name = "Kullanıcı Adı"
        self.label_con_bg = "white"
        self.label_con_fg = None
        self.label_con_write_type = 'Verdana 20 bold'

        self.label1_con_name = "Merhaba"
        self.label2_con_name = "Kullanıcı Girişiniz Başarılı. Oyuna Geçebilirsiniz.."
        self.label3_con_name = ";"
        self.label1_con_fg = None
        self.label1_con_write_type = 'Verdana 12 bold'

        self.tool_con_bg = "white"
        self.tool_con_write_type = 'Verdana 13 bold'

        #########OYUN BUTONU##################
        self.game_buton_name = "OYUNA GİT"
        self.game_buton_color = '#0a41e5'
        self.game_buton_height = 1
        self.game_buton_width = 10
        self.game_buton_write_type = 'Verdana 30 bold'

        self.game_back_buton_name = "BAŞLANGICA\nDÖN"
        self.game_back_buton_color = '#0a41e5'
        self.game_back_buton_height = 2
        self.game_back_buton_width = 7
        self.game_back_buton_write_type = 'Verdana 30 bold'

        #####MAİL####################
        self.mail_text = '''Merhaba,
    Hastaya ait egzersiz verileri tablosu ek'tedir..
    İyi Çalışmalar...
    '''
        self.mail_topic = "Hasta Günlük Egzersiz Verileri hk;"

        ##MESSAGEBOX
        self.successful_message = "Başarılı"
        self.unsuccessful_message = "Başarısız !"
        self.cancel_message = "İptal !"
        self.cancel_message1 = "İşlem İptal Edildi"
        self.warning_message = "Uyarı !"

        self.unfilled_field_message = "Lütfen Zorunlu Alanları Doldurun"
        self.successful_record_message = "Kayıt Başarılı"
        self.unsuccessful_record_message = "Kayıt Sırasında Hata Oluştu"
        self.successful_login_message = "Kullanıcı Girişi Başarılı"
        self.unsuccessful_login_message = "Kullanıcı Adı Sistemde Kayıtlı Değil"
        self.not_found_record_message = "Kullanıcıya Ait Kayıt Bulunamadı Kayıtlı Değil"
        self.matching_usurname_message = "Kullanıcı Adı Daha Önce Kullanıldı"

        self.update_warning_message = 'Emin misiniz ? ?\nKullanıcı Verileriniz Güncellenecek'
        self.update_succsessful_message = "Kullanıcı Verileri Başarıyla Güncellendi"
        self.update_unsuccsessful_message = "Kullanıcı Verileriniz Güncellenemedi"
        self.delete_warning_message = 'Emin misiniz ? ?\nKullanıcı Verilerinizin Tamamı Silinecek'
        self.delet_succsessful_message = "Kullanıcı Verileri Silindi"
        self.update_unsuccsessful_message = "Kullanıcı Verileriniz Silinemedi"

        self.mail_succsessful_message = "Egzersiz Verileri Mail Adresinize Gönderildi"
        self.mail_succsessful_message = "Egzersiz Verileri Mail Adresinize Gönderildi"
        self.mail_unsuccsessful_message = "Egzersiz Verileri Mail Adresinize Gönderilemedi"
        self.mail_unsuccsessful_message1 = "Mail Adresiniz Sitemde Kayıtlı Değil \n Lütfen Güncelle Sekmesinden Mail Aresinizi Ekleyin ve Tekrar Deneyin"
        self.mail_unsuccsessful_message2 = "Mail Şifreniz Sitemde Kayıtlı Değil \n Lütfen Güncelle Sekmesinden Mail Şifrenizi Ekleyin ve Tekrar Deneyin"
        self.mail_unsuccsessful_message3 = "Lütfen En Az Bir Mail Adresi Ekleyin"

        ##Game_Message
        self.exercise_positive_message = "Günlük Başarıyla Egzersiz Tamamlandı"
        self.exercise_negative_message = "Günlük Egzersiz Tamamlanmadı !"
