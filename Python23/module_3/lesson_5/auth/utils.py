import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def random_code():
    code = random.randrange(10 ** 5, 10 ** 6)
    return code


def send_email(receiver_email):
    code = str(random_code())
    sender_email = "absaitovdev@gmail.com"
    password = "xdaogcqthhoidbug"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    html = f"""
    <html>
      <body>
        <p>Hi,<br>
           Code : {code}
        </p>
      </body>
    </html>
    """
    part2 = MIMEText(html, "html")
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return code
