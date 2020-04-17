
import inspect
import logging


def custom_logger(log_level=logging.DEBUG):

    # Gets the name of the class / method from where this method is called
    # Don't know how this works but it has to be here
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # Set level of messages
    # Overriding the log level defined in Method level
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('automation.log', mode='w')
    file_handler.setLevel(log_level)

    # Format of the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
