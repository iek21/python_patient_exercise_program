import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from tkinter import messagebox

from settings import Variables

v = Variables()


def mail(mail_adress, pasword, doctor_mail, other_mail):
    global message, receiver_address1, receiver_address2
    mail_content = v.mail_text
    sender_address = mail_adress
    sender_pass = pasword
    control = True
    status = 0

    if doctor_mail:
        if other_mail:
            receiver_address1 = other_mail
            receiver_address2 = doctor_mail

            message = MIMEMultipart()
            message["To"] = receiver_address1
            message["To"] = receiver_address2
            message["Subject"] = v.mail_topic
            status = 1

    if not doctor_mail:
        if other_mail:
            receiver_address1 = other_mail
            message = MIMEMultipart()
            message["To"] = receiver_address1
            message["Subject"] = v.mail_topic
            status = 2
    if not other_mail:
        if doctor_mail:
            receiver_address2 = doctor_mail
            message = MIMEMultipart()
            message["To"] = receiver_address2
            message["Subject"] = v.mail_topic
            status = 3
    if not other_mail:
        if not doctor_mail or doctor_mail == "Girilmedi":
            control = False
            messagebox.showinfo(v.unsuccessful_message, v.mail_unsuccsessful_message3)

    if control:
        try:
            message.attach(MIMEText(mail_content, "plain"))
            attach_file_name = v.excel_file_name
            attach_file = open(attach_file_name, "rb")
            payload = MIMEBase("application", "octate-stream")
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header("Content-Disposition", "attachment", filename=attach_file_name)
            message.attach(payload)
            session = smtplib.SMTP("smtp.gmail.com", 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            if status == 1:
                session.sendmail(sender_address, receiver_address1, text)
                session.sendmail(sender_address, receiver_address2, text)
            if status == 2:
                session.sendmail(sender_address, receiver_address1, text)
            if status == 3:
                session.sendmail(sender_address, receiver_address2, text)
            session.quit()
            messagebox.showinfo(v.successful_message,
                                v.mail_succsessful_message)
        except:
            messagebox.showinfo(v.unsuccessful_message,
                                v.mail_unsuccsessful_message)
