# import sys
# sys.path.append("C:\\Users\\lenovo\\Desktop\\songhuijuan")


# from abc import abstractclassmethod    #这个是什么？在pom里面的作用是？

# class Base(object):        #为什么这里加object？可写可不写

#     def __init__(self,driver):         #为什么要加上driver？
#         # self._validate_page(driver)       #这个是什么？没看懂,作用是什么？
#         self.driver = driver

    # @abstractclassmethod
    # def _validate_page(self,driver):      #没有任何实际意义，为什么要加这个函数？
    #     return

# class InvalidPageException(Exception):     #为什么要加这个？作用是什么？
#     """ Throw this exception when you don't find
#         the correct page 
#     """
#     pass