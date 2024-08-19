# import asyncio


# async def b():
#     result = 20 + 20
#     return result
#
#
# async def a():
#     result = await b()
#     return result


# print(asyncio.run(a()))

# class A:
#     async def add(self , num1 , num2):
#         return num1 + num2
#
#     async def cal(self):
#         result = await self.add(20,20)
#         return result

# print(asyncio.run(A().cal()))




# =================== file -> async open ===================
# import asyncio

# import aiofiles

# async def read():
#     async with aiofiles.open('test.txt' , 'r') as f:
#         data = await f.read()
#     return data

# def function():
#     asyncio.run(read())
# print(asyncio.run(read()))








