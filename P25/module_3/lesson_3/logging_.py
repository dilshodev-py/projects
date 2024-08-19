import logging

error = logging.Logger('error_log', level=40)
critical = logging.Logger('critical_log', level=50)

error_handler = logging.FileHandler('error.log', mode='a')
critical_handler = logging.FileHandler('critical.log',mode='a')

format = logging.Formatter("%(pathname)s %(lineno)d %(levelno)s %(levelname)s %(asctime)s %(message)s")

error_handler.setFormatter(format)
error_handler.setLevel(40)
critical_handler.setFormatter(format)
critical_handler.setLevel(50)

error.addHandler(error_handler)
critical.addHandler(critical_handler)

error.error("Error paydo bo'ldi")
critical.critical("Critical paydo bo'ldi")

# logging.basicConfig(filename='project.log',
#                     filemode='a',
#                     level=10,
#                     format="%(pathname)s %(lineno)d %(levelno)s %(levelname)s %(asctime)s %(message)s")

# a = int(input())
# b = int(input())

# try:
#     a / b
#     logging.info('Success')
# except ZeroDivisionError as m:
#     logging.critical(m)
