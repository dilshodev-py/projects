# import multiprocessing
# import os
# import time
#
#
# def task1(nums):
#     time.sleep(2)
#     print(os.getpid())
#     print(f'task1 success finished {nums}')

#
# start = time.time()

# version - 1
# p1 = multiprocessing.Process(target=task1)
# p2 = multiprocessing.Process(target=task1)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# version -2
# processing_list = []
# for i in range(2):
#     p = multiprocessing.Process(target=task1)
#     p.start()
#     processing_list.append(p)
# for p in processing_list:
#     p.join()

# version -3

# with multiprocessing.Pool(100) as pool:
#     pool.map(task1, list(range(1,1000)))



# end = time.time()
# print(end - start)