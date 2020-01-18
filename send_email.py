import os
import smtplib
from email.message import EmailMessage
import time

# separate sensitives info from the code using os env variables
# generate a password for email in https://myaccount.google.com/apppasswords
# define params in user variables
# get infos from windows user variable

EMAIL_SRC = os.environ.get('EMAIL_ADRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASSWORD')

# using email message var
msg=EmailMessage()
msg['From']=EMAIL_SRC
msg['To']='ouahabimohammedlamine@yandex.com'
msg['Subject']='test html sending ...'
msg.set_content('How are you Amine?')

""" files=['resume/photo.jpg','resume/cv-v6.pdf']
for file in files :
    with open(file,'rb') as f :
        file_data=f.read()
        file_name=f.name
    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name) """
#Sending html script as content
''' 
msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>hello</h1>
    <p>sending html as email</p>
</body>
</html>
    """,subtype='html')
###############################'''

def SendEmailfromGmailServerSSL(_msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SRC, EMAIL_PASS)        
        smtp.send_message(_msg)


#using Debugging email Server
# # python -m smtpd -c DebuggingServer -n Localhost:1025     
def SendDebuggingEmailServer(_msg):
    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(_msg)

def main():
    i=1
    while True:
        del msg['Subject']  
        msg['Subject']='{} email sended...'.format(i)
        print( msg['Subject'] )
        SendDebuggingEmailServer(msg)
        SendEmailfromGmailServerSSL(msg)        
        time.sleep(30) #pause 5mn
        i=i+1
        


#check if its run locally not imported
if __name__ == '__main__':
    main()



