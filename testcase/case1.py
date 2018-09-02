#coding:UTF-8
import unittest
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")
# from common.clickelement import find_element
from common.openurl import *
from common.switch_to_last_window import *
from common.write_into_file import Write_into_file,Zz,Time
from common.manage_dir import get_file_name
from ddt import data,file_data,ddt,unpack
import csv
from pom.po_homepage import Homepage
from pom.po_selectpage import Selectpage
import HtmlTestRunner
from log.log import log

l = log()

def get_data_csv(filename):
    users = []
    with open(filename,'r',encoding='UTF-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users

@ddt
class Test(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = getdriver()

    def setUp(self):
        self.driver = getdriver()

    @data(*get_data_csv("./data_from/data.csv"))
    @unpack
    def test1(self,data_1,data_2,data_3,data_4):
        geturl(self.driver,'https://www.baidu.com/')      #打开该url
        # find_element('//*[@id="u1"]/a[2]').click()      #点击hao123
        e = Homepage(self.driver)       
        e.click_hao123()
        #l.info('点击hao123')    #写入日志
        switch_to_last_window(self.driver)    #切换到新的页面
        # find_element('//*[@id="search-input"]').send_keys(data_1)    #在好123的搜索框中输入搜索字符
        f = Selectpage(self.driver)
        f.select(data_1)           #为什么没提示？？
        # find_element('//*[@id="search-form"]/div[2]/input').click()     #点击百度一下
        switch_to_last_window(self.driver)    #切换到新的页面
        try:
        # print(self.assertEqual(f.tz_msg(),data_2))  #验证是否一致     assert前加self
            l.info('success')
            self.assertEqual('foo'.upper(), 'FOO')
        except:
            print(data_3)
            l.info(data_3)
        # self.assertEqual('foo'.upper(), 'FOO')

        response = get_source(self.driver)      #得到当前界面的源码
        a = Zz()    #得到源码中的匹配信息
        b = a.zzre(data_4,response)      #为什么没有提示信息???类有提示，但是函数没提示？？
        g = Time()
        h = g.time_name + ".txt"
        c = get_file_name(h)    #得到文件名称
        print(c)
        d = Write_into_file(b)      #将匹配到的信息b写入到文件c当中
        d.write_into_txt(c)

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_suit'))