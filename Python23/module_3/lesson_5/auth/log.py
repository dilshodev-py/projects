import logging

user_logger = logging.Logger('user_log')
user_logger.setLevel(level=logging.INFO)
user_handler=logging.FileHandler(filename='users.log')
user_handler.setLevel(level=logging.INFO)
f1=logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
user_handler.setFormatter(f1)
user_logger.addHandler(user_handler)


main_logger = logging.Logger('user_log')
main_logger.setLevel(level=logging.ERROR)
main_handler=logging.FileHandler(filename='error.log')
main_handler.setLevel(level=logging.ERROR)
f1=logging.Formatter("%(levelname)s-%(name)s-%(pathname)s-%(lineno)d-%(message)s-%(asctime)s")
main_handler.setFormatter(f1)
main_logger.addHandler(main_handler)

