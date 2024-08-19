# async   - paralelik
# syncron - ketma ketlik
# import asyncio
# import time

# async - (thread, process)

# async def test1(num):
#     print('test1 start')
#     await asyncio.sleep(3)
#     print('test1 end')
#     print(num + 10)
#
# async def test2(num):
#     print('test2 start')
#     await asyncio.sleep(2)
#     print('test2 end')
#     print(num + 10)
#
# async def test3(num):
#     print('test3 start')
#     await asyncio.sleep(4)
#     print('test3 end')
#     print(num + 10)
#
#
# async def tasks():
#     time.sleep(2)
#     await asyncio.gather(test1(1) , test2(2), test3(3))
#
# start = time.time()
# asyncio.run(tasks())
# end = time.time()
# print(end - start)










