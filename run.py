import unittest
from BeautifulReport import BeautifulReport

# 用例存放位置，把放用例的地址填上去填到用例的文件夹
from utils.sendQWechart import sendQWechart

test_case_path = "./testCase"
# 用来测试报告存放位置
report_path = './report'
# 自定义测试报告名称
filename = '测试报告'
# html里面报告汇总用例的名称
description = 'Procese接口测试'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
# 我这里运行全部的测试用例
pattern = "*.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    # unittest的一个方法，智能获取文件下面的case去跑
    result = BeautifulReport(test_suite)
    # 只能绘制图表
    result.report(filename=filename, description=description, report_dir=report_path)
    # 发送企微消息
    testsRun = result.testsRun
    success_count = result.success_count
    failure_count = result.failure_count
    sendQWechart().send_msg_markdown(testsRun, success_count, failure_count)
    # TODO 发送邮件报告

