# -*- coding utf-8 -*-
import logging
import os.path
import time
class Logger:
    def __init__(self,logger):

        #创建logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建handler
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))  #日期
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+'.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        # self.logger.info("info日志信息")
        # self.logger.debug("debug日志信息")
        # self.logger.warning("warning日志信息")
        # self.logger.error("error日志信息")

    def getlog(self):
        return  self.logger

