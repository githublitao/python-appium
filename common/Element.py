#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from Exception import Custom_exception
from common import creat_case


class Element:
    """
    封装Appium中关于元素对象的方法
    """

    def __init__(self, driver):
        self.driver = driver

    def get(self, message):
        """
        获取页面元素
        :param message: 单个元素信息列表包含，方式type， 超时时间time， 值value
        :return:
        """
        way, timeout, value = message
        way_list = ['xpath', 'id', 'ids', 'name', 'classes_name', 'accessibility_id']
        for i in way_list:
            if i == way and i == 'xpath':
                element = self.driver.find_element_by_xpath(value)
                return element
            elif i == way and i == 'id':
                element = self.driver.find_element_by_id(value)
                return element
            elif i == way and i == 'ids':
                elements = self.driver.find_elements_by_id(value)
                return elements
            elif i == way and i == 'name':
                element = self.driver.find_element_by_name(value)
                return element
            elif i == way and i == 'classes_name':
                elements = self.driver.find_elements_by_class_name(value)
                return elements
            elif i == way and i == 'accessibility_id':
                elements = self.driver.find_element_by_accessibility_id(value)
                return elements
            else:
                raise Custom_exception.WrongLocation

    def wait_element(self, message):
        """
        等待页面元素加载
        :param message: 单个元素信息列表包含，方式tpye， 超时时间time， 值value
        :return:
        """
        way, timeout, value = message
        timeout = int(timeout)
        way_list = ['xpath', 'id', 'name', 'classes_name']
        for i in way_list:
            if i == way and i == 'xpath':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value)))
                return element
            elif i == way and i == 'id':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value)))
                return element
            elif i == way and i == 'name':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value)))
                return element
            elif i == way and i == 'classes_name':
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                return element
            else:
                raise Custom_exception.WrongLocation

    def over(self):
        """
        关闭driver
        :return:
        """
        try:
            element = self.driver.quit()
            return element
        except Exception as e:
            creat_case.exception_handling(e)

    def get_screen(self, path):
        """
        截图
        :param path: 图片存放路径
        :return:
        """
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        """
        获取屏幕大小
        :return:
        """
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        """
        向上移动
        :return:
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        """
        向下移动
        :return:
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        """
        向左移动
        :return:
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        """
        向右移动
        :return:
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def back(self):
        """
        物理键返回
        :return:
        """
        self.driver.keyevent(4)

    def switch_h5(self):
        """
        切换至webview
        :return:
        """
        self.driver.switch_to.context("WEBVIEW")

    def switch_app(self):
        """
        切换至app原生页面
        :return:
        """
        self.driver.switch_to.context("NATIVE_APP")

    def get_page(self, key):
        """
        获取当前页面的树形结构源代码，与uiautomatorviewer截屏所展示出来的结构是相同的，判断是否存在，不存在返回-1
        :param key:
        :return:
        """
        return self.driver.page_source.find(key)

    def friend_shake(self):
        """
        摇一摇手机
        :return:
        """
        self.driver.shake()
