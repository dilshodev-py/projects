import logging
from os.path import join
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent

base_log = join(BASE_PATH, "log")

user_logger = logging.getLogger("user")
user_logger.setLevel(level=logging.WARNING)

# handlers
user_handler = logging.FileHandler(filename=join(base_log , 'user.log'))
user_handler.setLevel(level=logging.WARNING)

# formats
f1 = logging.Formatter("%(name)s - %(levelname)s - %(message)s - %(asctime)s")


user_handler.setFormatter(f1)

user_logger.addHandler(user_handler)


