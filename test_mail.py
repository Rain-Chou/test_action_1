import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'csmu05@gmail.com'
receiver = ['csmu2015@gmail.com','csmu05@gmail.com']
passwd = "bplu azwc whbd zrmx"


msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = Header("Test send email","utf-8").encode()

body = "Test send email"

msg_text=MIMEText(body)
msg.attach(msg_text)
c = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
    server.login(sender,passwd)
    server.sendmail(sender,receiver,msg.as_string())
print("success send mail!")

for msg in receiver:
    print(msg)