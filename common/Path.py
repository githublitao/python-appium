#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
#   封装配置文件地址
import os

from common import runtime, mkdir_log_directory

pwd = os.getcwd()
father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")


def report_path():
    """
    测试报告
    :return:
    """
    path = father_path+'\\Test_Report\\'
    return path


def log_path():
    """
    日志位置
    :return:
    """
    path = father_path + '\\log\\'+runtime.test_start_time()+'\\'
    mkdir_log_directory.mk_dir(path)
    return path


def scan_files(prefix=None, postfix=None):
    """
    返回文件绝对路径
    :param prefix: 匹配前缀文件
    :param postfix: 匹配后缀文件
    :return:
    """
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
