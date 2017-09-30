# -*- coding:utf-8 -*-
"""
Created on 2017年9月28日

@author: lt
"""
#   读取测试用例
# import xlrd
# import logging
# from Exception import Custom_exception
# from common import creat_case, Path
# Path.scan_files(postfix='.xls')
#
#
# class ReadExcelResult:
#
#     def __init__(self, fp):
#         try:
#             self.data = xlrd.open_workbook(fp)
#         except Exception, e:
#             logging.error("%s" % e)
#         try:
#             self.case = self.data.sheet_by_name(u'测试结果')
#             self.case_num = self.case.nrows                         # 读取测试结果条数+1
#         except Exception as e:
#             creat_case.exception_handling(e)
#             raise Custom_exception.OpenXlsError
#
#     def test_results(self):
#         results = []
#         for i in range(1, self.case_num):
#             single_results = []
#             number = int(self.case.row(i)[0].value)
#             mod_ule = self.case.row(i)[1].value.encode('utf8')
#             test_point = self.case.row(i)[2].value.encode('utf8')
#             test_name = self.case.row(i)[3].value.encode('utf8')
#             degree_of_importance = self.case.row(i)[4].value.encode('utf8')
#             expected_result = self.case.row(i)[5].value.encode('utf8')
#             actual_result = self.case.row(i)[6].value.encode('utf8')
#             error_log = self.case.row(i)[7].value.encode('utf8')
#             error_screenshot = self.case.row(i)[8].value.encode('utf-8')
#             single_results.append(number)
#             single_results.append(mod_ule)
#             single_results.append(test_point)
#             single_results.append(test_name)
#             single_results.append(degree_of_importance)
#             single_results.append(expected_result)
#             single_results.append(actual_result)
#             single_results.append(error_log)
#             single_results.append(error_screenshot)
#             # single_results = [number, mod_ule, test_point, test_name, degree_of_importance, expected_result,
#             #                   actual_result, error_log]
#             results.append(single_results)
#         return results
from common import runtime
import datetime
from common import Path


def ab(l):
    end_time = datetime.datetime.now()
    run_time = (datetime.datetime.now()-runtime.start_time_test()).seconds
    second = run_time % 60
    minute = run_time / 60 % 60
    hours = run_time / 60 / 60 % 24
    day = run_time / 60 / 60 / 24
    elapsed_time = ' %s 天 %s 小时 %s 分 %s 秒' % (day, hours, minute, second)
    total_count = len(l)
    fail_count = 0
    error_count = 0
    for j in range(0, len(l)):
        if l[j][6] == 'error':
            error_count += 1
        if l[j][6] == 'fail':
            fail_count += 1
    fail_proportion = round(fail_count / total_count, 2)
    error_proportion = round(error_count / total_count, 2)
    success_proportion = 1-fail_proportion-error_proportion
    f = open(Path.father_path+'\\Test_Report\\'+runtime.test_start_time()+'.html', 'w')
    f.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>nidone测试报告</title>
</head>
<body>
    <h1 style="text-indent:2em;">nidone6测试报告</h1>
        <p style="text-indent:4em;">测速开始时间:
                <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span>
                </p>
        <p style="text-indent:4em;">测试结束时间:
                <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span>
                </p>
        <p style="text-indent:4em;">测试耗时:
                <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span>
                </p>
        <p style="text-indent:4em;">Total:
                <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span>
        Fail:        <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span>
        Error:
                <span style="display: inline-block;padding-left: 10px;text-indent: 0em;">%s</span></p>
        <p style="text-indent:4em;">
            <canvas id="canvas_circle" width="500" height="300" style="border:2px solid #0026ff;" >
                浏览器不支持canvas
            </canvas>
        </p>''' % (runtime.start_time_test(), end_time, elapsed_time, total_count, fail_count, error_count))

    f.write('''        <style type="text/css">
            table {
                width: 94%;
                table-layout: fixed;
                background-color:yellow				
}
            td {
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                height: 5px;
            }
        </style>
        <table border="1px" align="center">
            <tr>
                <th style="width: 25px;">测试ID</th>
                <th style="width: 80px;">所属模块</th>
                <th style="width: 70px;">测试点</th>
                <th style="width: 250px;">测试标题</th>
                <th style="width: 30px;">重要程度</th>
                <th style="width: 150px;">预期结果</th>
                <th style="width: 35px;">执行结果</th>
                <th style="width: 50px;">错误日志</th>
                <th style="width: 30px;">错误截图</th>
            </tr>''')
    for i in range(0, len(l)):
        if l[i][6] == '':
            l[i][6] = 'success'
        f.write('''            <tr bgcolor="#7cfc00">
                <td >%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td onmouseover="moveIn(this)">%s</td>
                <td>%s</td>>
                <td>''' % (l[i][0], l[i][1], l[i][2], l[i][3], l[i][4], l[i][5], l[i][6]))
        if l[i][7]:
            f.write('''             <a href="file://localhost/%s">错误日志</a>
                </td>>
                <td>
                    <a href="file://localhost/%s" target="_blank>">截图</a>
                </td>
            </tr>''' % (l[i][7].encode('utf8'), l[i][8].encode('utf8')))
    f.write('''        </table>
        <script>
            //绘制饼图
            function drawCircle(canvasId, data_arr, color_arr, text_arr)
            {
                var c = document.getElementById(canvasId);
                var ctx = c.getContext("2d");

                var radius = c.height / 2 - 20; //半径
                var ox = radius + 20, oy = radius + 20; //圆心

                var width = 30, height = 10; //图例宽和高
                var posX = ox * 2 + 20, posY = 30;   //
                var textX = posX + width + 5, textY = posY + 10;

                var startAngle = 0; //起始弧度
                var endAngle = 0;   //结束弧度
                for (var i = 0; i < data_arr.length; i++)
                {
                    //绘制饼图
                    endAngle = endAngle + data_arr[i] * Math.PI * 2; //结束弧度
                    ctx.fillStyle = color_arr[i];
                    ctx.beginPath();
                    ctx.moveTo(ox, oy); //移动到到圆心
                    ctx.arc(ox, oy, radius, startAngle, endAngle, false);
                    ctx.closePath();
                    ctx.fill();
                    startAngle = endAngle; //设置起始弧度

                    //绘制比例图及文字
                    ctx.fillStyle = color_arr[i];
                    ctx.fillRect(posX, posY + 20 * i, width, height);
                    ctx.moveTo(posX, posY + 20 * i);
                    ctx.font = 'bold 12px 微软雅黑';    //斜体 30像素 微软雅黑字体
                    ctx.fillStyle = color_arr[i]; //"#000000";
                    var percent = text_arr[i] + "：" + 100 * data_arr[i] + "%";
                    ctx.fillText(percent, textX, textY + 20 * i);
                }
            }


            function moveIn(obj)
            {
                obj.title=obj.innerHTML;
            }''')

    f.writelines('''            function init() {
                //绘制饼图
                //比例数据和颜色
                var data_arr = [%s, %s, %s];
                var color_arr = ["#00FF21", "#FFAA00", "#00AABB"];
                var text_arr = ["Fail", "Success", "Error"];

                drawCircle("canvas_circle", data_arr, color_arr, text_arr);
            }

            //页面加载时执行init()函数
            window.onload = init;
        </script>
</body
</html>''' % (fail_proportion, success_proportion, error_proportion))
    f.close()

