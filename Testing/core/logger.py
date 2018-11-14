# coding=utf-8

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
__author__ = 'qiguojie'
__date__ = '2016-11-30'

import datetime, os
import config

class Logger(object):

    def __init__(self):
        # 要写入log的目录，这个需要在config中配置
        self.log_dir = config.log_file_dir

    def log_write(self, message):
        """
            写入log文件，包含检查文件是否存在（每天生成1个），如不存在则创建；然后使用追加的方式写入message信息
        """
        log_dir = self.log_dir
        # 判断logs目录是否存在；如不存在则创建；
        if os.path.exists(log_dir):
            log_file = os.path.join(log_dir, 'comall_' + datetime.datetime.now().strftime('%Y%m%d') + '.log')
        else:
            os.mkdir(r'%s' % log_dir)
            log_file = os.path.join(log_dir, 'comall_' + datetime.datetime.now().strftime('%Y%m%d') + '.log')
        file_open = open(log_file, "a")
        try:
            file_open.write(message + "\n")
        finally:
            file_open.close()

    def info(self, message):
        # 判断执行信息开关是否打开，如果打开则打印log
        if config.info:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.log_write(now + " Info: " + message)

    def debug(self, message):
        # 判断调试信息的开关是否打开，如果打开则打印log
        if config.debug:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.log_write(now + " Debug: " + message)

    def error(self, message):
        # 判断调试信息的开关是否打开，如果打开则打印log
        if config.error:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.log_write(now + " Error: " + message)


