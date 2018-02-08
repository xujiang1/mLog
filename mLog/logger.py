#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging
import logging.config
import os
from functools import wraps


class LogLevelFilter(logging.Filter):
    def __init__(self, name='', level=logging.DEBUG, levels=None):
        super(LogLevelFilter,self).__init__(name)
        self.level = level
        self.levels = levels

    def filter(self, record):
        if self.levels == None:
            return record.levelno == self.level
        else:
            for level in self.levels:
                if record.levelno == level:
                    return True
            return False

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class mLogger():
    def __init__(self,LOG_DIR):
        logging.config.fileConfig("./logging.conf")
        # create logger
        self.logger_name = "all"
        self.logger = logging.getLogger(self.logger_name)
        self.LOG_DIR = ''
        self.logfilelists = ["mylog.log", "mydebuglog.log", "myinfolog.log", "mywarnlog.log", "myerrorlog.log",
                             "myexceptionlog.log", "mycriticallog.log"]
        self.initlogger()



    def initlogger(self):
        # 过滤器
        filter_stdout = LogLevelFilter(levels=[logging.INFO, logging.DEBUG])
        filter_debug = LogLevelFilter(level=logging.DEBUG)
        filter_info = LogLevelFilter(level=logging.INFO)
        filter_warn = LogLevelFilter(level=logging.WARN)
        filter_error = LogLevelFilter(level=logging.ERROR)
        filter_exception = LogLevelFilter(level=logging.ERROR)  # 会返回错误堆栈
        filter_critical = LogLevelFilter(level=logging.CRITICAL)

        handlers = self.logger.handlers
        # 下面是一些过滤器 将对应级别的信息输出到对应的文件方便查找错误
        # streamerrhandler不进行过滤 因为他的level为warn及以上
        handlers[1].addFilter(filter_stdout)  # streamouthandler
        handlers[3].addFilter(filter_debug)  # debug
        handlers[4].addFilter(filter_info)  # info
        handlers[5].addFilter(filter_warn)  # warn
        handlers[6].addFilter(filter_error)  # error
        handlers[7].addFilter(filter_exception)  # exception
        handlers[8].addFilter(filter_critical)  # critical

        for i in range(9):
            if i >= 2:
                handlers[i].baseFilename = os.path.join(self.LOG_DIR, self.logfilelists[i - 2])

# logger = mLogger("./logs").logger
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.exception('exception message')
# logger.critical('critical message')





