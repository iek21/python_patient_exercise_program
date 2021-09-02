##library
from tkinter import messagebox
import tkinter as tk
import time

import UI as ui
from databse import data, return_data
from settings import Variables
import excel
import mail_send

v = Variables()
d = data()
rd = return_data()


def username_record_control_block(username, status):
    control = False
    data = rd.username_data()

    if username:
        for i in data:
            a = ''.join(i)
            if a == username:
                control = True
            if control:
                break
        if control:
            if status == 1:
                messagebox.showinfo(v.successful_message, v.successful_login_message)
            elif status == 2:
                pass
        if not control:
            if status == 1:
                messagebox.showinfo(v.unsuccessful_message, v.unsuccessful_login_message)
            elif status == 2:
                pass
    else:
        messagebox.showinfo(v.unsuccessful_message, v.unfilled_field_message)
    return control


def recorded_data_control_block(date, username, name, surname, tc, age, hight, weight, mail, pasword,
                                doc_mail):
    global game_button_control_rec

    game_button_control_rec = False
    username_control = username_record_control_block(username, 2)

    if username and name and surname and tc and age and hight and weight:
        if username_control:
            messagebox.showinfo(v.unsuccessful_message, v.matching_usurname_message)
        else:
            m = mail
            s = pasword
            d = doc_mail

            if not m:
                m = "Girilmedi"
            if not s:
                s = "Girilmedi"
            if not d:
                d = "Girilmedi"
            try:
                d.add_data(date, username, name, surname, tc, age, hight, weight, m, s, d)
                ui.game_button_function(1)
                game_button_control_rec = True
                messagebox.showinfo(v.successful_message, v.successful_record_message)
            except:
                messagebox.showinfo(v.unsuccessful_message, v.unsuccessful_record_message)
    else:
        messagebox.showinfo(v.unsuccessful_message, v.unfilled_field_message)

    return game_button_control_rec


def exercise_record_control_block(username):
    status = username_record_control_block(username, 2)

    if status:
        data = d.delete_exercise_data()
        status = 1
        for i in range(len(data)):
            if data[i][0] == username:
                status = 2
                break
    if status == 1:
        messagebox.showinfo(v.unsuccessful_message, v.not_found_record_message)
    else:
        pass
    return status


def user_information_block(username):
    data = []
    record_data = rd.return_user_data()

    for i in range(len(record_data)):
        if record_data[i][1] == username:
            data = record_data[i]
    return data


def update_query_block():
    control = False
    MsgBox = tk.messagebox.askquestion(v.warning_message,
                                       v.update_warning_message,
                                       icon='warning')
    if MsgBox == 'yes':
        try:
            messagebox.showinfo(v.successful_message, v.update_succsessful_message)
            control = True
        except:
            messagebox.showinfo(v.unsuccessful_message, v.update_unsuccsessful_message)
    else:
        messagebox.showinfo(v.cancel_message, v.cancel_message1)
        control = False
    return control


def delete_block(username):
    control = False

    MsgBox = tk.messagebox.askquestion(v.warning_message,
                                       v.delete_warning_message,
                                       icon='warning')
    if MsgBox == 'yes':
        try:
            d.delete_data(username)
            d.delete_exercise_data(username)
            messagebox.showinfo(v.successful_message, v.delet_succsessful_message)
            control = True
        except:
            messagebox.showinfo(v.unsuccessful_message, v.unsuccessful_message)

    else:
        messagebox.showinfo(v.cancel_message, v.cancel_message)

    return control


def excel_block(username):
    exercise_list = []
    regester_data = user_information_block(username)

    exercise_data = rd.return_exercise_data()
    for i in range(len(exercise_data)):
        if exercise_data[i][0] == username:
            exercise_list.append(exercise_data[i])

    excel.create_excel(regester_data, exercise_list)


def mail_address_control_block(username):
    data = []
    record_data = rd.return_user_data()
    mail_control = True
    password_control = True
    doc_mail_control = True

    for i in range(len(record_data)):
        if record_data[i][1] == username:
            data = record_data[i]
    if data[8] == "Girilmedi":
        mail_control = False
    if data[9] == "Girilmedi":
        password_control = False
    if data[10] == "Girilmedi":
        doc_mail_control = False

    if mail_control == False and password_control == False:
        messagebox.showinfo(v.unsuccessful_message,
                            v.mail_unsuccsessful_message1)

    if mail_control == False:
        if password_control:
            messagebox.showinfo(v.unsuccessful_message,
                                v.mail_unsuccsessful_message1)
    if password_control == False:
        if mail_control:
            messagebox.showinfo(v.unsuccessful_message,
                                v.mail_unsuccsessful_message2)
    return mail_control, password_control, doc_mail_control


def mail_send_block(username, mail, password, doctor_mail, other_mail):
    excel_block(username)
    time.sleep(0.2)
    mail_send.mail(mail, password, doctor_mail, other_mail)


def game_data_record(username, date):
    d.add_exercise_data(username, date, v.exercise_positive_message,
                        v.exercise_negative_message, v.exercise_negative_message)
