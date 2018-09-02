#coding:UTF-8
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")     #找不到时添加环境变量
from selenium import webdriver

def getdriver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    return driver

def geturl(driver,url):
    driver.get(url)
    driver.maximize_window()