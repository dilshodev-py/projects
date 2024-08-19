# from os import getpid
# print(getpid())
# print(10)
# print(getpid())
# 1 process -> 1 main thread
import multiprocessing
import time
import threading
from os import getpid

from module_3.lesson_3.main import receiver_email

# main thread - > multi thread
# def function(num):
#     print(getpid())
#     time.sleep(2)
#     print(num)
# #
#
# start = time.time()
# values = [10, 20, 30, 40, 50, 60, 70]
# threads = []
# for i in values:
#     t1 = threading.Thread(target=function, args=(i,))
#     t1.start()
#     threads.append(t1)
# for thread in threads:
#     thread.join()
#
# print(time.time() - start)

#
# import time
# import threading
#
emails = [f"EMAIL{i}" for i in range(1, 1_000_001)]

number = [i for i in range(1 , 1000001 , 8500)]


# 3 secund

def send_email(receiver_email):
    time.sleep(3)
    print(f"Success send email ! {receiver_email}")

def split_process(number):
    import threading
    threads = []
    for i in emails[number: number+8500]:
        t = threading.Thread(target=send_email, args=(i,))
        t.start()
        threads.append(t)
    for i in threads:
        i.join()



#
# start = time.time()
# threads = []
# for i in emails:
#     t = threading.Thread(target=send_email , args=(i,))
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
# print(time.time() - start)



def add(a, b):
    time.sleep(3)
    print(a + b)


start = time.time()

with multiprocessing.Pool(118) as p:
    p.map(split_process , number)
print(time.time() - start)


# for i in emails:
#     p = multiprocessing.Process(target=send_email, args=(i,))
#     p.start()
#     processes.append(p)
# for i in processes:
#     i.join()
