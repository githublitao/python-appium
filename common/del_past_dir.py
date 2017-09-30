#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年9月30日

@author: li tao
"""
import shutil
import time
import datetime
import Path
import os
import logging


#   删除文件
def delete_fp():
    try:
        lg = [Path.father_path+'\\log', Path.report_path()]
        for j in lg:
            if os.path.exists(j):
                ls = os.listdir(j)
                for i in range(0, len(ls)):
                    path = os.path.join(lg, ls[i])
                    if os.path.exists(path):
                        creat_time = time.localtime(os.stat(path).st_ctime)     # 文件最后访问时间
                        y = time.strftime('%Y', creat_time)
                        m = time.strftime('%m', creat_time)
                        d = time.strftime('%d', creat_time)
                        h = time.strftime('%H', creat_time)
                        M = time.strftime('%M', creat_time)
                        d2 = datetime.datetime(int(y), int(m), int(d), int(h), int(M))  # 格式化时间
                        time_difference = (datetime.datetime.now()-d2).days         # 计算时间差
                        if time_difference >= 2:                           # 时间差超过10天，则删除
                            shutil.rmtree(path)
            else:
                logging.warning('日志或测试报告文件夹不存在')
    except Exception as e:
        logging.error(e)



