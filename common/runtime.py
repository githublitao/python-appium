#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import time
import log
try:
    runtime = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
except Exception as e:
    log.exception_handling(e)


def test_start_time():
    return runtime
