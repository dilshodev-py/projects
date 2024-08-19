""" ---------------------- function ----------------------"""
# import math
#
# class User:
#     pass
#
# def name(arg1 = 1,/,*,  arg2 = None) -> User:
#     # logic
#     """bu function name nomli function"""
#     """bu function name nomli function"""
#     return
#     yield
#
# print(name.__doc__)
import json

from bs4 import BeautifulSoup

""" ---------------------- iterable ----------------------"""

# list
# str
# tuple
# set
# dict
#
#
# class Other:
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         pass


""" ---------------------- iterator ----------------------"""

# iter()
# next()
#
# for i in [1, 2, 3, 4]:
#     pass

""" ---------------------- generator ----------------------"""

# def test():
#     yield
#
# xotiradan kam joy egalidi
# tezroq ishlidi
# index yo'q

# p = map(func , iterable)
# p = filter(func , iterable)

""" ---------------------- decorator ----------------------"""

# def decorator_name(arg):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             # logic -> check
#             result = function(*args, **kwargs)
#             return result
#         return wrapper
#     return inner
#
#
# @decorator_name(10)
# @decorator_name(10)
# @decorator_name(10)
# @decorator_name(10)
# @decorator_name(10)
# def text():
#     pass

""" ---------------------- json ----------------------"""

# loads
# dumps
# load
# dump

# loads
# dumps

# a = [1,2,3,4,5]
# a = json.dumps(a)
# a=  json.loads(a)
# print(type(a))
# object uchun kerak


# for file
# load
# dump


""" ---------------------- thread ----------------------"""
# from threading import Thread
#
# # 1 jarayonda -> asosiy oqimni bir nechta oqimlarga bo'lish
#
# t = Thread(target=func1 , args=(1,))
# t = Thread(target=func2 , args=(1,))
# t = Thread(target=func3 , args=(1,))
# t = Thread(target=func4 , args=(1,))
# t = Thread(target=func5 , args=(1,))
# t = Thread(target=func6 , args=(1,))
# t = Thread(target=func7 , args=(1,))
#
# t.start()
# t.start()
# t.start()
# t.start()
# t.start()
# t.start()
# t.start()
#
# t.join()
# t.join()
# t.join()
# t.join()
# t.join()
# t.join()
# t.join()
# t.join()

# l = [(funct1 , (1,2,3)) , (funct1 , (1,2,3))]
#
# tmp = []
# for func , args in l:
#     T = Thread(target=func , args= args)
#     T.start()
#     tmp.append(T)
#
# for t in tmp:
#     t.join()

""" ---------------------- Process ----------------------"""
from multiprocessing import Process, Pool

# ko'p jarayon yaratish


# l = [(funct1 , (1,2,3)) , (funct2 , (1,2,3))]
#
# tmp = []
# for func , args in l:
#     T = Process(target=func , args= args)
#     T.start()
#     tmp.append(T)
#
# for t in tmp:
#     t.join()

# with Pool(4) as p:
#     p.map(func=fucn , iterable=[(1,2) , (1,2)])

# IO - Input Output

""" ---------------------- async ----------------------"""
# async -> thread , process

# requests
# aiofiles
# httpx
import httpx


# async
# async def test():
#     async with httpx.AsyncClient() as client:
#         response = await client.get(link, data)
#
# web = "https://kun.uz"


# # page 1


# html = httpx.get(web).content
# soup = BeautifulSoup(html , 'html.parser')
# url = soup.find('a' , {"class" : 'small-news__title'})['href']
#
# # page 2
# html = httpx.get(web + url).content
# soup = BeautifulSoup(html , 'html.parser')
# tmp = soup.find('div' , {"class" : "single-content"})
# print(tmp.text)

