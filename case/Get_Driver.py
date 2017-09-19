#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""
import os
from appium import webdriver
from common.Get_Phone import Phone, Path
import time
PATH=lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
Phone = Phone()
#   初始化driver


class Driver:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = Phone.version()
        desired_caps['deviceName'] = Phone.model()
        desired_caps['app'] = PATH(Path.apk_path())
#       desired_caps['appPackage'] = 'com.sixty.nidoneClient'
#       desired_caps['appActivity'] = 'com.sixty.nidoneClient.view.activity.SDK_WebApp'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
#       如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def get_driver(self):
        return self.driver

