#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
执行测试用例list
"""


def test_case_list(case_num):
    while True:
        try:
            all_or_part = raw_input('请选择：1.运行全部用例    2.运行部分用例\n'
                                    '》》')
            if int(all_or_part) == 2:
                while True:
                    fist = raw_input("请输入开始用例编号》》 ")
                    end = raw_input("请输入末尾用例编号》》：")
                    if int(fist) < 1:
                        print "开始用例序号必须大于等于1"
                        raise
                    elif int(end) >= case_num:
                        print "结束用例序号大于用例数量"
                        raise
                    elif int(fist) > int(end):
                        print "用例开始序号大于结束序号"
                        raise
                    else:
                        return int(fist), int(end)+1
            elif int(all_or_part) == 1:
                return 1, case_num
        except:
            print "输入有误！！"


