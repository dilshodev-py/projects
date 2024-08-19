# import threading
# import time
# import os
# import requests


# response = requests.get('https://jsonplaceholder.typicode.com/users')
# print(response.json())



# print(os.getpid())
# # jarayoy - process -> main thread
#
#
# def function1(num1 , num2):
#     time.sleep(1)
#     print(f"Function1 -> {os.getpid()}")
# def function2(num1 , num2):
#     time.sleep(1)
#     print(f"Function2 - {os.getpid()}")
#
# def function3(num1 , num2):
#     time.sleep(1)
#     print(f"Function3 - {os.getpid()}")
#
# def function4(num1 , num2):
#     time.sleep(1)
#     print(f"Function4 - {os.getpid()}")

# # start = time.time()
# # function1()
# # function1()
# # function1()
# # function1()
# # print(time.time() - start)
#
# start = time.time()
# tasks = [(function1 , (1,2)) , (function2 , (2,3)) , (function3 , (1,2)) , (function4 , (1,2))]
# threads = []
# for func, args in tasks:
#     t = threading.Thread(target=func , args=args)
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
# # t1 = threading.Thread(target=function1 , args=(1,2))
# # t2 = threading.Thread(target=function2 , args=(1,2))
# # t3 = threading.Thread(target=function3 , args=(1,2))
# # t4 = threading.Thread(target=function4 , args=(1,2))
# #
# # t1.start()
# # t2.start()
# # t3.start()
# # t4.start()
# #
# # t1.join()
# # t2.join()
# # t3.join()
# # t4.join()
# print(time.time()- start)


# =========================================================


# import multiprocessing
#
# def a(num):
#     time.sleep(2)
#     print(f"{num} {os.getpid()}")
#
#
# if __name__ == '__main__':
#
#
#     proccess = []
#     for i in range(10000):
#         p = multiprocessing.Process(target=a , args=(i,))
#         p.start()
#         proccess.append(p)
#
#     for p in proccess:
#         p.join()


# file

# python -> asyncfile , httpx , .....

# import multiprocessing

# def a(num):
#     time.sleep(2)
#     print(f"{num} {os.getpid()}")


# start = time.time()
# with multiprocessing.Pool(8) as p:
#     p.map(a , list(range(10)))
# print(time.time()-start









