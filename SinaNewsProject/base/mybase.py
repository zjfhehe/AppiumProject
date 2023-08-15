from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
import unittest
from selenium.common import NoSuchElementException


class DC_base(unittest.TestCase):
    def setUp(self) -> None:
        self.desired_capabilities = {}
        self.desired_capabilities["platformName"] = "Android"
        self.desired_capabilities["platformVersion"] = "12.0"
        self.desired_capabilities["deviceName"] = "3437789507001HM"
        self.desired_capabilities["app"] = r"C:\Users\zjf\Downloads\com.sina.news.apk"
        self.desired_capabilities["newCommandTimeout"] = 240
        self.desired_capabilities["appPackage"] = "com.sina.news"
        self.desired_capabilities["appActivity"] = ".module.launch.activity.PowerOnScreen"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_capabilities)
        self.driver.implicitly_wait(12)
    def tearDown(self) -> None:
        self.driver.quit()
    def is_element_show(self,how,what):
        try:
            self.driver.find_element(how,what)
        except NoSuchElementException as e:
            return False
        return True
