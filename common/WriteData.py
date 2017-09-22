# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
import xlrd
from xlutils.copy import copy
from Path import case_path
from Path import sheet_number_path


class Excel:

    def __init__(self, fp):
        try:
            self.data = xlrd.open_workbook(fp)
        except Exception, e:
            print str(e)
    #   测试执行失败，写入测试结果，原因，http状态

    def write_fail(self, case_id, result, reason, state):
        try:
            wb = copy(self.data)
            ws = wb.get_sheet(sheet_number_path())
            ws.write(case_id, 13, state)
            ws.write(case_id, 14, result )
            ws.write(case_id, 15, reason)
            wb.save(case_path())
        except:
            print '写入测试结果失败'
            raise
    #   测试执行成功，写入测试结果，返回状态

    def write(self, case_id, result, state):
        try:
            wb=copy(self.data)
            ws = wb.get_sheet(sheet_number_path())
            ws.write(case_id, 13, state)
            ws.write(case_id, 14, result )
            wb.save(case_path())
        except Exception as e:
            print '写入测试结果失败: %s' % e
