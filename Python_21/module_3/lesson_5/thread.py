# import os
# import threading
# import time
#
#
# def function(num) :
#     time.sleep(2)
#     print(10*num)
#     print("process id : ",os.getpid())
#
# start = time.time()
# threads = []
# for i in range(1,6):
#     t = threading.Thread(target=function , args=(i,))
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
# print(time.time() - start)





# def function1():
#     time.sleep(2)
#     print("function1")
#
# def function2():
#     time.sleep(3)
#     print("function2")
#
# def function3():
#     time.sleep(1)
#     print("function3")
#
# def function4():
#     time.sleep(5)
#     print("function4")

# t2 = threading.Thread(target=function , args=(2,))
# t3 = threading.Thread(target=function , args=(3,))
# t4 = threading.Thread(target=function , args=(4,))
# t5 = threading.Thread(target=function , args=(5,))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# print(time.time() - start)





