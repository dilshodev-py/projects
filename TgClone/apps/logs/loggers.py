from logging import getLogger, Formatter, FileHandler, DEBUG
from os.path import join

from apps.utils.settings import BASE_URL

LOG_URL = join(BASE_URL , 'apps' ,'logs')

user_logger = getLogger('user_logs')
user_logger.setLevel(DEBUG)
user_handler=FileHandler(join(LOG_URL , 'user.log') , mode='a')
user_handler.setLevel(level=DEBUG)
f1=Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
user_handler.setFormatter(f1)
user_logger.addHandler(user_handler)



