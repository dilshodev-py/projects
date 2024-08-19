import random
from pathlib import Path

BASE_DIR = Path(__file__).parent


def send_email_code(receiver_email):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "absaitovdev@gmail.com"
    password = "xdaogcqthhoidbug"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    code = random.randrange(10**5 , 10**6)
    html = f"""
        <h1>code : {code}</h1>
    """
    part2 = MIMEText(html, "html")
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return code

class DB_Config:
    dbname = "todo_db"
    user = "postgres"
    host = "localhost"
    password = 1
    port = 5432
