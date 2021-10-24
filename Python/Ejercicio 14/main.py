import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

send_mail = input("Who sends the mail: ")
password = input("Enter your password: ")
receive_mail = input("Who receives the mail: ")

message = MIMEMultipart("alternative")
message["Subject"] = input("Subject: ")
message["From"] = send_mail
message["To"] = receive_mail

text = input("Write your message: ")
text = MIMEText(text, "plain")

filename = input("Enter filename or path of file: ")
with open(filename, 'rb') as attachment:
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(attachment.read())

encoders.encode_base64(part2)
part2.add_header(
    "Content-Disposition",
     f"attachment; filename= {filename}",
     )

message.attach(text)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(send_mail, password)
    server.sendmail(
        send_mail, receive_mail, message.as_string()
        )
