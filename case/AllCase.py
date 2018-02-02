# coding:utf-8
import unittest
import os
# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径


# 获取所有py文件中所有test开头的用力
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    return discover


def run_case():
    runner = unittest.TextTestRunner()
    runner.run(all_case())
