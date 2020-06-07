import os
from some import check
import logging.config


def main():
    log_filename = "logs/app.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    logging.config.fileConfig('logging.conf')
    # your program code


if __name__ == '__main__':
    main()
    #     logger = logging.getLogger(__name__+"A")
    #     logger.debug("Hello ...")
    #     logger.info("Hello ...")
    #     logging.config.fileConfig('logging.conf')
    # create logger
    logger = logging.getLogger("temp1")
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
    check.sayHello()
    logger.debug('xxxxxxxxx debug message')
    logger.info('xxxxxxxxxx info message')
    logger.warning('xxxxxxxxxxxx warn message')
    logger.error('xxxxxxxxxxx error message')
    logger.critical('xxxxxxxxx critical message')
