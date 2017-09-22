#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import ReadData
import Path
from case import runlist
import log


@log.deco(u'生成测试用例脚本')
def test_case():
    ob = ReadData.Excel(Path.data_path())
    fist, end = runlist.test_case_list(ob.case_num)
    f = open(Path.case_py(), 'w')
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
            if ob.get_case_desc(i)[j][1] == 'sleep':
                f.write('        time.sleep(%s)\n' % ob.get_case_desc(i)[j][4])
            elif ob.get_case_desc(i)[j][1] == 'sw_h5':
                f.write('            self.OP.sw_h5()\n')
            elif ob.get_case_desc(i)[j][1] == 'sw_app':
                f.write('            self.OP.sw_app()\n')
            elif ob.get_case_desc(i)[j][1] == 'send_keys':
                f.write('            self.OP.send_keys("%s", "%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3], ob.get_case_desc(i)[j][4]))
            elif ob.get_case_desc(i)[j][1] == 'clicks':
                f.write('            self.OP.clicks("%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3]))
            elif ob.get_case_desc(i)[j][1] == 'wait_element':
                f.write('            self.OP.wait_element("%s", "%s")\n'
                        % (ob.get_case_desc(i)[j][2], ob.get_case_desc(i)[j][3]))
            elif ob.get_case_desc(i)[j][1] == 'go_back':
                f.write('            self.OP.go_back()\n')
            elif ob.get_case_desc(i)[j][1] == 'swipe_up':
                f.write('            self.OP.swipe_up()\n')
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_down':
                f.write('            self.OP.swipe_to_down()\n')
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_left':
                f.write('            self.OP.swipe_to_left()\n')
            elif ob.get_case_desc(i)[j][1] == 'swipe_to_right':
                f.write('            self.OP.swipe_to_right()\n')
        f.write('        except Exception as e:\n')
        f.write('            log.exception_handling(e, self.method_name, u"%s", self.OP)'
                % ob.get_case_desc(i)[0])
        f.write('\n')
    f.close()
