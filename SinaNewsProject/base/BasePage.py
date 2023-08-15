class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #定位元素
    def locate(self,locator):
        return self.driver.find_element(*locator)