#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
执行测试用例list
"""


#  case_num  总的测试用例数量
def test_case_list(case_num):
    while True:
        try:
            all_or_part = input('请选择：1.运行全部用例    2.运行部分用例\n''》》')
            if int(all_or_part) == 2:
                while True:
                    try:
                        print('-'*50)
                        print("请输入您要测试的用例范围   q=返回上一菜单")
                        fist = input("开始用例编号》》 ")
                        if fist == 'q':
                            break
                        elif int(fist) < 1:
                            print("输入有误！！\n开始用例序号必须大于等于1")
                        end = input("结尾用例编号》》")
                        if end == 'q':
                            break
                        elif int(end) >= case_num:
                            print("输入有误！！\n结束用例序号不能大于用例数量")
                        elif int(fist) > int(end):
                            print("输入有误！！\n用例开始序号不能大于结束序号")
                        else:
                            return int(fist), int(end)+1
                    except:
                        print("输入有误！！1")
            elif int(all_or_part) == 1:
                print(case_num)
                return 1, case_num
        except:
            print('输入有误')