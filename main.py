#!/usr/bin/env python
# coding: utf-8

#===================================================
from wechat import WeChat
from wechat.utils import *
from wx_msg_handler import WeChatMsgProcessor
from config import Constant
from config import Log
#---------------------------------------------------
import threading
import traceback
import os
import logging
import time
#===================================================
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

wechat_msg_processor = WeChatMsgProcessor()
wechat = WeChat("wx.qq.com")
wechat.msg_handler = wechat_msg_processor
wechat_msg_processor.wechat = wechat

while True:
    try:
        wechat.start()
    except KeyboardInterrupt:
        echo(Constant.LOG_MSG_QUIT)
        wechat.exit_code = 1
    else:
        Log.error(traceback.format_exc())
    finally:
        wechat.stop()
    
    # send a mail to tell the wxbot is failing
    #subject = 'wxbot stop message'
    #log_file = open(eval(cm.get('handler_fileHandler', 'args'))[0], 'r')
    #mail_content = '<pre>' + str(wechat) + '\n\n-----\nLogs:\n-----\n\n' + ''.join(log_file.readlines()[-100:]) + '</pre>'
    #sg.send_mail(subject, mail_content, 'text/html')
    #log_file.close()

    if wechat.exit_code == 0:
        echo(Constant.MAIN_RESTART)
    else:
        # kill process
        os.system(Constant.LOG_MSG_KILL_PROCESS % os.getpid())
