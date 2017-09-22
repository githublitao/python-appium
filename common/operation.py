#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
import logging

import Element
import Global
from case import Get_Driver


class Opera:
    """
    用户操作封装
    """
    def __init__(self):
        self.dr = Get_Driver.Driver()
        self.D = Element.Element(self.dr.get_driver())
        self.p = Global.Locator()

#   点击事件
    def clicks(self, page_name, locator):
        self.D.get(self.p.get_type(page_name, locator)).click()

#   输入文本
    def send_keys(self, page_name, locator, text):
        self.D.get(self.p.get_type(page_name, locator)).send_keys(text)

#   获得元素文本
    def get_text(self, page_name, locator):
        element_text = self.D.get(self.p.get_type(page_name, locator)).text.encode('utf-8')
        return element_text

#   等待页面元素加载
    def wait_element(self, page_name, locator):
        self.D.wait_element(self.p.get_type(page_name, locator))

#   物理键返回
    def go_back(self):
        self.D.back()

#   切换web view
    def sw_h5(self):
        self.D.switch_h5()

#   切换至app
    def sw_app(self):
        self.D.switch_app()

#   关闭driver
    def quit(self):
        self.D.over()

#   获取屏幕size
    def getsize(self):
        size = self.D.get_size()
        return size

#   向上滑动
    def swipe_up(self):
        self.D.swipe_to_up()

#   向下滑动
    def swipe_to_down(self):
        self.D.swipe_to_down()

#   向左滑动
    def swipe_to_left(self):
        self.D.swipe_to_left()

#   向右滑动
    def swipe_to_right(self):
        self.swipe_to_right()

#   截图
    def screen(self, path, name, time):
        try:
            self.D.get_screen(path+'\\'+name+time+'.png')
            logging.info('错误截图已保存在 ' + path)
        except Exception as e:
            logging.error('截图失败：%s ' %e)


