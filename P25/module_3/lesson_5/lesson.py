"""revision"""
import time

"""
processing 
threading 
"""
# import multiprocessing


# def task1(num):
#     time.sleep(3)
#     print("Finish task1")
#
#
# def task2():
#     time.sleep(6)
#     print("Finish task2")
#
#
# def task3():
#     time.sleep(3)
#     print("Finish task3")
#
#
# def task4():
#     time.sleep(4)
#     print("Finish task3")



# ======================== process ========================

# task1()
# task2()
# task3()
# with multiprocessing.Pool(8) as p:
#     p.map(task1 , [1,2,3,4,5,6])
#
# start = time.time()
# tmp = []
# for i in [task1 , task2 , task3 , task4]:
#     p = multiprocessing.Process(target=i)
#     p.start()
#     tmp.append(p)
# for i in tmp:
#     i.join()
#
# print(time.time() - start)


# =============================== thread ======================

# import threading
#
# start = time.time()
# tmp = []
# for i in [(task1,10), task2, task3, task4]:
#     if isinstance(i , tuple):
#         t = threading.Thread(target=i[0] , args=(i[1],))
#     else:
#         t = threading.Thread(target=i)
#     t.start()
#     tmp.append(t)
#
# for i in tmp:
#     i.join()
# print(time.time() - start)


