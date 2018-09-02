#coding:UTF-8
import unittest
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")
# from common.clickelement import find_element
from common.openurl import *
from common.screenshot import *
from common.switch_to_last_window import *
from log.log import log
from pom.po_homepage import Homepage
from pom.po_selectpage import Selectpage

l = log()

class Test_1(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        cls.driver = getdriver()

    # @unittest.skip("sssss")
    def test_1(self,a = 'search-input'):
        geturl(self.driver,'https://www.baidu.com/')      #打开该url
        # find_element('//*[@id="u1"]/a[2]').click()      #点击hao123
        e = Homepage(self.driver)       
        e.click_hao123()
        # switch_to_last_window(self.driver)    #切换到新的页面
        # a = 'search-input'
        
        move_and_screenshot(self.driver,a,"now")      #移动到某元素并截屏，a是js的ByByid元素    //为什么总是报各种 not defined???
        l.info('test_1成功')      #写入日志

    # def test_2(self):
    #     geturl(self.driver,'https://www.baidu.com/')      #打开该url
    #     # find_element('//*[@id="u1"]/a[2]').click()      #点击hao123
    #     e = Homepage(self.driver)
    #     e.click_hao123()
    #     switch_to_last_window(self.driver)    #切换到新的页面
    #     move_screenshot(self.driver,100,"new")      #移动多少距离并截图保存至某文件
    #     l.error('test_2 成功')        #写入日志
            

if __name__ == '__main__':
    unittest.main()



# if __name__=="__main__":
#     unittest.main()
#     driver = getdriver()
#     b = Test_1()
#     b.test_1(driver)
#     b.test_2(driver)

# if __name__=="__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\lenovo\Desktop\songhuijuan\report'))


        


        
        
