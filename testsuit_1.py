#coding:UTF-8
import unittest
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")
# import HtmlTestRunner
from testcase.case1 import Test
from testcase.case2 import Test_1

#单独加载某函数     //总是报找不到类中的函数？？？
def getsuit():
    suite = unittest.TestSuite()
    suite.addTest(Test_1('test_2'))
    # suite.addTest(Test("test1"))     #引用了DDT的不能用addTest这种方式单独加载
    return suite

# if __name__ =='__main__':
#     runner = unittest.TextTestRunner()
#     loader = unittest.TestLoader()   #加载器
#     suite = getsuit()
#     runner.run(suite)
