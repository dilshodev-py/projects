import os
import threading
import time


def task1():
    time.sleep(2)
    print(f"Finished task1 - {os.getpid()}")
def task2():
    time.sleep(3)
    print(f"Finished task2 - {os.getpid()}")
def task3():
    time.sleep(1)
    print(f"Finished task3 - {os.getpid()}")

def task4():
    time.sleep(4)
    print(f"Finished task4 - {os.getpid()}")

# start = time.time()
# task1()
# task2()
# task3()
# task4()

# thread1 = threading.Thread(target=task1 )
# thread2 = threading.Thread(target=task2 )
# thread3 = threading.Thread(target=task3 )
# thread4 = threading.Thread(target=task4 )
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()

threads = []
start = time.time()
for i in [task1 , task2 , task3 , task4]:
    t = threading.Thread(target=i)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
#
#
# end = time.time()
# print(end-start)


# threads = []
# start = time.time()
# for i in range(100):
#     t = threading.Thread(target=task4)
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
#
# end = time.time()
# print(end - start)













