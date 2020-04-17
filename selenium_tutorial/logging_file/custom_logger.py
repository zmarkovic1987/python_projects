import inspect
import logging


def custom_logger(log_level):

    # Gets the name of the class / method fro where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # Set default to be all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('{0}.log'.format(logger_name), mode='w')  # w is for overwriting logs in file
    file_handler.setLevel(log_level)

    # Define formatter
    formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s:',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


