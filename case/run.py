#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月23日

@author: li tao
"""


from common import log
from common import creat_case
import AllCase

if __name__ == '__main__':
    log.log_config()
    creat_case.test_case()      # 初始化用例脚本
    AllCase.run_case()

