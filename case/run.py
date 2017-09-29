#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月23日

@author: li tao
"""

import AllCase
from common import creat_case
from common import log
from Report import generate_test_report

if __name__ == '__main__':
    log.log_config()            # 初始化日志配置
    creat_case.test_case()      # 初始化用例脚本
    AllCase.run_case()          # 执行用例
    creat_case.write_excel()
    generate_test_report.ab(creat_case.test_result_list())
