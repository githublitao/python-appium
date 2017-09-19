#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月23日

@author: li tao
"""

# from Report import Test_Report, Send_report
import unittest
from Test_Case import Test
import time
from common import log

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    log.log_config(time)
    # # 初始化测试报告
    # rp = Test_Report.Report()
    # # 测试时间
    # time = rp.time
    # 创建测试报告
    # runner = rp.build_report()
    runner = unittest.TextTestRunner()
    # 添加测试用例
    test = Test('testAdd', time)
    # test1 = Test('testAdd1', time)
    # test3 = Test('testAdd3', time)
    suite = unittest.TestSuite()
    suite.addTest(test)
    # suite.addTest(test1)
    # suite.addTest(test3)
    # 执行测试用例
    runner.run(suite)
    # 发送测试报告
    # Send_report.send_email(time)
