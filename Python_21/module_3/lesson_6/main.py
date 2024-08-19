""""""
from multiprocessing import Pool

"""
rivision
    Multithreading
        1 main thread
        1 process
        inf thread
    
    Multiprocessing
        inf process (1 main thread)
        inf thread
        
    ToDo
"""


# import time
# from threading import Thread
# from multiprocessing import Process, Pool


# def a(arg):
#     time.sleep(2)
#     print(arg)

# def write_file(data):
#     time.sleep(1)
#     with open('test.txt', 'a') as f:
#         f.write(data+"\n")

# s = time.perf_counter()
# for i in range(1,101):
#     a(10)
# threads = []
# for i in range(1,101):
#     t = Thread(target=write_file, args=(str(i),))
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
# print(time.perf_counter()-s)


# def write_file(data):
#     time.sleep(1)
#     with open('test.txt', 'a') as f:
#         f.write(data+"\n")
# s = time.time()
# prosecces = []
# for i in range(1,10001):
#     p = Process(target=write_file , args=(str(i),))
#     p.start()
#     prosecces.append(p)
# for i in prosecces:
#     i.join()
# print(time.time() - s)


# s = time.time()
# with Pool(10) as p:
#     p.map(write_file , map(str , ))
# #
# print(time.time()- s)


# def a(args):
#     print(args[0] + args[1])

# with Pool(8) as p:
#     p.map(a, [(1, 2), (3, 4)])

# 3 soat
