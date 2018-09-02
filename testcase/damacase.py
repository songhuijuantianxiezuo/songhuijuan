#coding:UTF-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('https://www.baidu.com/')
driver.maximize_window()
#点击新闻按钮
news = driver.find_element_by_css_selector('#u1 > a:nth-child(1)').click()
#获得所有的窗口
allwindows = driver.window_handles
print(len(allwindows))
#切换到最后一个窗口
driver.switch_to_window(allwindows[len(allwindows)-1])
# driver.delete_all_cookies()
# driver.add_cookie({'name':'BAIDUID','value':'1A17A79C8A382256D71B04E9D3BA3A74:FG=1'})
# driver.refresh()
##为什么我添加百度的cookie不成功
driver.find_element_by_id('passLog').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_12__userName"]').send_keys('15000011941')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_12__password"]').send_keys('324476')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_12__memberPass"]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_12__submit"]').click()
time.sleep(3)
allwindows = driver.window_handles
driver.switch_to_window(allwindows[len(allwindows)-1])
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__32__button_send_mobile"]').click()
# a = input("验证码是：")
# driver.find_element_by_xpath('//*[@id="TANGRAM__32__input_label_vcode"]').click()
# driver.find_element_by_xpath('//*[@id="TANGRAM__32__input_label_vcode"]').send_keys(abs)
##百度页面，为何无法输入验证码，报错信息：元素找不到 
