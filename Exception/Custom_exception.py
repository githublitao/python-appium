#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
#   自定义异常类，可自行添加


class WrongLocation(Exception):
    def __init__(self, err='错误的元素定位方式'):
        Exception.__init__(self, err)


class ReadXmlError(Exception):
    def __init__(self, err='Xml读取初始化失败'):
        Exception.__init__(self, err)


class MailInitializationError(Exception):
    def __init__(self, err='邮件初始化'):
        Exception.__init__(self, err)


class GetDriverError(Exception):
    def __init__(self, err='初始化driver失败'):
        Exception.__init__(self, err)


class OpenXlsError(Exception):
    def __init__(self, err='打开用例文件失败'):
        Exception.__init__(self, err)


class CreatTestCaseError(Exception):
    def __init__(self, err='创建用例脚本失败'):
        Exception.__init__(self, err)


class CloseFileError(Exception):
    def __init__(self, err='关闭文件是发生错误'):
        Exception.__init__(self, err)


class ReadDeviceError(Exception):
    def __init__(self, err='读取待测设备时发生错误'):
        Exception.__init__(self, err)


class LogConfigError(Exception):
    def __init__(self, err='日志配置初始化错误'):
        Exception.__init__(self, err)


class InitResultError(Exception):
    def __init__(self, err='初始化测试结果表失败'):
        Exception.__init__(self, err)


class WriteResultError(Exception):
    def __init__(self, err='写入测试结果失败'):
        Exception.__init__(self, err)


class SaveReusltError(Exception):
    def __init__(self, err='保存测试结果失败'):
        Exception.__init__(self, err)


class ElementNotExist(Exception):
    def __init__(self, err='页面元素不存在'):
        Exception.__init__(self, err)
