
import logging
import os

from some import MyDelete1

# logger = logging.getLogger('myapp')
# hdlr = logging.FileHandler('logs/app.log', "a")
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# formatter.datefmt = "%Y-%m-%d %H:%M:%S"
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
# logger.setLevel(logging.DEBUG)

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt="%Y-%m-%d %H:%M:%S",
#                     filename='/logs/app.log',
#                     filemode='w')
# hdlr = logging.FileHandler('logs/app.log', "a")
# logger = logging.getLogger('myapp')
# logger.addHandler(hdlr)
# logger.setLevel(logging.DEBUG)
log_filename = "logs/app.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
logger = logging.getLogger()
handler = logging.FileHandler(log_filename, "a")
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
formatter.datefmt = "%Y-%m-%d %H:%M:%S"
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger = logging.getLogger("Delete-1")
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
    MyDelete1.deleteAll()
    logger.debug('xxxxxxxxx debug message')
    logger.info('xxxxxxxxxx info message')
    logger.warning('xxxxxxxxxxxx warn message')
    logger.error('xxxxxxxxxxx error message')
    logger.critical('xxxxxxxxx critical message')