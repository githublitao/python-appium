#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
import configparser
import Path


class Phone:
    """
    获取待测设备唯一标识和版本
    """
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Path.phone_info())
        try:
            self.Phone_Model = config['Phone']['Phone_Model']
            self.System_Version = config['Phone']['System_Version']
        except Exception as e:
            print '%s' % e

    def model(self):
        return self.Phone_Model

    def version(self):
        return self.System_Version
