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


def phone_info():
    """
    被测设备信息
    """
    path = father_path+'\\Phone_Info.ini'
    return path


def apk_path():
    """
    待测应用Path
    """
    path = father_path+'\\app-client-debug-test-2.3.13.apk'
    return path


def report_path():
    """
    测试报告
    """
    path = father_path+'\\Test_Report\\'
    return path


def email_path():
    """
    邮箱配置文件
    """
    path = father_path+'\\email_address.ini'
    return path


def page_path():
    """
    page.xml
    """
    path = father_path+'\\page.xml'
    return path


def log_path():
    """
    日志位置
    """
    path = father_path + '\\log\\'
    return path

