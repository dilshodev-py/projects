# async
# async(thread)
import asyncio
import time

async def task2():
    await asyncio.sleep(3)
    print("task2")
async def task3():
    await asyncio.sleep(4)
    print("task2")

async def task1(num , num1):
    await asyncio.sleep(3)
    await asyncio.gather(task2() , task3())
    print("task")


start = time.time()
asyncio.run(task1(1,2))
print(time.time()-start)
