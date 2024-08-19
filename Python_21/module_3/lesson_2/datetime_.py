import datetime # module

now_datetime = datetime.datetime.now()  # now date time

print(now_datetime.strftime("%p"))
print(now_datetime.strftime("%X")) # time

str_datetime = "2024-01-01 12:12:12.123"
date_time = datetime.datetime.fromisoformat(str_datetime)
print(date_time.strftime('%A')) # monday

tuple_date = (2024 , 8 , 10 , 2 , 12 , 45)
d = datetime.datetime(*tuple_date)
print(d)

import time
# 1970-01-01
print(datetime.date.today() - datetime.date(1970, 1, 1))
secund = time.time()
date = datetime.date.fromtimestamp(secund)
print(date)



