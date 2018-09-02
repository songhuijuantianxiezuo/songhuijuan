#coding:UTF-8
from common.openurl import *

def switch_to_last_window(driver):
    allwindows = driver.window_handles
    driver.switch_to_window(allwindows[len(allwindows)-1])
    print(r"now_url_is:",driver.current_url)

def get_source(driver):
    response = driver.page_source
    return response
