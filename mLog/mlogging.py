#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging
#日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)，
import sys

logging.basicConfig(filename='logger.log',level=logging.DEBUG)
# sh = logging.StreamHandler(stream=None)
# fh = logging.FileHandler("test.log", mode='a', encoding=None, delay=False)
logging.debug("debug message")
logging.info("info messasge")
logging.warn("warn message")
logging.error("error message")
logging.critical("critical message")

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create file handler
log_path = './log.log'
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')








