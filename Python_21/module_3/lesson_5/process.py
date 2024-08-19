# import multiprocessing
# import os
# import time
#
# def a(num):
#     time.sleep(2)
#     print(num , os.getpid())

# start = time.time()
# with multiprocessing.Pool(60) as p:
#     p.map(a , range(1 , 120))
# print(time.time() - start)
# print("Finished !")
# start = time.time()
# process = []
# for i in [2,10]:
#     p = multiprocessing.Process(target=a , args=(i,))
#     p.start()
#     process.append(p)
#
# for pro in process:
#     pro.join()
# print(time.time() - start)

# print("Finished !")