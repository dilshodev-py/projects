import asyncio
# import json
# import time
# from multiprocessing import Pool, Process
# import aiofiles
# import httpx

# l = ["todos", "users", "photos", "albums", "posts", "comments"]



# async def get_(url_name):
#     async with httpx.AsyncClient() as f:
#         data = await f.get(f"https://jsonplaceholder.typicode.com/{url_name}")
#
#     data_json = json.dumps(data.json(), indent=3)
#     async with aiofiles.open(f"{url_name}.json" , "w") as f:
#         await f.write(data_json)
#
# async def task():
#     await asyncio.gather(*[get_(i) for i in l])
#
#
# start = time.time()
# asyncio.run(task())
# print(time.time()- start)


# start = time.time()
# with Pool(3) as p:
#     p.map(get_ , l)
# print(time.time() - start)

# processes = []
# for i in l:
#     p = Process(target=get_ , args= (i,))
#     p.start()
#     processes.append(p)
#
# for i in processes:
#     i.join()

