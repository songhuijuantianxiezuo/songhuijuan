#coding:UTF-8
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")     #找不到时添加环境变量
import time
import csv
import xlwt
import re
import yaml
import json
import configparser

class Write_into_file:

    def __init__(self,content):
        self.content = content

    def write_into_csv(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.csv'):
        
        with open(filepath,'w+') as fo:
            # fo.write(str(self.content))     
            f = csv.writer(fo)
            for i in range(1,6):
                f.writerow([i,self.content])    #writerow是写入单行，writerows是写入多行
        # return filepath



    def write_into_xl(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.xls'):
        # with open(filepath,'w+') as fo:
        #     fo.write(str(self.content))
        # return filepath
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('my sheet')
        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(1,1, self.content)
        # 保存
        workbook.save(filepath)           #为什么生成的文件是二进制？？？




    def write_into_txt(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.txt'):
        with open(filepath,'w+') as fo:
            fo.write(str(self.content))
        return filepath



    def write_into_yaml(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.yaml'):
        with open(filepath,'w+') as fo:
            #读取yaml文件   yaml.load(fo)
            yaml.dump(self.content,fo)
            #fo.load(str(b))
        return filepath

    def write_into_json(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.json'):
        with open(filepath,'w+') as fo:
            c = json.dump(self.content,fo)    #将python转码为json格式
            # fo.write(c)
        # return filepath

    def write_into_ini(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.cfg'):
        fo = configparser.ConfigParser()
        fo.add_section("1")
        fo.set('1','%s'%(self.content),'3')
        with open(filepath,'w+') as f:
            fo.write(f)      #非 f.write(fo)！！！  
        # return filepath


class Zz:   #zz指正则

    def __init__(self):   #从b中筛选出所有的符合a要求的词
        pass
        

    def zzre(self,a,b):
        c = re.compile(a,re.S|re.I)
        d = re.findall(c,b)
        return d

class Time:

    def __init__(self):
        pass                  

    @property
    def time_name(self):
        # time_name_now = time.strftime(r"%Y-%m-%d",time.localtime())
        time_name_now = time.strftime(r"%Y-%m-%d_%H_%M_%S",time.localtime())   #加上时分秒就运行不成功了 ？？？
        return str(time_name_now)

if __name__ =="__main__":
    a = {"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"浦东新区长江南路1099弄56号"}}
    w = Write_into_file(a)
    w.write_into_json()

    # b = Time()
    # print(b.time_name)
    