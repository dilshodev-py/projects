import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randrange


def send_email(receiver_email : str):

    code = randrange(10 ** 5, 10 ** 6)
    sender_email = "absaitovdev@gmail.com"
    password = "kwpskboqqtcvbvnp"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Confirmation"
    message["From"] = sender_email
    message["To"] = receiver_email
    html = f"""
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <h1>code : {code}</h1> 
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



