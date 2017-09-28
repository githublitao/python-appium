# -*- coding:utf-8 -*-
"""
Created on 2017年9月28日

@author: lt
"""
#   读取测试用例
import xlrd
import logging
import re
from Exception import Custom_exception
from common import log, Path
Path.scan_files(postfix='.xls')


class ReadExcelResult:

    def __init__(self, fp):
        try:
            self.data = xlrd.open_workbook(fp)
        except Exception, e:
            logging.error("%s" % e)
        try:
            self.case = self.data.sheet_by_name(u'测试结果')
            self.case_num = self.case.nrows                         # 读取测试结果条数+1
        except Exception as e:
            log.exception_handling(e)
            raise Custom_exception.OpenXlsError

    def test_results(self):
        results = []
        for i in range(1, self.case_num):
            single_results = []
            number = int(self.case.row(i)[0].value)
            mod_ule = self.case.row(i)[1].value.encode('utf8')
            test_point = self.case.row(i)[2].value.encode('utf8')
            test_name = self.case.row(i)[3].value.encode('utf8')
            degree_of_importance = self.case.row(i)[4].value.encode('utf8')
            expected_result = self.case.row(i)[5].value.encode('utf8')
            actual_result = self.case.row(i)[6].value.encode('utf8')
            error_log = self.case.row(i)[7].value.encode('utf8')
            error_screenshot = self.case.row(i)[8].value.encode('utf-8')
            single_results.append(number)
            single_results.append(mod_ule)
            single_results.append(test_point)
            single_results.append(test_name)
            single_results.append(degree_of_importance)
            single_results.append(expected_result)
            single_results.append(actual_result)
            single_results.append(error_log)
            single_results.append(error_screenshot)
            # single_results = [number, mod_ule, test_point, test_name, degree_of_importance, expected_result,
            #                   actual_result, error_log]
            results.append(single_results)
        return results

