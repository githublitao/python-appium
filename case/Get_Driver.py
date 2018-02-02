#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
import os
from appium import webdriver
from common import Get_Phone
from common import Path
from common import log
from common import creat_case
from Exception import Custom_exception
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Driver:
    """
    初始化driver
    """
    @log.deco(u'初始化driver')
    def __init__(self):
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = Get_Phone.get_android_version()     # 设备版本
            desired_caps['deviceName'] = Get_Phone.get_device_name()        # 设备名称
            desired_caps['app'] = PATH(Path.scan_files(postfix='.apk'))     # 待测应用
#           desired_caps['appPackage'] = 'com.sixty.nidoneClient'
#           desired_caps['appActivity'] = 'com.sixty.nidoneClient.view.activity.SDK_WebApp'
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
#           如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        except Exception as e:
            creat_case.exception_handling(e)
            raise Custom_exception.GetDriverError

    def get_driver(self):
        return self.driver

