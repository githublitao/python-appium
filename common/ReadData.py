# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
#   读取测试用例
import xlrd as xlrd

from Exception import Custom_exception
from common import Path, creat_case

case = []


class ReadCaseExcel:
    # fp 测试用例路径
    def __init__(self):
        global case
        try:
            self.data = xlrd.open_workbook(Path.scan_files(postfix='case.xls'))
            case = self.data.sheet_by_name(u'测试用例')
            self.case_num = case.nrows                         # 测试用例行数
        except Exception as e:
            creat_case.exception_handling(e)
            raise Custom_exception.OpenXlsError

    @staticmethod
    def result_list(first, end):
        """
        构造测试结果表
        :param first: 开始用例编号
        :param end: 结束用例编号
        :return:
        """
        global case
        results = []
        for case_id in range(first, end):
            single_results = []
            number = int(case.row(case_id)[0].value)
            mod_ule = case.row(case_id)[1].value.encode('utf8')
            test_point = case.row(case_id)[2].value.encode('utf8')
            test_name = case.row(case_id)[4].value.encode('utf8')
            degree_of_importance = case.row(case_id)[5].value.encode('utf8')
            expected_result = case.row(case_id)[6].value.encode('utf8')
            single_results.append(number)
            single_results.append(mod_ule)
            single_results.append(test_point)
            single_results.append(test_name)
            single_results.append(degree_of_importance)
            single_results.append(expected_result)
            results.append(single_results)
        return results

    def case_num(self):
        """
        用例条数
        :return:
        """
        return self.case_num


class ReadStepExcel:
    """
    fp 测试步骤表路径
    case 测试用例数据列表
    """
    def __init__(self):
        global case
        try:
            self.data = xlrd.open_workbook(Path.scan_files(postfix='step.xls'))
            self.procedure = self.data.sheet_by_name(u'测试步骤')
            self.procedure_num = self.procedure.nrows               # 测试步骤行数
            self.case = case
        except Exception as e:
            creat_case.exception_handling(e)
            raise Custom_exception.OpenXlsError

    def get_case_desc(self, case_id):
        """
        根据传入的测试用例case_id，获得该case的操作步骤
        :param case_id: 测试用例编号
        :return:
        """
        # pattern = re.compile(ur'[1-9]\d*')       # 正则用于匹配数字
        # pattern1 = re.compile("'(.*?)'")         # 正则用于匹配字符串
        test_procedure = []                     # 用例操作步骤列表
        index = int(self.case.row(case_id)[0].value)
        # 用例标题
        test_title = self.case.row(case_id)[4].value.encode("utf8")
        # test_title = pattern1.findall(str(self.case.row(case_id)[4]).decode("unicode_escape").encode("utf8"))[0]
        #  用例方法名称
        test_name = self.case.row(case_id)[3].value.encode("utf8")
        # test_name = pattern1.findall(str(self.case.row(case_id)[3]).decode("unicode_escape").encode("utf8"))[0]
        test_procedure.append(index)
        test_procedure.append(test_title)
        test_procedure.append(test_name)
        for i in range(1, self.procedure_num):
            case = int(self.procedure.row(i)[0].value)
            # case = int(pattern.findall(str(self.procedure.row(i)[0]))[0])
            if case == case_id:         # 判断操作步骤表中的用例与传入的用例相同
                # 操作步骤序号
                procedure = int(self.procedure.row(i)[1].value)
                # procedure = int(pattern.findall(str(self.procedure.row(i)[1]))[0])
                # 操作方法
                operation = self.procedure.row(i)[3].value.encode('utf8')
                # operation = pattern1.findall(str(self.procedure.row(i)[3]).decode("unicode_escape").encode("utf8"))[0]
                # 元素pageName
                page_name = self.procedure.row(i)[4].value.encode('utf8')
                # page_name = pattern1.findall(str(self.procedure.row(i)[4]).decode("unicode_escape").encode("utf8"))[0]
                # 定位元素类型
                type_element = self.procedure.row(i)[5].value.encode('utf8')
                # type_element = pattern1.findall(str(self.procedure.row(i)[5])
                #                                 .decode("unicode_escape").encode("utf8"))[0]
                # 定位数值
                try:
                    value = self.procedure.row(i)[6].value.encode('utf8')
                    # value = pattern1.findall(str(self.procedure.row(i)[6]).decode("unicode_escape").encode("utf8"))[0]
                except:
                    value = int(self.procedure.row(i)[6].value)
                    # value = int(pattern.findall(str(self.procedure.row(i)[6]))[0])
                case_element = [procedure, operation,
                                page_name, type_element, value]
                test_procedure.append(case_element)
                # 根据步骤id排序
                count = len(test_procedure)
                for index in range(1, count):
                    key = test_procedure[index][0]
                    j = index - 1
                    while j >= 3:
                        if test_procedure[j][0] >= key:
                            mobile_list = test_procedure[j + 1]
                            test_procedure[j + 1] = test_procedure[j]
                            key = mobile_list[0]
                            test_procedure[j] = mobile_list
                        j -= 1
        return test_procedure    # 单用例执行步骤
