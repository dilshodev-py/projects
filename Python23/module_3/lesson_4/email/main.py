import smtplib, ssl

port = 465  # For SSL Secure Sockets Layer
smtp_server = "smtp.gmail.com"
sender_email = "absaitovdev@gmail.com"  # Enter your address
receiver_email = "absaitovdev@gmail.com"  # Enter receiver address
password = "xdaogcqthhoidbug"
message = """Python sila """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)