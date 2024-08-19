import logging

info_logger=logging.getLogger('info')
info_logger.setLevel(level=logging.INFO)
info_handler=logging.StreamHandler()
info_handler.setLevel(level=logging.INFO)
f1=logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
info_handler.setFormatter(f1)
info_logger.addHandler(info_handler)


# ===================================================

debug_logger=logging.getLogger('debug')
debug_logger.setLevel(level=logging.DEBUG)
debug_handler=logging.FileHandler(filename='logs/debug.log')
debug_handler.setLevel(level=logging.DEBUG)
f1=logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
debug_handler.setFormatter(f1)
debug_logger.addHandler(debug_handler)


# ==============================================

error_logger= logging.getLogger('error')
error_logger.setLevel(level=logging.ERROR)
error_handler=logging.FileHandler(filename='logs/error.log')
error_handler.setLevel(level=logging.ERROR)
f1=logging.Formatter("%(levelname)s-%(name)s - File : %(filename)s - Line: %(lineno)s -%(message)s- Time : %(asctime)s")
error_handler.setFormatter(f1)
error_logger.addHandler(error_handler)