# # import logging
# #
# #
# # logging.basicConfig(level=logging.ERROR ,filename="app.log" , filemode='a' , format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")
# # logging.error(f'This will get logged to a file : {__name__}')

# import logging
#
# logging.basicConfig(level=0,filename="log.json", filemode="a", format="%(name)s - %(levelname)s - %(message)s - %(asctime)s")
#
# logging.debug('This is a debug message') #        0
# logging.info('This is an info message') #         1
# logging.warning('This is a warning message') #    2
# logging.error('This is an error message') #       3
# logging.critical('This is a critical message') #  4


# logging_example.py

import logging

# Create a custom logger
debug_logger = logging.getLogger("debug")
info_logger = logging.getLogger("info")
warning_logger = logging.getLogger("warning")
error_logger = logging.getLogger("error")
critical_logger = logging.getLogger("critical")
debug_logger.setLevel(level=logging.DEBUG)
info_logger.setLevel(level=logging.INFO)
warning_logger.setLevel(level=2)
error_logger.setLevel(level=3)
critical_logger.setLevel(level=4)

# Create handlers
f_debug_handler = logging.FileHandler('debug.log')
f_info_handler = logging.FileHandler('info.log')
f_warning_handler = logging.FileHandler('warning.log')
f_error_handler = logging.FileHandler('error.log')
f_critical_handler = logging.FileHandler('critical.log')
f_debug_handler.setLevel(level=logging.DEBUG)
f_info_handler.setLevel(level=logging.INFO)
f_warning_handler.setLevel(level=2)
f_error_handler.setLevel(level=3)
f_critical_handler.setLevel(level=4)


# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_debug_handler.setFormatter(f_format)
f_info_handler.setFormatter(f_format)
f_warning_handler.setFormatter(f_format)
f_error_handler.setFormatter(f_format)
f_critical_handler.setFormatter(f_format)

# Add handlers to the logger
debug_logger.addHandler(f_debug_handler)
info_logger.addHandler(f_info_handler)
warning_logger.addHandler(f_warning_handler)
error_logger.addHandler(f_error_handler)
critical_logger.addHandler(f_critical_handler)


# debug_logger.debug("Debug level")
# info_logger.info("Info level")
# warning_logger.warning("warning level")
# error_logger.error("error level")
# critical_logger.critical("critical level")

"""
home work
    register(auth)
        email <- code 12354
        password
        code >>> 12354
    
"""