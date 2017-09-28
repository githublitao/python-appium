# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
import xlrd
from xlutils.copy import copy
import Path

class Excel:

    def __init__(self, fp):
        try:
            self.data = xlrd.open_workbook(fp)
        except Exception, e:
            print str(e)

    def write_fail(self, case_num):
        length = len(case_num)
        print length
        wb = copy(self.data)
        ws = wb.get_sheet(2)
        for i in range(0, length):
            print i
            extent = len(case_num[i])
            for j in range(0, extent):
                ws.write(i+1, j, case_num[i][j])
        wb.save(Path.father_path+'\\test_report.xls')


ob = Excel(Path.scan_files(postfix='case.xls'))
a = [[1,2,3,45,67,8],[2,3,4,5,667,7,2],[1,2,3,4,656,243,]]
ob.write_fail(a)
