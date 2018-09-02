import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")

# from pom.po import Base
# from pom.po import InvalidPageException
# from common.clickelement import find_element

class Homepage():
    hao_123 = '//*[@id="u1"]/a[2]'

    def __init__(self,driver):
        # super(Homepage,self).__init__(driver)
        self.driver = driver

    def click_hao123(self):
        # return self.driver.find_element_by_xpath(self.hao_123).click()
        return self.driver.find_element_by_xpath(self.hao_123).click()
        #注意加self,到底什么时候加self，什么时候不加呢？我看driver前面要加，类里面自定义的变量和传入的变量要加self

    # def _validate_page(self,driver):
    #     try:
    #         # self.driver.find_element_by_xpath(self.hao_123)
    #         self.driver.find_element_by_xpath(self.hao_123)
    #     except:
    #         raise InvalidPageException("hao123加载失败")   
    #     #加raise的作用是：是不是不加raise会报错，加raise就不会再报错了？？还有后面这个是什么错误？
