"""
Central logging utility class which controls logging related configuration

Usages:
first two lines in each python file will be following where logging is required
    from util.logger import Logger
    logger = Logger.get_logger(__file__)
Then one can use `LOG` object to log debug, info, warning, error, exception, critical logs

Example:
    LOG.debug("Job created with id: {} type: {}".format("id", 0))

    LOG.info("Logging with curly braces id: {} type: {{}}".format("id"))

    LOG.warning("Job created with id: {} python object: {}".format("job-id", "Any in-built python object"))

    LOG.error("Job created with id: {} custom object: {}".format("job-id", "Any custom user-defined python object which implements __str__ or __repr__ method"))

    LOG.critical("Job created with id: {} type: {}".format("job-id", 0))

    try:
        raise Exception("my custom exception")
    except Exception:
        # This will print stack trace along with variables formatting
        LOG.exception("Caught exception while creating job with id: {} type: {}".format("job-id", 0))


"""
import os
import logging
import logging.handlers

from conf.config_manager import ConfigManager

BASIC_LOG_FORMAT = "%(asctime)s,%(msecs)d [%(levelname)s]:[%(name)s:%(thread)d:%(threadName)s: %(process)d:%(processName)s] %(message)s"
TIME_FORMAT = "%d/%b/%Y:%H:%M:%S"

LOGGING_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class Logger:

    @staticmethod
    def get_logger(name=None):
        """
        One can set OS environment variable while running process through supervisor by adding following line
        environment=LOG_LEVEL="debug"
        Please note that user should be same user as command running user.
        if user=deploy then don't add sudo etc to command
        :param name:
        :return:
        """
        if name:
            name = os.path.splitext(os.path.basename(name))[0]
        logger = logging.getLogger(name)
        log_level = LOGGING_LEVELS.get(ConfigManager.get_instance().log_level(), logging.DEBUG)
        logger.setLevel(log_level)
        formatter = logging.Formatter(BASIC_LOG_FORMAT, TIME_FORMAT)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


if __name__ == "__main__":
    Logger.get_logger()
