#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from common import log
from common import operation
from common import creat_case
# 测试用例


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, method_name="runTest", run_time=None):
        super(ParametrizedTestCase, self).__init__(method_name)
        self.method_name = method_name


class Test(ParametrizedTestCase):
    def setUp(self):
        self.OP = operation.Opera()

    def tearDown(self):
        self.OP.quit()

    @log.deco(u"正确登录")
    def test_login(self):
        try:
            self.OP.sw_h5()
            self.OP.send_keys("login", "账号", "18202886913")
            self.OP.clicks("login", "密码")
            self.OP.send_keys("login", "密码", "123456")
            self.OP.clicks("login", "登录")
        except Exception as e:
            creat_case.exception_handling(e, index=1, test_name="正确登录", method_name=self.method_name, op=self.OP)

    @log.deco(u"正常登录1")
    def test_login1(self):
        try:
            self.OP.sw_app()
            self.OP.send_keys("login", "账号", "18202886911")
            self.OP.clicks("login", "密码")
            self.OP.send_keys("login", "密码", "123")
            self.OP.clicks("login", "登录")
        except Exception as e:
            creat_case.exception_handling(e, index=2, test_name="正常登录1", method_name=self.method_name, op=self.OP)
