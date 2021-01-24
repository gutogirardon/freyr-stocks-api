"""
Freyr - A Free stock API
"""

import logging
import os
import sys

DEFAULT_LOGGING_DIRECTORY = "freyr/logs"

loggers = {}


def create_logger(name, level=logging.DEBUG, stderr=None,
                  filename=None, logging_directory=DEFAULT_LOGGING_DIRECTORY):
    """
    Create logger in any given context

    :param name: log name
    :param level: stderror level (logging.INFO, DEBUG, etc)
    :param stderr: stderror level (logging.INFO, DEBUG, etc), if None, nothing is printed
    :return:
    """

    if loggers.get(name):
        return loggers.get(name)

    if not filename:
        filename = F"{name}.log"
        filename = os.path.join(logging_directory, filename)
        if not os.path.exists(logging_directory):
            os.makedirs(logging_directory, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    log_model = F"%(asctime)s -%(levelname)10s - %(module)s.%(funcName)s.L_%(lineno)d: %(message)s"
    formatter = logging.Formatter(log_model, datefmt='%Y-%m-%d %H:%M:%S')

    fh = logging.FileHandler(filename)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    if stderr:
        ch = logging.StreamHandler(sys.stderr)
        ch.setLevel(stderr)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    loggers[name] = logger
    return logger