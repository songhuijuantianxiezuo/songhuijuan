from common.openurl import getdriver

def move_and_screenshot(driver,elebyId,name):
    # print("document.getElementById('%s').scrollIntoView()"%(elebyId))
    driver.execute_script('document.getElementById("%s").scrollIntoView()'%(elebyId))   #注意不要丢了""
    # print("ele=====",elebyId,name)
    driver.save_screenshot(r'C:\Users\lenovo\Desktop\songhuijuan\screenshot\%s.png'%name)

def move_screenshot(driver,size,name):
    driver.execute_script(r'document.scrollingElement.scrollTop=%d'%size)
    driver.save_screenshot(r'C:\Users\lenovo\Desktop\songhuijuan\screenshot\%s.png'%name)
