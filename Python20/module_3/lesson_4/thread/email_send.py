# import threading
# import time
#
# emails = ['ime37me@gmail.com',
#           'stalker.yoqubov@gmail.com',
#           'sbekzod150@gmail.com',
#           'meintinker911@gmail.com',
#           'alisherravshanovuni@gmail.com',
#           'asliddinkutbiddinov1@gmail.com',
#           'clashakk2915@gmail.com',
#           'botir1791@gmail.com',
#           'shakhruh.rakhimov@gmail.com',
#           'normurodovakamola03@gmail.com',
#           'deo17ssssssssss@gmail.com',
#           'joraqoziyevmusoxon9@gmail.com']
#
# import smtplib, ssl
# def send_email(receiver_email):
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     sender_email = "absaitovdev@gmail.com"  # Enter your address
#     password = "xfjlatnnnxfhzylq"
#     message = f"""
#     Code : 123456"""
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)
#
# start = time.time()
# threads = []
# for i in emails:
#     th = threading.Thread(target=send_email , args = (i,))
#     th.start()
#     threads.append(th)
#
# for i in threads:
#     i.join()
# print(time.time() - start)
# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# data = response.json()
# print(data)
from math import ceil

print(len("justification."))

words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16

matrix = []
tmp = []
while words:
   i = words[0]
   if len(" ".join(tmp + [i])) <= maxWidth:
      tmp.append(i)
      words.pop(0)
      continue
   matrix.append(tmp.copy())
   tmp.clear()
if tmp:
   matrix.append(tmp.copy())


result = []
for i in matrix[:-1]:
   p = maxWidth - len("".join(i))
   t = ""
   if len(i) == 1:
      t += i[0]+" "*p
      result.append(t)
      continue
   sep = ceil(p / (len(i)-1))

   for index,j in enumerate(i):
      if sep <= p:
         sep = ceil(p / (len(i[index:]) - 1))
         t += j + " "*sep
         p -= sep
      else:
         t += j+" "*p
         p -= p
   result.append(t)

p = maxWidth - len(" ".join(matrix[-1]))
tmp = " ".join(matrix[-1]) + p*" "
result.append(tmp)


print(result)







# [
#    "This    is    an",
#    "example of text",
#    "justification.  "
# ]