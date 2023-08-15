from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_capabilities={}
desired_capabilities['platformName']='Android'
desired_capabilities['platformVersion']='12.0'
desired_capabilities['deviceName']='3437789507001HM'
desired_capabilities['appPackage']='com.jianwan.tgdzzwxzc.yy3733'
#desired_capabilities['appActivity']='com.quicksdk.apiadapter.game3373.ChannelSplashActivity'
desired_capabilities['appActivity']='org.cocos2dx.javascript.SplashActivity'
desired_capabilities['newCommandTimeout']=240
#desired_capabilities['automationName']='uiautomator2'
desired_capabilities['']=''
desired_capabilities['']=''
desired_capabilities['']=''
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)

driver.wait_activity("com.quicksdk.apiadapter.game3373.ChannelSplashActivity",10,1)
driver.implicitly_wait(10)
el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]")
el1.click()
driver.implicitly_wait(10)
el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.EditText")
el3.send_keys("13811683900")
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText")
el4.send_keys("12345678")
el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.Button")
el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
el6.click()

driver.implicitly_wait(15)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(857,708)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
sleep(1)


sleep(5)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(106,2031)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

sleep(1)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(563,1949)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(15)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(559,1677)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(566,1050)
actions.w3c_actions.pointer_action.release()
actions.perform()

#选择服务器
driver.implicitly_wait(15)
sleep(3)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(287,1671)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(15)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(529,1741)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

sleep(4)

#点击加速
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1,940)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(276,1149)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(885,1291)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(974,634)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

#点击叉子
driver.implicitly_wait(15)
sleep(5)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(974,634)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

for i in range(200):

    #点击副本
    TouchAction(driver).press(x=433,y=2104).release().perform()
    sleep(2)
    #点击最上方的副本
    TouchAction(driver).press(x=580,y=800).release().perform()
    sleep(1)
    #点击蓝色挑战
    TouchAction(driver).press(x=554,y=1060).release().perform()
    sleep(1)
    for j in range(41):
        #点击困难战50次
        TouchAction(driver).press(x=724,y=1630).release().perform()
        sleep(3)
        #点击关闭
        TouchAction(driver).press(x=1000, y=800).release().perform()
        sleep(1)
    # 点击关闭挑战页面
    TouchAction(driver).press(x=1000, y=800).release().perform()
    sleep(1)
    #点击装备底tab
    TouchAction(driver).press(x=624, y=2140).release().perform()
    sleep(1)
    #点击出售
    TouchAction(driver).press(x=835, y=564).release().perform()
    sleep(2)
    #点击可见全选
    TouchAction(driver).press(x=556, y=1984).release().perform()
    sleep(7)
    #点击出售
    TouchAction(driver).press(x=890, y=1983).release().perform()
    sleep(3)
    #点击卡牌底tab
    TouchAction(driver).press(x=293, y=2125).release().perform()
    sleep(1)
    #点击卡牌出售
    TouchAction(driver).press(x=818, y=1909).release().perform()
    sleep(4)
    for k in range(3):
        #点击可见全选
        TouchAction(driver).press(x=567, y=1984).release().perform()
        sleep(9)
        # 点击出售
        TouchAction(driver).press(x=892, y=1984).release().perform()
        sleep(5)
    #点击主城
    TouchAction(driver).press(x=112, y=2100).release().perform()
    # 点击炼化
    TouchAction(driver).press(x=862, y=1405).release().perform()
    for m in range(3):
        # 点击选择装备
        TouchAction(driver).press(x=568, y=1948).release().perform()
        # 点击炼化
        TouchAction(driver).press(x=556, y=1765).release().perform()
        sleep(3)
        # 点击关闭
        TouchAction(driver).press(x=974, y=1071).release().perform()
        sleep(1)

driver.quit()