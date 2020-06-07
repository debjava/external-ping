import logging
logging.basicConfig(level=logging.DEBUG)


def sayHello():
    logger = logging.getLogger(__name__)
    logger.debug("Check I am in check ...")
    logger.info('check info message')
    logger.warning("check warn message")
    print("Coming here ...")