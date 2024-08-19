import logging

# logging.basicConfig(filename="test.logs", level=logging.NOTSET, format="%(levelname)s - %(message)s %(asctime)s")
#
# logging.info("This is a info message !")
# logging.critical("This is a critical message !")
# logging.error("This is a error message !")
# logging.debug("This is a debug message !")
# logging.warning("This is a warning message !")

# Logger(info)
# Logger(debug)
# Logger(warning)
# Logger(error)
# Logger(critical)
info_logger = logging.getLogger("info")
info_logger.setLevel(level=logging.INFO)
info_handler = logging.FileHandler(filename='info.log')
info_handler.setLevel(level=logging.INFO)
f1 = logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
info_handler.setFormatter(f1)
info_logger.addHandler(info_handler)

info_logger.info("Success !")



debug_logger = logging.getLogger("debug")
debug_logger.setLevel(level=10)
debug_handler = logging.StreamHandler()
debug_handler.setLevel(level=10)
f1 = logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
debug_handler.setFormatter(f1)
debug_logger.addHandler(debug_handler)

debug_logger.debug("Debug success !")






base_log = "/home/dilshod/PycharmProjects/Python_21/module_3/lesson_3/logging_/logs/"
info_logger = logging.getLogger("info")
debug_logger = logging.getLogger("debug")
info_logger.setLevel(level=logging.INFO)
debug_logger.setLevel(level=10)

info_logger.info("Success !")




# handlers
info_handler = logging.FileHandler(filename=base_log+'info.log')
debug_handler = logging.FileHandler(filename=base_log+'debug.log')
info_handler.setLevel(level=logging.INFO)
debug_handler.setLevel(level=10)



# formats
f1 = logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
f2 = logging.Formatter("%(levelname)s-%(name)s-%(message)s")

info_handler.setFormatter(f1)
debug_handler.setFormatter(f2)

info_logger.addHandler(info_handler)
debug_logger.addHandler(debug_handler)



info_logger.info("Success !")
debug_logger.debug("Debug success !")







