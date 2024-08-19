import asyncio
import aiofiles
import json

# with open('revision.txt', 'r') as f:
#     f.read()


# async def read_file():
#     async with aiofiles.open('revision.txt', 'w') as f:
#         text = await f.read()
#     print(text)
#
# asyncio.run(read_file())

# ============================================
# async def read_file():
#     async with aiofiles.open('users.json', 'r') as f:
#         data = await f.read()
#         data = json.loads(data)
#     print(data)
#
# asyncio.run(read_file())


# =================================================



"""
            requests
            
            GET     <- (link)
            POST    -> (link , data)
            PATCH   -> (link , data)
            PUT     -> (link , data)
            DELETE  -> (link , data)
"""

import httpx

#
# response = httpx.get('https://telegra.ph/file/958ca22356a11a5215a00.png')
#
# bytes_text = response.content
# with open("img1.png" , 'wb') as f:
#     f.write(bytes_text)


async def get_and_writefile():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://telegra.ph/file/00a50a39fc5e172f45857.png')
    bytes_text = response.content
    async with aiofiles.open("img1.png" , 'wb') as f:
        await f.write(bytes_text)

asyncio.run(get_and_writefile())

# async(thread + process)

# async def g():
#     result = 10 + 10
#     return result

# print(asyncio.run(g()))

# ================================================

# async def test1():
#     return 'Test1'
#
#
# async def test2():
#     result = await test1()
#     print("test2")
#     return result
#
#
# print(asyncio.run(test2()))


# =================================================
# import time
#
#
# async def test1():
#     await asyncio.sleep(2)
#     print('test1')
#
#
# async def test2():
#     await asyncio.sleep(4)
#     print("test2")
#
#
# async def main():
#     await asyncio.gather(test1() ,test2())
#     print("finish")

# start = time.time()
# asyncio.run(main())
# print(time.time() - start)

# a = [1,2,3,4,5,6]

# class A:
#     def __init__(self , a):
#         self.a = a
#
#     async def a_print(self):
#         await self.is_valid()
#         print(self.a)
#
#     async def is_valid(self):
#         # logic
#         pass

# web scrap





