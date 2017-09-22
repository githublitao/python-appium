#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
#   封装配置文件地址
import os
pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")


# def phone_info():
#     """
#     被测设备信息
#     :return:
#     """
#     path = father_path+'\\Phone_Info.ini'
#     return path


def report_path():
    """
    测试报告
    :return:
    """
    path = father_path+'\\Test_Report\\'
    return path


# def email_path():
#     """
#     邮箱配置文件
#     :return:
#     """
#     path = father_path+'\\email_address.ini'
#     return path


# def page_path():
#     """
#     page.xml
#     :return:
#     """
#     path = father_path+'\\page.xml'
#     return path


def log_path():
    """
    日志位置
    :return:
    """
    path = father_path + '\\log\\'
    return path


# def data_path():
#     """
#     测试数据存放
#     :return:
#     """
#     path = father_path+'\\case.xls'
#     return path


# def case_py():
#     """
#     用例脚本
#     :return:
#     """
#     path = father_path+'\\case\\Test_Case.py'
#     return path


#   prefix 匹配前缀文件
#   postfix匹配后缀文件
def scan_files(prefix=None, postfix=None):
    #   返回文件路径
    files_list = []
    for root, sub_dirs, files in os.walk(father_path):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))
    return files_list[0]
