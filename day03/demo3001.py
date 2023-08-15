from appium import webdriver
from time import sleep
#启动应用程序
desired_capabilities={}
desired_capabilities["automationName"]="UiAutomator2"
desired_capabilities["platformName"]="Android"
desired_capabilities["platformVersion"]="12.0"
desired_capabilities["deviceName"]="Android Emulator"
desired_capabilities["app"]=r"C:\Users\zjf\Downloads\com.sina.news.apk"
desired_capabilities["newCommandTimeOut"]=120
desired_capabilities["unicodeKeyboard"]=True
desired_capabilities["resetKeyboard"]=True
desired_capabilities[""]=""
desired_capabilities[""]=""
desired_capabilities[""]=""
desired_capabilities[""]=""
desired_capabilities[""]=""
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)
#关闭app
sleep(2)
driver.quit()



