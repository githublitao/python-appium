#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import time
import HTMLTestRunner
import common.Path


#   测试报告初始化
class Report:
    def __init__(self):
        self.time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        self.file = common.Path.report_path()+self.time+".html"
        self.fp = file(self.file, 'wb')

    def build_report(self):
        runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp, title='test_report', description='mamainst_test_interface')
        return runner

    def get_time(self):
        return self.time

    def get_fp(self):
        return self.fp