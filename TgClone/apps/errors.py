from apps.logs.loggers import user_logger


class UserException(Exception):
    def __init__(self, message):
        user_logger.debug(message)
        super(UserException, self).__init__(message)

