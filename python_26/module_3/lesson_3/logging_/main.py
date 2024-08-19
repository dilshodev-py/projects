# import logging
#
# logging.basicConfig(level=logging.DEBUG ,
#                     format="%(name)s:%(message)s:%(levelname)s-%(asctime)s-%(pathname)s-%(lineno)d:%(created)f" ,
#                     datefmt="%Y-%m-%d %H:%M",
#                     filename="/home/dilshod/PycharmProjects/python_26/module_3/lesson_2/app.log",
#                     filemode='a')
#
#
# logging.debug("This is a debug message")  # 10
# logging.info("This is an info message") # 20
# logging.warning("This is a warning message") # 30
# logging.error("This is an error message") # 40
# logging.critical("This is a critical message") # 50


import logging
from os.path import join
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.parent

user_logger = logging.getLogger("User")
user_logger.setLevel(10)
console_handler = logging.FileHandler(filename=join(BASE_DIR, 'module_3' , 'lesson_2', 'log' , 'user_logging.log'),mode='a')
console_handler.setLevel(10)
user_logger.addHandler(console_handler)
formatter = logging.Formatter("{asctime} - {levelname} - {message}",datefmt="%Y-%m-%d %H:%M" ,style="{")
console_handler.setFormatter(formatter)


product_logger = logging.getLogger("Product")
product_logger.setLevel(10)
console_handler = logging.FileHandler(filename=join(BASE_DIR, 'module_3' , 'lesson_2', 'log' , 'product_logging.log'),mode='a')
console_handler.setLevel(10)
product_logger.addHandler(console_handler)
formatter = logging.Formatter("{asctime} - {levelname} - {message}",datefmt="%Y-%m-%d %H:%M" ,style="{")
console_handler.setFormatter(formatter)

