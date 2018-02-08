#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# [loggers]
# # 定义logger模块，root是父类，必需存在的，其它的是自定义。
# # logging.getLogger(NAME)便相当于向logging模块注册了一种日志打印
# # name 中用 . 表示 log 的继承关系
#
# [handlers]
# # 定义handler
# [formatters]
# # 定义格式化输出
# [logger_root]
#
# # 实现上面定义的logger模块，必需是[logger_xxxx]这样的形式
#
# # [logger_xxxx] logger_模块名称
# # level     级别，级别有DEBUG、INFO、WARNING、ERROR、CRITICAL
# # handlers  处理类，可以有多个，用逗号分开
# # qualname  logger名称，应用程序通过 logging.getLogger获取。对于不能获取的名称，则记录到root模块。
# # propagate 是否继承父类的log信息，0:否 1:是
#
# [handler_infohandler]
# # [handler_xxxx]
# # class handler类名
# # level 日志级别
# # formatter，上面定义的formatter
# # args handler初始化函数参数
#
# [formatter_form01]
#
# # 日志格式
# #--------------------------------------------------
# # %(asctime)s       年-月-日 时-分-秒,毫秒 2013-04-26 20:10:43,745
# # %(filename)s      文件名，不含目录
# # %(pathname)s      目录名，完整路径
# # %(funcName)s      函数名
# # %(levelname)s     级别名
# # %(lineno)d        行号
# # %(module)s        模块名
# # %(message)s       消息体
# # %(name)s          日志模块名
# # %(process)d       进程id
# # %(processName)s   进程名
# # %(thread)d        线程id
# # %(threadName)s    线程名
#
# 使用方式：
#
# from logging.config import fileConfig
#
# fileConfig('loggin_config.ini')
# logger=logging.getLogger('infoLogger')
# logger.info('test1')
# logger_error=logging.getLogger('errorhandler')
# logger_error.error('test5')

