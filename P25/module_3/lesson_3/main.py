# import calendar

# yy = 2017
# mm = 11
# print(calendar.calendar(yy))

# import calendar

# obj = calendar.Calendar()

# for day in obj.monthdatescalendar(2024, 12):
#     print(day)

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2006, 9, 11 )
# tmp = datetime.datetime.now() - x
# print(datetime.date.fromordinal(tmp.days))


# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime("%A , %d-%B , %Y"))

# 1970-01-01
# print(datetime.datetime.now().timestamp())
# print(datetime.datetime.utcfromtimestamp(1717844620))

# import smtplib, ssl
#
# port = 465
# password = "bzhsrmvtslqimkuw"
# sender_email = "absaitovdev@gmail.com"
# receiver_email = "ismoilovabdulaziz127@gmail.com"
# context = ssl.create_default_context()
# message = 'Hello World'
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email , message)






