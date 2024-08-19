import threading
import time
a = 9

def function(sec):
    global a
    a += 1
    print(a)
    time.sleep(sec)



l = [2,2,4,6,1]

# main thread
start = time.time()
threads = []
for i in l:
    th = threading.Thread(target=function , args = (i,))
    th.start()
    threads.append(th)
for i in threads:
    i.join()
# th1 = threading.Thread(target=function , args=(2,))
# th2 = threading.Thread(target=function , args=(2,))
# th3 = threading.Thread(target=function , args=(4,))
# th4 = threading.Thread(target=function , args=(20,))
# th5 = threading.Thread(target=function , args=(1,))
# th1.start()
# th2.start()
# th3.start()
# th4.start()
# th5.start()
# th1.join()
# th2.join()
# th3.join()
# th4.join()
# th5.join()
# function(2) # 2
# function(2) # 2
# function(4) # 4
# function(6) # 6
# function(1) # 1
print(time.time() - start)

# time : 15 sek