import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

desired_capabilities={
    "platformName":"Android",
    "platformVersion":"12.0",
    "deviceName":"",
    "appPackage":"",
    "appActivity":"",
    "newCommandTimeout":''

}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)
driver.find_element(AppiumBy.ID,value=)
if __name__ == '__main__':
    unittest.main()
