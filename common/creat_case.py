#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import Path
import ReadData
import log
from case import run_list
import logging
from Exception import Custom_exception


@log.deco(u'生成测试用例脚本')
def test_case():
    ob = ReadData.Excel(Path.scan_files(postfix='.xls'))
    fist, end = run_list.test_case_list(ob.case_num)
    try:
        f = open(Path.scan_files(prefix='Test_Case'), 'w')
    except Exception as e:
        log.exception_handling(e)
        raise Custom_exception.CreatTestCaseError
    f.write('#! /usr/bin/python\n')
    f.write('# -*- coding:utf-8 -*-\n')
    f.write('import unittest\n')
    f.write('import time\n')
    f.write('from common import log\n')
    f.write('from common import operation\n')
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
        f.write('    @log.deco(u"%s")\n' % ob.get_case_desc(i)[0])
        f.write('    def %s(self):\n' % ob.get_case_desc(i)[1])
        f.write('        try:\n')
        for j in range(2, len(ob.get_case_desc(i))):
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
        f.write('        except Exception as e:\n')
        f.write('            log.exception_handling(e, u"%s", self.method_name, self.OP)'
                % ob.get_case_desc(i)[0])
        f.write('\n')
    try:
        f.close()
    except Exception as e:
        logging.error(e)
        raise Custom_exception.CloseFileError
