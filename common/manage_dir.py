
# import time
import os

def get_file_name(name):
    current_dir = os.getcwd()
    # s_current_dir = os.path.split(current_dir)[0]
    new_dir = os.path.join(current_dir,"file_into","%s"%(name))    #若file_into不存在则报错
    # print(new_dir)
    # print(current_dir)
    return new_dir

# get_file_name("1.txt")