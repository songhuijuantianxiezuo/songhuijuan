import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")

# from pom.po import Base
# from pom.po import InvalidPageException
# from common.clickelement import find_element

from common.openurl import getdriver

class Selectpage():

    hao123_ssk = '//*[@id="search-input"]'      #hao123搜索框
    hao123_bdyx = '//*[@id="search-form"]/div[2]/input'    #hao123百度一下
    baidu_tz = '//*[@id="kw"]'    #跳转后输入框的内容
    baidu_tz_1 = "kw"
    #后续元素多时，可以用读取文件的方式，来给元素赋值
    def __init__(self,driver):
        # super(Selectpage,self).__init__(driver)
        self.driver = driver

    def select(self,ssk):                     
        #是不是类中方法的参数，必不能来源于外部，必须是类中定义，或通过实例化类，来将参数传进来？例如下文中的ssk参数
        #答：不是，可以从外部传进来
        self.driver.find_element_by_xpath(self.hao123_ssk).send_keys(ssk)
        # find_element(self.hao123_ssk).send_keys(ssk)
        self.driver.find_element_by_xpath(self.hao123_bdyx).click()
        # find_element(self.hao123_bdyx).click()

    # # @property
    # def tz_msg(self):             #跳转信息
    #     # return self.driver.find_element_by_xpath(self.baidu_tz).text.strip()
    #     return self.driver.find_element_by_id(self.baidu_tz_1).


if __name__ == '__main__':
    driver= getdriver()
    driver.get("https://www.hao123.com/")
    s = Selectpage(driver)
    s.select('hhhhhhhh')
    print(s.tz_msg())
    # driver.find_element_by_id
