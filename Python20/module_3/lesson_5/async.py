import asyncio
# async IO

# project - > def()  10000
# project - > async def()  10000000



# async def function1(num):
#     return num
#
#
# async def function2(num):
#     return await function1(num)
#
# def add():
#     return asyncio.run(function2(10))
#
#
# print(add())
import time


# async def task1():
#     print("start task1") # 1
#     await asyncio.sleep(2)
#     print("end task1") # 5
#
# async def task2():
#     print("start task2") # 2
#     await asyncio.sleep(1)
#     print("end task2") # 4
#
# async def task3():
#     print("start task3") # 3
#     await asyncio.sleep(3)
#     print("end task3") # 6
#
#
# async def function():
#     await asyncio.gather(task1() , task2(), task3())
#     # await task1()
#     # await task2()
#     print("stop")
#
# asyncio.run(function())

# project -> async

import aiofiles
import httpx

# async def request_get():
#     async with httpx.AsyncClient() as client:
#         data = await client.get("https://jsonplaceholder.typicode.com/posts")
#     return data.json()


# print(asyncio.run(request_get()))
# async def read_data():
#     async with aiofiles.open("test.txt" , 'r') as f:
#         return await f.read()
#
#
# print(asyncio.run(read_data()))



