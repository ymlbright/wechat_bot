#!/usr/bin/env python
# coding: utf-8
# Modify base on https://github.com/Urinx/WeixinBot/blob/master/wxbot_project_py2.7/config/log.py
#===================================================
from constant import Constant
#---------------------------------------------------
import logging
import logging.config
#===================================================

logging.config.fileConfig(Constant.WECHAT_CONFIG_FILE)
# create logger
Log = logging.getLogger(Constant.LOGGING_LOGGER_NAME)

# 'application' code
# Log.debug('debug message')
# Log.info('info message')
# Log.warn('warn message')
# Log.error('error message')
# Log.critical('critical message')
