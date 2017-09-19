#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
import unittest
import time
from common import log
from common import Path
from common import mkdir_log_directory
import logging
from common import operation
# 测试用例


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, method_name='runTest', run_time=None):
        super(ParametrizedTestCase, self).__init__(method_name)
        self.time = run_time
        self.method_name = method_name


class Test(ParametrizedTestCase):
    def setUp(self):
        self.OP = operation.Opera()

    def tearDown(self):
        self.OP.quit()

    @log.deco(u'登录测试')
    def testAdd(self):
        time.sleep(15)
        try:
            self.OP.sw_h5()
            self.OP.send_keys('login', '账号', '18202886913')
            self.OP.clicks('login', '密码')
            self.OP.send_keys('login', '密码', '123456')
            self.OP.clicks('login', '登录')
            self.OP.wait_element('login', '账户或密码错误')
        except Exception as e:
            logging.error('%s' % e)
            path = Path.log_path()+self.time+'_error'
            mkdir_log_directory.mk_dir(path)
            self.OP.screen(path+'\\'+self.method_name+'.png')
            path1 = Path.log_path()+self.time+'.log'
            error_log = path+'\\'+u'登录测试'+'.log'
            log.error_log(path1, error_log)

    @log.deco(u'登录测试1')
    def testAdd1(self):
        time.sleep(15)
        try:
            self.OP.sw_h5()
            self.OP.send_keys('login', '账号', '18202886913')
            self.OP.clicks('login', '密码')
            self.OP.send_keys('login', '密码', '123456')
            self.OP.clicks('login', '登录')
            self.OP.wait_element('login', '账户或密码错误')
        except Exception as e:
            logging.error('%s' % e)
            path = Path.log_path()+self.time+'_error'
            mkdir_log_directory.mk_dir(path)
            self.OP.screen(path+'\\'+self.method_name+'.png')
            path1 = Path.log_path()+self.time+'.log'
            error_log = path+'\\'+u'登录测试1'+'.log'
            log.error_log(path1, error_log)

    @log.deco(u'登录测试3')
    def testAdd3(self):
        time.sleep(15)
        try:
            self.OP.sw_h5()
            self.OP.send_keys('login', '账号', '18202886913')
            self.OP.clicks('login', '密码')
            self.OP.send_keys('login', '密码', '123123')
            self.OP.clicks('login', '登录')
            self.OP.wait_element('login', '账户或密码错误')
        except Exception as e:
            logging.error('%s' % e)
            path = Path.log_path()+self.time+'_error'
            mkdir_log_directory.mk_dir(path)
            self.OP.screen(path, self.method_name)
            path1 = Path.log_path()+self.time+'.log'
            error_log = path+'\\'+u'登录测试3'+'.log'
            log.error_log(path1, error_log)


