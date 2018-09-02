#coding:UTF-8
from selenium import webdriver
import time
import requests
import re
import csv
# import HtmlTestRunner
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
print(driver.current_url)
allwindows = driver.window_handles
driver.switch_to_window(allwindows[len(allwindows)-1])
# print(driver.page_source)     #driver.page_source是打印源码
# driver.switch_to_window(driver.current_url)   这个不对，报错：没有这样的窗口
driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('a')
driver.find_element_by_xpath('//*[@id="search-form"]/div[2]/input').click()
allwindows = driver.window_handles
driver.switch_to_window(allwindows[len(allwindows)-1])
current_url = driver.current_url
# response = requests.get(current_url)
response = driver.page_source
with open(r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.csv','w+') as fo:
    # fo.write(response)
# print(response.text)
    # 为什么文件中写入的内容要比实际的内容少好多？
    a = re.compile("https*",re.S|re.I)
    b = re.findall(a,response)
    fo.write(str(b))
for i in range(10,90,10):
    driver.execute_script(r'document.scrollingElement.scrollTop=900-%d'%(i*10))
    driver.save_screenshot(r'C:\Users\lenovo\Desktop\songhuijuan\screenshot\%d.png'%(i*10))


