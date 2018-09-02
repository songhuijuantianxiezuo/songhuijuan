#coding:UTF-8
import unittest
from HtmlTestRunner import HTMLTestRunner
from testcase.case1 import Test
from testcase.case2 import Test_1

test_cases = (Test,Test_1)
# test_cases = (Test_1,)

#加载全部函数
def getsuits(loader,tests):
    suite = unittest.TestSuite()
    # suite.addTest(Test_1('test_2'))
    # suite.addTest(Test('test_1'))
    for test_class in tests:
        all_tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(all_tests)
        #将类里所有的函数加载到suite里
    return suite

if __name__ =='__main__':
    # runner = unittest.TextTestRunner()
    loader = unittest.TestLoader()   #加载器
    # suite = getsuit()
    suites = getsuits(loader,test_cases)
    # runner = HTMLTestRunner(output="reports")
    runner = HTMLTestRunner(output="example_suit")        #这个output是输出目录
    runner.run(suites)
    #为什么生成的report有乱码？？？