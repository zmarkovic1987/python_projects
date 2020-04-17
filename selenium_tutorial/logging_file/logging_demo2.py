import logging
import logging_file.custom_logger as cl


class LoggingDemo2():

    logger = cl.custom_logger(logging.DEBUG)

    def method_1(self):
        self.logger.debug("debug message")
        self.logger.info("info message")
        self.logger.warning("warning message")
        self.logger.error("error message")
        self.logger.critical("critical message")

    def method_2(self):

        m2_log = cl.custom_logger(logging.INFO)

        m2_log.debug("debug message")
        m2_log.info("info message")
        m2_log.warning("warning message")
        m2_log.error("error message")
        m2_log.critical("critical message")

    def method_3(self):

        m3_log = cl.custom_logger(logging.WARNING)

        m3_log.debug("debug message")
        m3_log.info("info message")
        m3_log.warning("warning message")
        m3_log.error("error message")
        m3_log.critical("critical message")


start = LoggingDemo2()
start.method_1()
start.method_2()
start.method_3()
