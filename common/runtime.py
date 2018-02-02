#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import time
import datetime

from common import creat_case

try:
    runtime = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    start_time = datetime.datetime.now()
except Exception as e:
    creat_case.exception_handling(e)


def test_start_time():
    return runtime


def start_time_test():
    return start_time
