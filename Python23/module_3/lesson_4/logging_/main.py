import logging
#
# logging.basicConfig(filename='test.log' , filemode='a' ,level=10 ,
#                     format='%(levelname)s - %(name)s -Filename: %(filename)s %(lineno)d -> %(message)s -Time : %(asctime)s', datefmt="%y")
#
#
# def div(num1 , num2):
#     try:
#         result = num1 / num2
#         logging.info("Success divided !")
#         return result
#     except :
#         logging.error("Zero devision error")
#
# print(div(1, 2))


# logging.debug('This is Debug')         # 1024
# logging.info('This is info')           # 20
# logging.warning('This is warning')     # 30
# logging.error('This is error')         # 40
# logging.critical('This is critical')   # 50
from module_3.lesson_4.logging_.logger import info_logger, error_logger


def div(num1 , num2):
    try:
        result = num1 / num2
        info_logger.info("Success divided !")
        return result
    except :
        error_logger.error("Zero devision error")

print(div(1, 0))





