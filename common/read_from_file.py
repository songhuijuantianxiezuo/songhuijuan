#coding:UTF-8
import sys
sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")     #找不到时添加环境变量
import time
import csv
import xlrd
import re
import yaml
import json
import configparser
from file_into import *




def read_from_csv(filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.csv'):
    
    with open(filepath,'r') as fo:
        # fo.write(str(self.content))     
        f = csv.reader(fo)
        for row in f:
            print(row)    #writerow是写入单行，writerows是写入多行
    # return filepath



def read_from_xl(self,filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.xls'):
    # with open(filepath,'w+') as fo:
    #     fo.write(str(self.content))
    # return filepath
    # workbook = xlrd.s(encoding='utf-8')
    # worksheet = workbook.add_sheet('my sheet')
    # # 写入excel
    # # 参数对应 行, 列, 值
    # worksheet.write(1,1, self.content)
    # # 保存
    # workbook.save(filepath)           #为什么生成的文件是二进制？？？
#         data = xlrd.open_workbook('excelFile.xls')     #打开文件
#         table = data.sheets()[0]          #通过索引顺序获取
#         table = data.sheet_by_index(0) #通过索引顺序获取
#         table = data.sheet_by_name(u'Sheet1')#通过名称获取
#         #获取整行和整列的值（数组）
#         table.row_values(i)
#         table.col_values(i)
#         #获取行数和列数
# 　　    nrows = table.nrows
#         ncols = table.ncols
#        #循环行列表数据
#         for i in range(nrows ):
#             print table.row_values(i)
#         #单元格
#         cell_A1 = table.cell(0,0).value
#         cell_C4 = table.cell(2,3).value
#         #使用行列索引
#         cell_A1 = table.row(0)[0].value
#         cell_A2 = table.col(1)[0].value



def read_from_txt(filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.txt'):
    with open(filepath,'r') as fo:
        l = fo.read()
        for row in l:
            print(row)

def read_from_yaml(filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.yaml'):
    with open(filepath,'r') as fo:
        print(yaml.load(fo))
#             # yaml.dump(self.content,fo)
#             #fo.load(str(b))   #读取yaml文件
#         # return filepath

def read_from_json(filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.json'):
    with open(filepath,'r') as fo:
        c = json.load(fo)    #将python转码为json格式
        print(str(c))
        # fo.write(c)
    # return filepath

def read_from_ini(filepath=r'C:\Users\lenovo\Desktop\songhuijuan\file_into\file1.ini'):
    fo = configparser.ConfigParser()
# fo.add_section("1")
# fo.set('1','%s'%(self.content),'3')
# with open(filepath,'r') as f:
    fo.read(filepath)
    print(fo.sections())
    print(fo['1']['acdd'])
    print(fo.get('1','acdd'))
    # fo.write(f)      #非 f.write(fo)！！！  
# # return filepath

if __name__ =="__main__":
    read_from_ini()


# if __name__ =="__main__":
# a = {"userAccount":"54321","date":"2016-12-06 10:26:17","ClickTime": 1480991177,"jsonInfo":{"lon":121.5612,"lat":31.1832,"isGps":1,"netType":"WIFI","addr":"浦东新区长江南路1099弄56号"}}
# w = Write_into_file(a)
# w.write_into_json()
   
