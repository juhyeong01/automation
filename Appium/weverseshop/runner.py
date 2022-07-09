import unittest
import HtmlTestRunner
from TestSuites.TestCaseWeverse import Test_Suites

'''
html-testrunner 모듈을 통해 수행되는 테스트 케이스의 결과를 보고서 형식으로 추출되도록 설정
'''


testcase = unittest.TestLoader().loadTestsFromTestCase(Test_Suites)

testsuite = unittest.TestSuite([testcase])

HtmlTestRunner.HTMLTestRunner(
                                output = "TestReport",
                                report_name = "Test_Report",
                                report_title = "Test_result",
                                combine_reports = True
).run(testsuite)