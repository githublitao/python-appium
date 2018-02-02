#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月24日

@author: li tao
"""
from BasePage.ReadXml import BastPage
from common import Path


class Locator:
    """
    获取元素的定位方式，超时及定位值
    """

    def __init__(self):
        self.page = BastPage(Path.scan_files(prefix='page'))

    def get_type(self, page_name, locator):
        l = self.page.run(page_name, locator)
        return l['type'], l['timeOut'], l['value']