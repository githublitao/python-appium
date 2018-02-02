#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
import logging
from case import Get_Driver
from Exception import Custom_exception
from common import Element, Global


class Opera:
    """
    用户操作封装
    """
    def __init__(self):
        self.dr = Get_Driver.Driver()
        self.D = Element.Element(self.dr.get_driver())
        self.p = Global.Locator()

    def clicks(self, page_name, locator):
        """
        点击事件
        :param page_name: 页面名称
        :param locator: 元素名称
        :return:
        """
        self.D.get(self.p.get_type(page_name, locator)).click()

    def send_keys(self, page_name, locator, text):
        """
        调用输入法输入
        :param page_name: 页面元素
        :param locator: 元素名称
        :param text: 输入内容
        :return:
        """
        self.D.get(self.p.get_type(page_name, locator)).send_keys(text)

    def set_keys(self, page_name, locator, text):
        """
        直接对元素输入文本
        :param page_name: 页面元素
        :param locator: 元素名称
        :param text: 输入内容
        :return:
        """
        self.D.get(self.p.get_type(page_name, locator)).set_text(text)

    def get_text(self, page_name, locator):
        """
        获取元素文本
        :param page_name: 页面名称
        :param locator: 元素名称
        :return:
        """
        element_text = self.D.get(self.p.get_type(page_name, locator)).text.encode('utf-8')
        return element_text

    def wait_element(self, page_name, locator):
        """
        等待页面元素
        :param page_name:  页面名称
        :param locator: 元素名称
        :return:
        """
        self.D.wait_element(self.p.get_type(page_name, locator))

    def go_back(self):
        """
        物理键返回
        :return:
        """
        self.D.back()

    def sw_h5(self):
        """
        切换webview
        :return:
        """
        self.D.switch_h5()

    def sw_app(self):
        """
        切换至原生页面
        :return:
        """
        self.D.switch_app()

    def quit(self):
        """
        关闭dirver
        :return:
        """
        self.D.over()

    def getsize(self):
        """
        获取页面大小
        :return:
        """
        size = self.D.get_size()
        return size

    def swipe_up(self):
        """
        向上移动
        :return:
        """
        self.D.swipe_to_up()

    def swipe_to_down(self):
        """
        向下移动
        :return:
        """
        self.D.swipe_to_down()

    def swipe_to_left(self):
        """
        向左移动
        :return:
        """
        self.D.swipe_to_left()

    def swipe_to_right(self):
        """
        向右移动
        :return:
        """
        self.D.swipe_to_right()

    def screen(self, name, path):
        """
        截图
        :param name: 截图名称
        :param path: 截图存储路径
        :return:
        """
        try:
            self.D.get_screen(name)
            logging.info('错误截图已保存在 ' + path)
        except Exception as e:
            logging.error('截图失败：%s ' % e)

    def judge_key(self, key):
        """
        判断页面元素是否存在
        :param key:
        :return:
        """
        if self.D.get_page(key) == -1:
            raise Custom_exception.ElementNotExist

    def shake(self):
        """
        摇一摇手机
        :return:
        """
        self.D.friend_shake()
