from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/0')

@app.task
def hello():
    return 'hello world'

@app.task
def send_email(receiver_email):
    import smtplib, ssl
    port = 465
    password = "bzhsrmvtslqimkuw"
    sender_email = "absaitovdev@gmail.com"
    context = ssl.create_default_context()
    message = 'Hello World'

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email , message)