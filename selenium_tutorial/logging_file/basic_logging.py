"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logging.warning('warning message')
# logging.info('info message')
# logging.error('error message')
"""
LOGGING FORMAT
"""
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s:',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.warning("warning message")
logging.info("info message")
logging.error("error message")


