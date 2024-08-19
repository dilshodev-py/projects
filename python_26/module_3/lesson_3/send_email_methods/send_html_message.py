import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "absaitovdev@gmail.com"
receiver_email = "absaitovdev@gmail.com"
password = "zigntrldavncsspa"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
        <img src="https://telegra.ph/file/08302bb718370f2b47be9.png" alt="">
       <a href="http://t.me/absaitov_dilshod">My telegram</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())