from email.message import EmailMessage 
from pwd import password

# SSL stands for Secure Sockets Layer and is designed to create secure connection between client and server.
import ssl

# Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.
import smtplib #https://www.tutorialspoint.com/python/python_sending_email.htm


sender = 'mnvcode@gmail.com'
myPwd = password

receiver = 'manavendrasingh676@gmail.com'

subject = 'Testing'

body = 'from python'

# Creating instance of our class EmailMessage
em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context

print("sending email")

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender,receiver,em.as_string())

print()

# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receiver, body)         
#    print ("Successfully sent email")
# except smtplib.SMTPException:
#    print ("Error: unable to send email") 