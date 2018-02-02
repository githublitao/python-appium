#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
import logging
import logging.config
from Exception import Custom_exception

from common import Path, runtime


def log_config():
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        logfile = Path.log_path()+runtime.test_start_time()+'.log'
        fh = logging.FileHandler(logfile, mode='w+')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)
        logging.info('测试开始时间：%s' %runtime. test_start_time())
        # logging.basicConfig(level=logging.DEBUG,
        #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S',
        #                     filename=Path.log_path()+runtime.test_start_time()+'.log',
        #                     filemode='w')
    except Exception as e:
        print(e)
        raise Custom_exception.LogConfigError


# def screen_shot(path, test_name):
#     try:
#         os.popen("adb wait-for-device")
#         os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
#         os.popen("adb pull /data/local/tmp/tmp.png " + (path + "/" + test_name + ".jpg"))
#         os.popen("adb shell rm /data/local/tmp/tmp.png")
#         logging.info('错误截图已保存在 '+path)
#     except Exception as e:
#         logging.error('截图失败：%s '% e)


# file 运行日志存放路径
# path 错误日志存放路径
# test_name  日志记录开始位标志
def error_log(fp, path, test_name=None):
    try:
        f = open(fp)
        data = f.readlines()
        num = len(data)
        r = open(path, 'w+')
        r.writelines('<?xml version="1.0" encoding="UTF-8"?>\n')
        for i in range(0, len(data) - 1):
            if test_name in data[i]:
                for j in range(i, num - 2):
                    r.writelines(data[j])
            if test_name is None:
                if num <= 50:
                    for j in range(0, num-1):
                        r.writelines(data[j])
                else:
                    for j in range(num-50, num-1):
                        r.writelines(data[j])
        r.close()
        f.close()
        logging.info('记录错误日志')
    except Exception as e:
        logging.error(e)


# 日志打印装饰器
def deco(arg):
    def _deco(func):
        def __deco(*args, **kwargs):
            logging.info("  start %s." % arg)
            func(*args, **kwargs)
            logging.info("  %s success." % arg)
        return __deco
    return _deco



