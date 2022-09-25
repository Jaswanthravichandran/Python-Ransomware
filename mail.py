import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('hackmertestme@gmail.com','testmejash123')

server.send('hackmertestme@gmail.com','jaswanthr49839@gmail.com','hello')

print('mail sent..')