import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('njsk9032@gmail.com', 'Nsai903.')

server.sendmail('njsk9032@gmail.com','jyothisai903@gmail.com','this is the mesg send using python code')

print('Mail sent')