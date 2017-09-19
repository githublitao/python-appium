#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
#   自定义异常类，可自行添加


class WrongLocation(Exception):
    def __init__(self,err='错误的元素定位方式'):
        Exception.__init__(self,err)