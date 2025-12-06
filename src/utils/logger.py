from logging import getLogger, INFO


def get_logger():
    logger = getLogger()
    logger.setLevel(INFO)
    return logger