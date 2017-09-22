#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
import logging
import Path
import logging.config
import mkdir_log_directory
import runtime

def log_config():
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
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename=Path.log_path()+time+'.log',
    #                     filemode='w')


# def screen_shot(path, test_name):
#     try:
#         os.popen("adb wait-for-device")
#         os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
#         os.popen("adb pull /data/local/tmp/tmp.png " + (path + "/" + test_name + ".jpg"))
#         os.popen("adb shell rm /data/local/tmp/tmp.png")
#         logging.info('错误截图已保存在 '+path)
#     except Exception as e:
#         logging.error('截图失败：%s '% e)


def error_log(file, path):
    f = open(file)
    data = f.readlines()
    for i in range(0, len(data) - 1):
        if '登录测试' in data[i]:
            r = open(path, 'w+')
            r.writelines('<?xml version="1.0" encoding="UTF-8"?>')
            for j in range(i, len(data) - 2):
                r.writelines(data[j])
            r.close()
    logging.info('记录错误日志')


def deco(arg):
    def _deco(func):
        def __deco(*args, **kwargs):
            logging.info("  run %s." % arg)
            func(*args, **kwargs)
            logging.info("  %s end." % arg)
        return __deco
    return _deco


def exception_handling(e, method_name, test_name, op):
    logging.error(e)
    path = Path.log_path() + method_name + '_error'
    mkdir_log_directory.mk_dir(path)
    op.screen(path, method_name)
    path1 = Path.log_path() + runtime.test_start_time() + '.log'
    log_error = path + '\\' + runtime.test_start_time() + '.log'
    print path1
    print log_error
    error_log(path1, log_error)
