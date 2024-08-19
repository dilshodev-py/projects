# import json
# import requests # alt + enter + enter
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# posts = response.json()
# for i in posts:
#     print(i)


"""
        request - so'ro'v
        
        request protocol 4 ta :
            get     API dan olish
            post    API ga yuborish
            delete  API dan o'chirish
            patch   API dan qisman o'zgartirish 
            put     API to'liq o'rgartirish
            

"""

# 2-task
# import requests
#
# data = requests.get("https://dummyjson.com/users").json()
# users = data.get("users")
# amount = 0
# for user in users:
#     amount += user.get('age')
# print(amount)


# ============== httpx ===================



# async def get_data(link):
#     async with httpx.AsyncClient() as client:
#         data = await client.post(link)
#     return data.json()
#
#
# data = asyncio.run(get_data("https://dummyjson.com/users"))
# amount = 0
# for user in data.get("users"):
#     amount += user.get("age")
# print(amount)


# ===============================

# https://telegra.ph/file/2336fdc70f4400b7e6b84.png

# import asyncio
# import aiofiles
# import httpx
# async def task1():
#     link = "https://telegra.ph/file/08302bb718370f2b47be9.png"
#     async with httpx.AsyncClient() as client:
#         data = await client.post(link)
#
#     async with aiofiles.open("python.png" , 'wb') as f:
#         await f.write(data.content)
#
# asyncio.run(task1())



