#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""

import subprocess
import logging
import re


def connect_dvs():
    """
    检查设备是否连接成功，如果成功返回True，否则返回False
    """
    try:
        """
        获取设备列表信息，并用"\r\n"拆分
        """
        device_info = subprocess.check_output('adb devices').split("\r\n")
        """
        如果没有链接设备或者设备读取失败，第二个元素为空
        """
        if device_info[1] == '':
            return False
        else:
            return True
    except Exception as e:
        logging.error("Device Connect Fail:", e)


def get_android_version():
    try:
        if connect_dvs():
            #   获取系统设备系统信息
            sys_info = subprocess.check_output('adb shell cat /system/build.prop')
            #   获取安卓版本号
            android_version = re.findall("version.release=(\d\.\d)*", sys_info, re.S)[0]
            return android_version
        else:
            return "Connect Fail,Please reconnect Device..."
    except Exception as e:
        logging.error("Get Android Version:", e)


def get_device_name():
    try:
        if connect_dvs():
            #   获取设备名
            device_info = subprocess.check_output('adb devices -l')
            device_nam = re.findall(r'device product:(.*)\smodel', device_info, re.S)[0]
            return device_nam
        else:
            return "Connect Fail,Please reconnect Device..."
    except Exception as e:
        logging.error("Get Device Name:", e)
