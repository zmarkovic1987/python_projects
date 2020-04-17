"""
Logger Demo
"""
import logging


class LoggerDemoConsole():

    def test(self):
        # Create a Logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)  # SETTING A LEVEL

        # Create Console handler and set level to Info
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)  # Ser level of Handler - this Level wil override level set on Logger (above)

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s:',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler -> ch
        c_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(c_handler)

        # Logging messages
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")


start = LoggerDemoConsole()
start.test()


