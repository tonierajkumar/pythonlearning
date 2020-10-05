import smtplib

to = input("Enter the to address for the email:\n")
content = input("Enter the content for the email")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("tonierajkumar@gmail.com",'tonie$1234')
    server.sendmail('mchristy01@gmail.com',to,content)
    server.close()

sendEmail(to,content)
