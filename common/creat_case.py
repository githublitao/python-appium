#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import xlwt as xlwt

from case import run_list
from Exception import Custom_exception
import logging
import logging.config
from common import ReadData, Path, runtime, mkdir_log_directory, log

l = []


@log.deco('初始化用例')
def test_case():
    global l
    case_excel = ReadData.ReadCaseExcel()
    ob = ReadData.ReadStepExcel()
    fist, end = run_list.test_case_list(case_excel.case_num)
    l = ReadData.ReadCaseExcel.result_list(fist, end)
    try:
        f = open(Path.scan_files(prefix='Test_Case'), 'w')
    except Exception as e:
        raise Custom_exception.CreatTestCaseError
    f.write('#! /usr/bin/python\n')
    f.write('# -*- coding:utf-8 -*-\n')
    f.write('import unittest\n')
    f.write('from common import log\n')
    f.write('from common import operation\n')
    f.write('from common import creat_case\n')
    f.write('# 测试用例\n')
    f.write('\n')
    f.write('\n')
    f.write('class ParametrizedTestCase(unittest.TestCase):\n')
    f.write('    """ TestCase classes that want to be parametrized should\n')
    f.write('        inherit from this class.\n')
    f.write('    """\n')
    f.write('    def __init__(self, method_name="runTest", run_time=None):\n')
    f.write('        super(ParametrizedTestCase, self).__init__(method_name)\n')
    f.write('        self.method_name = method_name\n')
    f.write('\n')
    f.write('\n')
    f.write('class Test(ParametrizedTestCase):\n')
    f.write('    def setUp(self):\n')
    f.write('        self.OP = operation.Opera()\n')
    f.write('\n')
    f.write('    def tearDown(self):\n')
    f.write('        self.OP.quit()\n')
    for i in range(fist, end):
        f.write('\n')
        f.write('    @log.deco(u"%s")\n' % ob.get_case_desc(i)[1])
        f.write('    def %s(self):\n' % ob.get_case_desc(i)[2])
        f.write('        try:\n')
        for j in range(3, len(ob.get_case_desc(i))):
            # 等待
            if ob.get_case_desc(i)[j][1] == 'sleep':
                f.write('        time.sleep(%s)\n' % ob.get_case_desc(i)[j][4])
            # 切换 h5
            elif ob.get_case_desc(i)[j][1] == 'sw_h5':
                f.write('            self.OP.sw_h5()\n')
            # 切换app
            elif ob.get_case_desc(i)[j][1] == 'sw_app':
                f.write('            self.OP.sw_app()\n')
            # 输入
            elif ob.get_case_desc(i)[j][1] == 'send_keys':
                f.write('            self.OP.send_keys("%s", "%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3], ob.get_case_desc(i)[j][4]))
            # 点击
            elif ob.get_case_desc(i)[j][1] == 'clicks':
                f.write('            self.OP.clicks("%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3]))
            # 等待
            elif ob.get_case_desc(i)[j][1] == 'wait_element':
                f.write('            self.OP.wait_element("%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3]))
            # 物理键返回
            elif ob.get_case_desc(i)[j][1] == 'go_back':
                f.write('            self.OP.go_back()\n')
            # 向上滑动
            elif ob.get_case_desc(i)[j][1] == 'swipe_up':
                f.write('            self.OP.swipe_up()\n')
            # 向下滑动
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_down':
                f.write('            self.OP.swipe_to_down()\n')
            # 向左滑动
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_left':
                f.write('            self.OP.swipe_to_left()\n')
            # 向右滑动
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_right':
                f.write('            self.OP.swipe_to_right()\n')
            # 判断页面内容是否存在
            elif ob.get_case_desc(i)[j][1] == 'page_element':
                f.write('            self.OP.judge_key("%s", "%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3], ob.get_case_desc(i)[j][4]))
            elif ob.get_case_desc(i)[j][1] == 'set_keys':
                f.write('            self.OP.set_keys("%s", "%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3], ob.get_case_desc(i)[j][4]))
            elif ob.get_case_desc(i)[j][1] == 'shake':
                f.write('            self.OP.shake()\n')
        f.write('        except Exception as e:\n')
        f.write('            creat_case.exception_handling(e, index=%s, test_name="%s", method_name=self.method_name,'
                ' op=self.OP)' % (ob.get_case_desc(i)[0], ob.get_case_desc(i)[1]))
        f.write('\n')
    try:
        f.close()
    except Exception as e:
        logging.error(e)
        raise Custom_exception.CloseFileError


def exception_handling(e, index=None, test_name=None, method_name=None, op=None):
    """
    错误处理
    :param e: 报错内容
    :param index: 用例编号
    :param test_name: 测试用例名称
    :param method_name: 测试用例对应方法
    :param op: 操作驱动
    :return:
    """
    global l
    logging.error(e)
    path = Path.report_path() + runtime.test_start_time() + '_error'
    mkdir_log_directory.mk_dir(path)                # 创建错误日志目录
    path1 = Path.log_path() + runtime.test_start_time() + '.log'
    if index:
        log_error = path + '\\' + test_name.decode('utf8') + '.txt'     # 记录错误日志文件
        way = path + '\\' + method_name + runtime.test_start_time() + '.png'
        op.screen(way, path)  # 截图
        log.error_log(path1, log_error, test_name)
        if 'AssertionError' in e:
            for i in range(0, len(l)):
                if index == l[i][0]:
                    l[i].append('fail')
                    l[i].append(log_error)
                    l[i].append(way)
        else:
            for i in range(0, len(l)):
                if index == l[i][0]:
                    l[i].append('error')
                    l[i].append(log_error)
                    l[i].append(way)
    else:
        log_error = path + '\\' + 'error.txt'  # 记录错误日志文件
        log.error_log(path1, log_error)


# 定义表格属性
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_excel():
    """
    初始化结果表
    :return:
    """
    global l
    # 创建工作簿
    try:
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建sheet
        data_sheet = workbook.add_sheet('测试结果')
    except Exception as e:
        exception_handling(e)
        raise Custom_exception.InitResultError
    title = ['用例ID', '所属模块', '测试点', '用例描述', '重要程度', '预期结果', '实际结果', '错误日志', '错误截图']
    try:
        for i in range(len(title)):
            data_sheet.write(0, i, title[i])
        for j in range(len(l)):
            for index in range(len(l[j])):
                if l[j][6] is None and index == 6:
                    data_sheet.write(j+1, 6, 'success')
                    continue
                data_sheet.write(j+1, index, l[j][index])
    except Exception as e:
        exception_handling(e)
        raise Custom_exception.WriteResultError
    try:
        # 保存文件
        workbook.save(Path.father_path+u'\\测试结果.xls')
    except Exception as e:
        exception_handling(e)
        raise Custom_exception.SaveReusltError


def test_result_list():
    global l
    return l
