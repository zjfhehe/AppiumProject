from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

# 启动计算器
desired_capabilities={}
desired_capabilities['platformName']='Android'
desired_capabilities['platformVersion']='12.0'
desired_capabilities['deviceName']='3437789507001HM'
desired_capabilities['appPackage']='com.android.bbkcalculator'
desired_capabilities['appActivity']='.Calculator'
desired_capabilities['newCommandTimeout']=240
desired_capabilities['']=''
desired_capabilities['']=''
desired_capabilities['']=''
desired_capabilities['']=''
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)

#操作3+5=
el1 = driver.find_element(by=AppiumBy.ID, value="com.android.bbkcalculator:id/digit_3")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="加")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.android.bbkcalculator:id/digit_5")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="=")
el4.click()

#等待3秒
sleep(3)
#关闭计算器
driver.quit()