from appium import webdriver
from time import sleep
#启动ContactManager
desired_capabilities={}
desired_capabilities["platformName"]="Android"
desired_capabilities["platformVersion"]="12.0"
desired_capabilities["deviceName"]="3437789507001HM"
desired_capabilities["app"]=r"C:\Users\zjf\Downloads\com.sina.news.apk"
desired_capabilities["newCommandTimeout"]=240
desired_capabilities["unicodeKeyboard"]=True
desired_capabilities["resetKeyboard"]=True

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)

sleep(3)

driver.quit()