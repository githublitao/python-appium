# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
#   读取测试用例
import xlrd
import logging
import re
from Exception import Custom_exception
import log


class Excel:

    def __init__(self, fp):
        try:
            self.data = xlrd.open_workbook(fp)
        except Exception, e:
            logging.error("%s" % e)
        try:
            self.case = self.data.sheet_by_name(u'测试用例')
            self.case_num = self.case.nrows                         # 测试用例行数
            self.procedure = self.data.sheet_by_name(u'测试步骤')
            self.procedure_num = self.procedure.nrows               # 测试步骤行数
        except Exception as e:
            log.exception_handling(e)
            raise Custom_exception.OpenXlsError

#   根据传入的测试用例case_id，获得该case的操作步骤
    def get_case_desc(self, case_id):
        pattern = re.compile(ur'[1-9]\d*')       # 正则用于匹配数字
        pattern1 = re.compile("'(.*?)'")         # 正则用于匹配字符串
        test_procedure = []                     # 用例操作步骤列表
        test_title = pattern1.findall(str(self.case.row(case_id)[4]).decode("unicode_escape").encode("utf8"))[0]  # 用例标题
        #  用例方法名称
        test_name = pattern1.findall(str(self.case.row(case_id)[3]).decode("unicode_escape").encode("utf8"))[0]
        test_procedure.append(test_title)
        test_procedure.append(test_name)
        for i in range(1, self.procedure_num):
            case = int(pattern.findall(str(self.procedure.row(i)[0]))[0])
            if case == case_id:         # 判断操作步骤表中的用例与传入的用例相同
                # 操作步骤序号
                procedure = int(pattern.findall(str(self.procedure.row(i)[1]))[0])
                # 操作方法
                operation = pattern1.findall(str(self.procedure.row(i)[3]).decode("unicode_escape").encode("utf8"))[0]
                # 元素pageName
                page_name = pattern1.findall(str(self.procedure.row(i)[4]).decode("unicode_escape").encode("utf8"))[0]
                # 定位元素类型
                type_element = pattern1.findall(str(self.procedure.row(i)[5]).decode("unicode_escape").encode("utf8"))[0]
                # 定位数值
                try:
                    value = pattern1.findall(str(self.procedure.row(i)[6]).decode("unicode_escape").encode("utf8"))[0]
                except:
                    value = int(pattern.findall(str(self.procedure.row(i)[6]))[0])
                case_element = [procedure, operation,
                                page_name, type_element, value]
                test_procedure.append(case_element)
        return test_procedure    # 单用例执行步骤

    # 用例条数
    def case_num(self):
        return self.case_num




