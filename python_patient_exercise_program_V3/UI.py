##library
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry

import datetime
import time

from settings import Variables
import operation as op
from databse import data, return_data

v = Variables()
d = data()
rd = return_data()


def __init__():
    global ws, C
    ws = tk.Tk()
    ws.title(v.program_name)
    ws.geometry(v.program_size)
    ws.configure(bg=v.program_background)
    ws.config(width=ws.winfo_width())

    C = Canvas(ws, bg="blue", height=250, width=300)
    filename = PhotoImage(file="backgraund\\backgraund.png")
    background_label = Label(ws, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


def patient_exercise_program():
    __init__()
    entry()
    C.pack()
    ws.mainloop()


def entry():
    global new_record_button, login_button, record_view, delete_record_button

    time.sleep(0.1)

    frame_top = Frame(ws, bg=v.program_label_color)
    frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    title = Label(frame_top, bg=v.program_label_color, text=v.program_tittle, font=v.tittle_write_type)
    title.pack(padx=v.padx, pady=v.pady)

    new_record_button = tk.Button(text=v.record_buton_name, bg=v.record_buton_color, font=v.record_buton_write_type,
                                  command=record_tab)
    new_record_button.place(x=100, y=150)
    new_record_button.config(height=v.record_buton_height, width=v.record_buton_width)

    login_button = tk.Button(text=v.login_buton_name, bg=v.login_buton_color, font=v.login_buton_write_type,
                             command=continue_tab)
    login_button.place(x=570, y=150)
    login_button.config(height=v.login_buton_height, width=v.login_buton_width)

    delete_record_button = tk.Button(text=v.delete_buton_name, bg=v.delete_buton_color, font=v.delete_buton_write_type,
                                     command=delete_tab)
    delete_record_button.place(x=100, y=400)
    delete_record_button.config(height=v.delete_buton_height, width=v.delete_buton_width)

    record_view = tk.Button(text=v.view_buton_name, bg=v.view_buton_color,
                            font=v.view_buton_write_type, command=scanning_tab)
    record_view.place(x=570, y=400)
    record_view.config(height=v.view_buton_height, width=v.view_buton_width)


def entry_button_clear():
    new_record_button.place_forget()
    login_button.place_forget()
    delete_record_button.place_forget()
    record_view.place_forget()
    time.sleep(0.1)


def record_tab():
    global rec_clear_tool_function, game_button, game_button_control_rec

    game_button_control_rec = False

    def rec_button_function():
        global back_button_rec, record_button_rec

        back_button_rec = tk.Button(text=v.back_buton_rec_name, bg=v.back_buton_rec_color,
                                    font=v.back_buton_rec_write_type, command=record_back_button_function)
        back_button_rec.place(x=v.x_distance, y=600)
        back_button_rec.config(height=v.back_buton_rec_height, width=v.back_buton_rec_width)

        record_button_rec = tk.Button(text=v.record_buton_rec_name, bg=v.record_buton_rec_color,
                                      font=v.record_buton_rec_write_type, command=regester_data_helper_function)
        record_button_rec.place(x=v.x_distance + 300, y=600)
        record_button_rec.config(height=v.record_buton_rec_height, width=v.record_buton_rec_width)

    def rec_tool_function():
        global date, date_bar, input_name, input_surname, input_tc, input_age, input_height, input_weight, input_mail, \
            input_doc_mail, name, surname, tc, age, height, weight, mail, doc_mail, input_game, game, input_username_, username_, \
            input_password, password

        username_ = tk.Label(text=v.username_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        username_.place(x=v.x_distance, y=v.y_space)
        input_username_ = tk.Entry(width=v.tool_rec_width)
        input_username_.place(x=v.x_distance + 70, y=v.y_space)

        name = tk.Label(text=v.name_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        name.place(x=v.x_distance, y=v.y_space + 50)
        input_name = tk.Entry(width=v.tool_rec_width)
        input_name.place(x=v.x_distance + 70, y=v.y_space + 50)

        surname = tk.Label(text=v.surname_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        surname.place(x=v.x_distance, y=v.y_space + 100)
        input_surname = tk.Entry(width=v.tool_rec_width)
        input_surname.place(x=v.x_distance + 70, y=v.y_space + 100)

        tc = tk.Label(text=v.tc_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        tc.place(x=v.x_distance, y=v.y_space + 150)
        input_tc = tk.Entry(width=v.tool_rec_width)
        input_tc.place(x=v.x_distance + 70, y=v.y_space + 150)

        age = tk.Label(text=v.age_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        age.place(x=v.x_distance, y=v.y_space + 200)
        input_age = tk.Entry(width=v.tool_rec_width)
        input_age.place(x=v.x_distance + 70, y=v.y_space + 200)

        height = tk.Label(text=v.height_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        height.place(x=v.x_distance, y=v.y_space + 250)
        input_height = tk.Entry(width=v.tool_rec_width)
        input_height.place(x=v.x_distance + 70, y=v.y_space + 250)

        weight = tk.Label(text=v.weight_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        weight.place(x=v.x_distance, y=v.y_space + 300)
        input_weight = tk.Entry(width=v.tool_rec_width)
        input_weight.place(x=v.x_distance + 70, y=v.y_space + 300)

        mail = tk.Label(text=v.mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        mail.place(x=v.x_distance + 420, y=v.y_space)
        input_mail = tk.Entry(width=v.tool_rec_width)
        input_mail.place(x=v.x_distance + 490, y=v.y_space)

        password = tk.Label(text=v.password_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        password.place(x=v.x_distance + 420, y=v.y_space + 50)
        input_password = tk.Entry(width=v.tool_rec_width, show="*")
        input_password.place(x=v.x_distance + 490, y=v.y_space + 50)

        doc_mail = tk.Label(text=v.doc_mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        doc_mail.place(x=v.x_distance + 420, y=v.y_space + 100)
        input_doc_mail = tk.Entry(width=v.tool_rec_width)
        input_doc_mail.place(x=v.x_distance + 490, y=v.y_space + 100)

        date = tk.Label(text=v.date_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        date.place(x=v.x_distance + 420, y=v.y_space + 150)
        date_bar = DateEntry(width=12, height=10, foreground=v.tool_date_rec_fg,
                             borderwidth=1,
                             locale="de_DE")
        date_bar.place(x=v.x_distance + 490, y=v.y_space + 150)

        game = tk.Label(text=v.game_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        game.place(x=v.x_distance + 420, y=v.y_space + 200)
        input_game = Combobox()
        input_game['values'] = ("A Oyunu", "B Oyunu", "C Oyunu", "D Oyunu")
        input_game.current(0)
        input_game.place(x=v.x_distance + 490, y=v.y_space + 200)

    def rec_clear_tool_function():
        date.place_forget()
        date_bar.place_forget()
        name.place_forget()
        input_name.place_forget()
        surname.place_forget()
        input_surname.place_forget()
        tc.place_forget()
        input_tc.place_forget()
        age.place_forget()
        input_age.place_forget()
        height.place_forget()
        input_height.place_forget()
        weight.place_forget()
        input_weight.place_forget()
        mail.place_forget()
        input_mail.place_forget()
        doc_mail.place_forget()
        input_doc_mail.place_forget()
        input_game.place_forget()
        game.place_forget()
        input_username_.place_forget()
        username_.place_forget()
        input_password.place_forget()
        password.place_forget()

    def record_back_button_function():
        if game_button_control_rec:
            game_button.place_forget()
        back_button_rec.place_forget()
        record_button_rec.place_forget()
        rec_clear_tool_function()
        entry()

    def regester_data_helper_function():
        global game_button_control_rec
        game_button_control_rec = op.recorded_data_control_block(date_bar.get(), input_username_.get(),
                                                                 input_name.get(),
                                                                 input_surname.get(),
                                                                 input_tc.get(),
                                                                 input_age.get(), input_height.get(),
                                                                 input_weight.get(),
                                                                 input_mail.get(),
                                                                 input_password.get(), input_doc_mail.get())

    entry_button_clear()
    rec_tool_function()
    rec_button_function()


def continue_tab():
    global game_button, game_button_control_con

    game_button_control_con = False

    def button_tool_function_con():
        global input_username_control_con, back_button_continue, username_con, input_username_control_con, continue_button

        back_button_continue = tk.Button(text=v.continue_back_buton_name, bg=v.continue_back_buton_color,
                                         font=v.continue_back_buton_write_type,
                                         command=back_button_con_function)
        back_button_continue.place(x=v.x_distance, y=600)
        back_button_continue.config(height=v.continue_back_buton_height, width=v.continue_back_buton_width)

        username_con = tk.Label(text=v.label_con_name, font=v.label_del_write_type,
                                fg=v.label_con_fg)
        username_con.place(x=250, y=150)

        input_username_control_con = Entry(ws, font=v.tool_con_write_type)
        input_username_control_con.place(x=450, y=160)

        continue_button = tk.Button(text=v.continue_continue_buton_name, bg=v.continue_continue_buton_color,
                                    font=v.continue_continue_buton_write_type,
                                    command=username_data_helper_funtion)
        continue_button.place(x=710, y=150)

    def continue_tool_function(username):
        global label0_d, label1, label2, label3

        label0_var = StringVar()

        label1 = tk.Label(text=v.label1_con_name, font=v.label_del_write_type, fg=v.label1_con_fg)
        label1.place(x=v.x_distance_c, y=v.y_space_c)

        label0_var.set(username)
        label0_d = Label(ws, textvariable=label0_var, font=v.label_del_write_type, fg=v.label1_con_fg)
        label0_d.place(x=v.x_distance_c + 150, y=v.y_space_c)

        label2 = tk.Label(text=v.label3_con_name, font=v.label_del_write_type, fg=v.label1_con_fg)
        label2.place(x=v.x_distance_c + 320, y=v.y_space_c)

        label3 = tk.Label(text=v.label2_con_name, font=v.label_del_write_type, fg=v.label1_con_fg)
        label3.place(x=v.x_distance_c, y=v.y_space_c + 38)

    def back_button_con_function():
        if game_button_control_con:
            game_button.place_forget()
            label0_d.place_forget()
            label1.place_forget()
            label2.place_forget()
            label3.place_forget()
        continue_tab_clear()
        back_button_continue.place_forget()
        entry()

    def continue_tab_clear():
        username_con.place_forget()
        input_username_control_con.place_forget()
        continue_button.place_forget()

    def username_data_helper_funtion():
        global game_button_control_con
        control = op.username_record_control_block(input_username_control_con.get(), 1)
        game_button_control_con = control
        if control:
            continue_tab_clear()
            game_button_function(2)
            continue_tool_function(input_username_control_con.get())
        else:
            pass

    entry_button_clear()
    button_tool_function_con()


def delete_tab():
    global button_control, update_tab_control

    button_control = False
    update_tab_control = False

    def update_delete_buton_function():
        global update_button, delete_button

        update_button = tk.Button(text=v.update_buton_name, bg=v.update_buton_color, font=v.update_buton_write_type,
                                  command=update_helper_functuion)
        update_button.place(x=240, y=300)
        update_button.config(height=v.update_buton_height, width=v.update_buton_width)

        delete_button = tk.Button(text=v.delete_tab_buton_name, bg=v.delete_tab_buton_color,
                                  font=v.delete_tab_buton_write_type,
                                  command=delete_helper_funtion)
        delete_button.place(x=540, y=300)
        delete_button.config(height=v.delete_tab_buton_height, width=v.delete_tab_buton_width)

    def button_tool_function_del():
        global username_control_del, input_username_control_del, back_button_del, continue_button_del, username_del

        back_button_del = tk.Button(text=v.delete_back_buton_name, bg=v.delete_back_buton_color,
                                    font=v.delete_back_buton_write_type,
                                    command=back_button_del_function)
        back_button_del.place(x=v.x_distance, y=600)
        back_button_del.config(height=v.delete_back_buton_height, width=v.delete_back_buton_width)

        username_del = tk.Label(text=v.label_del_name, font=v.label_del_write_type,
                                fg=v.label_del_fg)
        username_del.place(x=250, y=150)

        input_username_control_del = Entry(ws, font=v.tool_del_write_type)
        input_username_control_del.place(x=450, y=160)

        continue_button_del = tk.Button(text=v.delete_continue_buton_name, bg=v.delete_continue_buton_color,
                                        font=v.delete_continue_buton_write_type,
                                        command=username_data_helper_funtion)
        continue_button_del.place(x=710, y=150)

    def update_tool_function(username):
        global input_name_update, input_surname_update, input_tc_update, input_age_update, input_height_update, input_weight_update, input_mail_update, \
            input_doc_mail_update, name, surname, tc, age, height, weight, mail, doc_mail, input_username_update_, username_, \
            input_password_update, password, old_name, old_surname, old_tc, old_age, old_height, old_weight, old_mail, old_password, old_doc_mail

        record_data = op.user_information_block(username)
        old_name = record_data[2]
        old_surname = record_data[3]
        old_tc = record_data[4]
        old_age = record_data[5]
        old_height = record_data[6]
        old_weight = record_data[7]
        old_mail = record_data[8]
        old_password = record_data[9]
        old_doc_mail = record_data[10]

        name = tk.Label(text=v.name_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        name.place(x=v.x_distance, y=v.y_space)
        input_name_update = tk.Entry(width=v.tool_rec_width)
        input_name_update.place(x=v.x_distance + 70, y=v.y_space)
        input_name_update.insert(END, old_name)

        surname = tk.Label(text=v.surname_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        surname.place(x=v.x_distance, y=v.y_space + 50)
        input_surname_update = tk.Entry(width=v.tool_rec_width)
        input_surname_update.place(x=v.x_distance + 70, y=v.y_space + 50)
        input_surname_update.insert(END, old_surname)

        tc = tk.Label(text=v.tc_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        tc.place(x=v.x_distance, y=v.y_space + 100)
        input_tc_update = tk.Entry(width=v.tool_rec_width)
        input_tc_update.place(x=v.x_distance + 70, y=v.y_space + 100)
        input_tc_update.insert(END, old_tc)

        age = tk.Label(text=v.age_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        age.place(x=v.x_distance, y=v.y_space + 150)
        input_age_update = tk.Entry(width=v.tool_rec_width)
        input_age_update.place(x=v.x_distance + 70, y=v.y_space + 150)
        input_age_update.insert(END, old_age)

        height = tk.Label(text=v.height_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        height.place(x=v.x_distance, y=v.y_space + 200)
        input_height_update = tk.Entry(width=v.tool_rec_width)
        input_height_update.place(x=v.x_distance + 70, y=v.y_space + 200)
        input_height_update.insert(END, old_height)

        weight = tk.Label(text=v.weight_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        weight.place(x=v.x_distance, y=v.y_space + 250)
        input_weight_update = tk.Entry(width=v.tool_rec_width)
        input_weight_update.place(x=v.x_distance + 70, y=v.y_space + 250)
        input_weight_update.insert(END, old_weight)

        mail = tk.Label(text=v.mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        mail.place(x=v.x_distance + 420, y=v.y_space)
        input_mail_update = tk.Entry(width=v.tool_rec_width)
        input_mail_update.place(x=v.x_distance + 490, y=v.y_space)
        input_mail_update.insert(END, old_mail)

        password = tk.Label(text=v.password_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        password.place(x=v.x_distance + 420, y=v.y_space + 50)
        input_password_update = tk.Entry(width=v.tool_rec_width, show="*")
        input_password_update.place(x=v.x_distance + 490, y=v.y_space + 50)
        input_password_update.insert(END, old_password)

        doc_mail = tk.Label(text=v.doc_mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        doc_mail.place(x=v.x_distance + 420, y=v.y_space + 100)
        input_doc_mail_update = tk.Entry(width=v.tool_rec_width)
        input_doc_mail_update.place(x=v.x_distance + 490, y=v.y_space + 100)
        input_doc_mail_update.insert(END, old_doc_mail)

    def update_button_2_function():
        global update_button_2

        update_button_2 = tk.Button(text=v.update_buton2_name, bg=v.update_buton2_color,
                                    font=v.update_buton2_write_type)
        update_button_2.place(x=v.x_distance + 300, y=600)
        update_button_2.config(height=v.update_buton2_height, width=v.update_buton2_width,
                               command=update_variable_helper_function)

    def update_clear_tool_function():
        name.place_forget()
        input_name_update.place_forget()
        surname.place_forget()
        input_surname_update.place_forget()
        tc.place_forget()
        input_tc_update.place_forget()
        age.place_forget()
        input_age_update.place_forget()
        height.place_forget()
        input_height_update.place_forget()
        weight.place_forget()
        input_weight_update.place_forget()
        mail.place_forget()
        input_mail_update.place_forget()
        doc_mail.place_forget()
        input_doc_mail_update.place_forget()
        input_password_update.place_forget()
        password.place_forget()

    def back_button_del_function():
        if update_tab_control:
            update_clear_tool_function()
            update_button_2.place_forget()
        else:
            delete_tab_clear(1)
        back_button_del.place_forget()
        entry()

    def delete_helper_funtion():
        button_control = op.delete_block(input_username_control_del.get())
        if button_control:
            delete_tab_clear(2)
        else:
            pass

    def username_data_helper_funtion():
        global button_control
        button_control = op.username_record_control_block(input_username_control_del.get(), 1)
        if button_control:
            update_delete_buton_function()
        else:
            pass

    def delete_tab_clear(selection):
        global continue_button_del
        if selection == 1:
            continue_button_del.place_forget()
            input_username_control_del.place_forget()
            username_del.place_forget()
            if button_control:
                update_button.place_forget()
                delete_button.place_forget()
        elif selection == 2:
            update_button.place_forget()
            delete_button.place_forget()

    def update_variable_helper_function():
        status = op.update_query_block()
        if status:
            d.update_data(old_name, old_surname, old_tc, old_age, old_height, old_weight, old_mail, old_password,
                          old_doc_mail,
                          input_name_update.get(), input_surname_update.get(), input_tc_update.get(),
                          input_age_update.get(), input_height_update.get(),
                          input_weight_update.get(), input_mail_update.get(),
                          input_password_update.get(), input_doc_mail_update.get())
        else:
            pass

    def update_helper_functuion():
        global update_tab_control
        update_tab_control = True
        delete_tab_clear(1)
        update_tool_function(input_username_control_del.get())
        update_button_2_function()

    entry_button_clear()
    button_tool_function_del()


def scanning_tab():
    global button_control, tool_control, mail_tab_control

    button_control = False
    tool_control = False
    mail_tab_control = False

    def tool_function(username):
        global date, date_d, username_, username_d, name, name_d, surname, surname_d, tc, tc_d, age, age_d, \
            height, height_d, weight, weight_d, mail, mail_d, doc_mail, doc_mail_d, tool_title, subtittle, \
            table_date, exercise_status1, exercise_status2, exercise_status3

        record_data = op.user_information_block(username)

        username_var = StringVar()
        date_var = StringVar()
        name_var = StringVar()
        surname_var = StringVar()
        tc_var = StringVar()
        age_var = StringVar()
        height_var = StringVar()
        weight_var = StringVar()
        mail_var = StringVar()
        doc_mail_var = StringVar()

        tool_title = tk.Label(text=v.tool_title_name, font=v.tool_title_write_type, fg=v.tool_rec_fg)
        tool_title.place(x=300, y=80)

        subtittle = tk.Label(text=v.tool_subtitle_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        subtittle.place(x=v.x_distance_s - 20, y=v.y_space_s - 30)

        date = tk.Label(text=v.date_sc_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        date.place(x=v.x_distance_s - 20, y=v.y_space_s)
        date_var.set(record_data[0])
        date_d = Label(ws, textvariable=date_var, font=v.tool_write_type)
        date_d.place(x=v.x_distance_s + 35, y=v.y_space_s + 17)

        username_ = tk.Label(text=v.username_name, font=v.tool_write_type,
                             fg=v.tool_rec_fg)
        username_.place(x=v.x_distance_s + 120, y=v.y_space_s)
        username_var.set(record_data[1])
        username_d = Label(ws, textvariable=username_var, font=v.tool_write_type)
        username_d.place(x=v.x_distance_s + 195, y=v.y_space_s + 17)

        name = tk.Label(text=v.name_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        name.place(x=v.x_distance_s + 280, y=v.y_space_s)
        name_var.set(record_data[2])
        name_d = Label(ws, textvariable=name_var, font=v.tool_write_type)
        name_d.place(x=v.x_distance_s + 325, y=v.y_space_s)

        surname = tk.Label(text=v.surname_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        surname.place(x=v.x_distance_s + 280, y=v.y_space_s + 20)
        surname_var.set(record_data[3])
        surname_d = Label(ws, textvariable=surname_var, font=v.tool_write_type)
        surname_d.place(x=v.x_distance_s + 350, y=v.y_space_s + 20)

        tc = tk.Label(text=v.tc_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        tc.place(x=v.x_distance_s + 465, y=v.y_space_s)
        tc_var.set(record_data[4])
        tc_d = Label(ws, textvariable=tc_var, font=v.tool_write_type)
        tc_d.place(x=v.x_distance_s + 500, y=v.y_space_s)

        age = tk.Label(text=v.age_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        age.place(x=v.x_distance_s + 465, y=v.y_space_s + 20)
        age_var.set(record_data[5])
        age_d = Label(ws, textvariable=age_var, font=v.tool_write_type)
        age_d.place(x=v.x_distance_s + 510, y=v.y_space_s + 20)

        height = tk.Label(text=v.height_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        height.place(x=v.x_distance_s + 620, y=v.y_space_s)
        height_var.set(record_data[6])
        height_d = Label(ws, textvariable=height_var, font=v.tool_write_type)
        height_d.place(x=v.x_distance_s + 670, y=v.y_space_s)

        weight = tk.Label(text=v.weight_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        weight.place(x=v.x_distance_s + 620, y=v.y_space_s + 20)
        weight_var.set(record_data[7])
        weight_d = Label(ws, textvariable=weight_var, font=v.tool_write_type)
        weight_d.place(x=v.x_distance_s + 670, y=v.y_space_s + 20)

        mail = tk.Label(text=v.mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        mail.place(x=v.x_distance_s + 740, y=v.y_space_s)
        mail_var.set(record_data[8])
        mail_d = Label(ws, textvariable=mail_var, font=v.tool_write_type)
        mail_d.place(x=v.x_distance_s + 805, y=v.y_space_s)

        doc_mail = tk.Label(text=v.doc_mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        doc_mail.place(x=v.x_distance_s + 740, y=v.y_space_s + 20)
        doc_mail_var.set(record_data[10])
        doc_mail_d = Label(ws, textvariable=doc_mail_var, font=v.tool_write_type)
        doc_mail_d.place(x=v.x_distance_s + 805, y=v.y_space_s + 35)

        table_date = tk.Label(text=v.tool_title_date_name, font=v.table_title_write_type, fg=v.tool_rec_fg)
        table_date.place(x=v.x_distance_s, y=v.y_space_s + 80)

        exercise_status1 = tk.Label(text=v.tool_title_exercise1_name, font=v.table_title_write_type, fg=v.tool_rec_fg)
        exercise_status1.place(x=v.x_distance_s + 250, y=v.y_space_s + 80)

        exercise_status2 = tk.Label(text=v.tool_title_exercise2_name, font=v.table_title_write_type, fg=v.tool_rec_fg)
        exercise_status2.place(x=v.x_distance_s + 500, y=v.y_space_s + 80)

        exercise_status3 = tk.Label(text=v.tool_title_exercise3_name, font=v.table_title_write_type, fg=v.tool_rec_fg)
        exercise_status3.place(x=v.x_distance_s + 750, y=v.y_space_s + 80)

    def tool_clear_function():
        date.place_forget()
        date_d.place_forget()
        username_.place_forget()
        username_d.place_forget()
        name.place_forget()
        name_d.place_forget()
        surname.place_forget()
        surname_d.place_forget()
        tc.place_forget()
        tc_d.place_forget()
        age.place_forget()
        age_d.place_forget()
        height.place_forget()
        height_d.place_forget()
        weight.place_forget()
        weight_d.place_forget()
        mail.place_forget()
        mail_d.place_forget()
        doc_mail.place_forget()
        doc_mail_d.place_forget()
        tool_title.place_forget()
        subtittle.place_forget()
        table_date.place_forget()
        exercise_status1.place_forget()
        exercise_status2.place_forget()
        exercise_status3.place_forget()

    def table_create(username):
        global table_date_in, exercise_status1_in, exercise_status2_in, exercise_status3_in, tool_control, \
            table_date_list, exercise_status1_list, exercise_status2_list, exercise_status3_list

        delete_tab_clear(1)

        exercise_data = rd.return_exercise_data()
        tool_function(username)

        count = 0

        table_date_list = []
        exercise_status1_list = []
        exercise_status2_list = []
        exercise_status3_list = []
        for i in range(len(exercise_data)):

            if exercise_data[i][0] == username:
                table_date_in_var = StringVar()
                exercise_status1_in_var = StringVar()
                exercise_status2_in_var = StringVar()
                exercise_status3_in_var = StringVar()

                table_date_in_var.set(exercise_data[i][1])
                table_date_in = Label(ws, textvariable=table_date_in_var, font=v.tool_write_type)
                table_date_in.place(x=v.x_distance_s + 10, y=v.y_space_s + 120 + (20 * count))
                table_date_list.append(table_date_in)

                exercise_status1_in_var.set(exercise_data[i][2])
                exercise_status1_in = Label(ws, textvariable=exercise_status1_in_var, font=v.tool_write_type)
                exercise_status1_in.place(x=v.x_distance_s + 210, y=v.y_space_s + 120 + (20 * count))
                exercise_status1_list.append(exercise_status1_in)

                exercise_status2_in_var.set(exercise_data[i][3])
                exercise_status2_in = Label(ws, textvariable=exercise_status2_in_var, font=v.tool_write_type)
                exercise_status2_in.place(x=v.x_distance_s + 510, y=v.y_space_s + 120 + (20 * count))
                exercise_status2_list.append(exercise_status2_in)

                exercise_status3_in_var.set(exercise_data[i][4])
                exercise_status3_in = Label(ws, textvariable=exercise_status3_in_var, font=v.tool_write_type)
                exercise_status3_in.place(x=v.x_distance_s + 760, y=v.y_space_s + 120 + (20 * count))
                exercise_status3_list.append(exercise_status3_in)

                count = count + 1
                if count > 10:
                    count = 0
                tool_control = True

    def record_data_clear_function(table_date_list, exercise_status1_list, exercise_status2_list,
                                   exercise_status3_list):

        for date in table_date_list:
            date.destroy()
        for exercise_status1 in exercise_status1_list:
            exercise_status1.destroy()
        for exercise_status2 in exercise_status2_list:
            exercise_status2.destroy()
        for exercise_status3 in exercise_status3_list:
            exercise_status3.destroy()

    def scan_mail_button_function():
        global scan_button, mail_button

        scan_button = tk.Button(text=v.scan_buton_name, bg=v.update_buton_color, font=v.update_buton_write_type,
                                command=scan_helper_functuion)
        scan_button.place(x=240, y=300)
        scan_button.config(height=v.update_buton_height, width=v.update_buton_width)

        mail_button = tk.Button(text=v.mail_buton_name, bg=v.delete_tab_buton_color,
                                font=v.delete_tab_buton_write_type,
                                command=mail_helper_functuion)
        mail_button.place(x=540, y=300)
        mail_button.config(height=v.delete_tab_buton_height, width=v.delete_tab_buton_width)

    def button_tool_function_del():
        global username_control_del, input_username_control_scan, back_button_del, continue_button_del, username_del

        back_button_del = tk.Button(text=v.delete_back_buton_name, bg=v.delete_back_buton_color,
                                    font=v.delete_back_buton_write_type,
                                    command=back_button_del_function)
        back_button_del.place(x=v.x_distance, y=600)
        back_button_del.config(height=v.delete_back_buton_height, width=v.delete_back_buton_width)

        username_del = tk.Label(text=v.label_del_name, font=v.label_del_write_type,
                                fg=v.label_del_fg)
        username_del.place(x=250, y=150)

        input_username_control_scan = Entry(ws, font=v.tool_del_write_type)
        input_username_control_scan.place(x=450, y=160)

        continue_button_del = tk.Button(text=v.delete_continue_buton_name, bg=v.delete_continue_buton_color,
                                        font=v.delete_continue_buton_write_type,
                                        command=username_data_helper_funtion)
        continue_button_del.place(x=710, y=150)

    def mail_tool_function(username):
        global doctor_mail, input_doctor_mail, send_mail_1, input_send_mail_1, mail_tab_control

        record_data = op.user_information_block(username)
        old_doc_mail = record_data[10]

        doctor_mail = tk.Label(text=v.doctor_send_mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        doctor_mail.place(x=v.x_distance, y=v.y_space)
        input_doctor_mail = tk.Entry(width=v.tool_rec_width)
        input_doctor_mail.place(x=v.x_distance + 140, y=v.y_space)
        input_doctor_mail.insert(END, old_doc_mail)

        send_mail_1 = tk.Label(text=v.other_send_mail_name, font=v.tool_write_type, fg=v.tool_rec_fg)
        send_mail_1.place(x=v.x_distance, y=v.y_space + 40)
        input_send_mail_1 = tk.Entry(width=v.tool_rec_width)
        input_send_mail_1.place(x=v.x_distance + 140, y=v.y_space + 40)

        mail_tab_control = True

    def mail_tool_clear_function():
        doctor_mail.place_forget()
        input_doctor_mail.place_forget()
        send_mail_1.place_forget()
        input_send_mail_1.place_forget()

    def send_button_function():
        global send_button
        send_button = tk.Button(text=v.send_buton_name, bg=v.send_buton_color,
                                font=v.send_buton_write_type, command=mail_send_function)
        send_button.place(x=v.x_distance + 140, y=v.y_space + 80)

    def mail_helper_functuion():

        mail_control, password_control, doc_mail_control = op.mail_address_control_block(
            input_username_control_scan.get())
        status = op.exercise_record_control_block(input_username_control_scan.get())
        if status == 2:
            if mail_control and password_control:
                delete_tab_clear(1)
                mail_tool_function(input_username_control_scan.get())
                send_button_function()
        if status == 1:
            pass

    def mail_send_function():
        record_data = op.user_information_block(input_username_control_scan.get())
        op.mail_send_block(input_username_control_scan.get(), record_data[8], record_data[9],
                           input_doctor_mail.get(), input_send_mail_1.get())

    def scan_helper_functuion():
        status = op.exercise_record_control_block(input_username_control_scan.get())
        if status == 1:
            pass
        if status == 2:
            table_create(input_username_control_scan.get())

    def back_button_del_function():
        if mail_tab_control:
            mail_tool_clear_function()
            send_button.place_forget()
        delete_tab_clear(1)
        back_button_del.place_forget()
        entry()

    def delete_tab_clear(selection):
        global continue_button_del
        if selection == 1:
            continue_button_del.place_forget()
            input_username_control_scan.place_forget()
            username_del.place_forget()
            if button_control:
                scan_button.place_forget()
                mail_button.place_forget()
            if tool_control:
                tool_clear_function()
                record_data_clear_function(table_date_list, exercise_status1_list, exercise_status2_list,
                                           exercise_status3_list)
        elif selection == 2:
            update_button.place_forget()
            delete_button.place_forget()

    def username_data_helper_funtion():
        global button_control
        button_control = op.username_record_control_block(input_username_control_scan.get(), 1)
        if button_control:
            scan_mail_button_function()
        else:
            pass

    entry_button_clear()
    button_tool_function_del()


def game_button_function(selection):
    global game_button

    def helper_fonction0():
        game_funtion(1)

    def helper_fonction1():
        game_funtion(2)

    if selection == 1:
        game_button = tk.Button(text=v.game_buton_name, bg=v.game_buton_color, font=v.game_buton_write_type,
                                command=helper_fonction0)
        game_button.place(x=680, y=600)
        game_button.config(height=v.game_buton_height, width=v.game_buton_width)

    if selection == 2:
        game_button = tk.Button(text=v.game_buton_name, bg=v.game_buton_color, font=v.game_buton_write_type,
                                command=helper_fonction1)
        game_button.place(x=680, y=600)
        game_button.config(height=v.game_buton_height, width=v.game_buton_width)


def game_funtion(selection):
    global record_button_rec, back_button_continue, back_button_rec, \
        input_username_, input_username_control_con, username_table, rec_clear_tool_function

    def game_back_button_function():
        game_back_button.place_forget()
        tag.place_forget()
        entry()

    def game_tool_function():
        global game_back_button, tag

        tag = tk.Label(text="EGZERSİZ VERİLERİ TABLOYA KAYIT EDİLDİ", bg="red", fg="white", font='Verdana 30 bold')
        tag.place(x=50, y=300)

        game_back_button = tk.Button(text=v.game_back_buton_name, bg=v.game_back_buton_color,
                                     font=v.game_back_buton_write_type,
                                     command=game_back_button_function)
        game_back_button.place(x=400, y=600)
        game_button.config(height=v.game_back_buton_height, width=v.game_back_buton_width)

    time_ = time.time()
    date = str(datetime.datetime.utcfromtimestamp(time_).strftime('%Y-%m-%d %H-%M-%S'))

    if selection == 1:
        game_button.place_forget()
        record_button_rec.place_forget()
        back_button_rec.place_forget()
        rec_clear_tool_function()
        username_table = input_username_.get()

    if selection == 2:
        username_table = input_username_control_con.get()
        game_button.place_forget()
        back_button_continue.place_forget()
        label0_d.place_forget()
        label1.place_forget()
        label2.place_forget()
        label3.place_forget()

    op.game_data_record(username_table, date)
    game_tool_function()
