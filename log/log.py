#coding:UTF-8
import logging

def log():
    log = logging.getLogger("log")      #log名称
    log.setLevel(logging.DEBUG)    #大写字母debug，设置显示的级别
    l = logging.FileHandler(r'C:\Users\lenovo\Desktop\songhuijuan\log\log.log',encoding='utf-8')     #日志存放目录
    formatter = logging.Formatter('%(asctime)-10s  %(name)-15s  %(levelname)-15s  %(message)-15s')
    l.setFormatter(formatter)
    #将l设置成固定格式
    log.addHandler(l)
    #将日志名称加入到日志中去
    return log