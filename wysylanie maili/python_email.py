import smtplib
import ssl



address = 'smtp.gmail.com'
port = 587
login= 'hrryniu@gmail.com'
app_password= ''

smtpObj = smtplib.SMTP(address,port)

print(smtpObj.ehlo())

code,msg = smtpObj.ehlo()

if code == 250:
    smtpObj.login(login, password)
    if code == 235:
        smtpObj.sendmail('mail nadawcy',
                         'mail odbiorct',
                         """Subject: Hej\n
                         Co u Ciebie? To jest test.\n
                         Dlaczego nie odpisujesz?
                          
                           """
                        )
        smtpObj.quit()
    else:
        print(code,msg)
        



else:
    print(code,msg)