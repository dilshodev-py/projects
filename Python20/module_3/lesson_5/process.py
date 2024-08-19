# import time
# from multiprocessing import Pool , Process

# import os , sys
# print(os.getpid())

# requests -> multiprocessing
# file     -> multiprocessing







# a= 7
# def function(arg):
#     with open("test.txt" ,"r") as f:
#         data = f.read()
#     data += "10"
#     with open('test.txt', "w") as f:
#         f.write(data)
#     print(os.getpid(), a)
#     time.sleep(2)

# start = time.time()
# with Pool(9) as p:
#     p.map(function,[1,2,3,4,5,6,7,8,9])
# print(time.time() - start)

#
# def function(arg):
#     print(os.getpid())
#     time.sleep(2)
#
# l = range(10)
# process = []
# start = time.time()
# for i in l:
#     p = Process(target=function , args=(i,))
#     p.start()
#     process.append(p)
# for i in process:
#     i.join()
# print(time.time() - start)


