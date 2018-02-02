#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月23日

@author: li tao
"""
import logging

from case import AllCase
from common import creat_case
from common import log
from common import server
from common import del_past_dir
from Report import generate_test_report


if __name__ == '__main__':
    try:
        log.log_config()            # 初始化日志配置
        server.start_server()  # 开启appium服务
        creat_case.test_case()      # 初始化用例脚本
        AllCase.run_case()          # 执行用例
        server.stop_server()        # 关闭appium服务
        generate_test_report.ab(creat_case.test_result_list())      # 创建测试报告
        del_past_dir.delete_fp()        # 删除过期的测试报告和log日志
    except Exception as e:
        logging.exception("ERROR")
        print(e)
