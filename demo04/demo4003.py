from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.appiumby import AppiumBy
#启动app
desired_capabilities={}
desired_capabilities['platformName']='Android'
desired_capabilities['platformVersion']='12.0'
desired_capabilities['deviceName']='3437789507001HM'
desired_capabilities['app']=r"C:\Users\zjf\Downloads\com.sina.news.apk"
desired_capabilities['newCommandTimeout']=240
desired_capabilities['appPackage']='com.sina.news'
desired_capabilities['appActivity']='.module.launch.activity.PowerOnScreen'
desired_capabilities['']=''
desired_capabilities['']=''
desired_capabilities['']=''

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)

driver.implicitly_wait(6)
el1 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]")
el1.click()
sleep(5)
TouchAction(driver).press(x=593, y=1722).wait(300).move_to(x=457, y=604).release().perform()

driver.implicitly_wait(6)

el2 = driver.find_element(by=AppiumBy.ID,
                          value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el2.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(593,1722)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(457,604)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(593,1722)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(457,604)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(157,1722)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(593,1722)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(8)
el3 = driver.find_element(by=AppiumBy.XPATH,
                          value="(//android.widget.RelativeLayout[@content-desc=\"ft_1\"])[2]/android.widget.TextView")
el3.click()

driver.implicitly_wait(8)
sleep(1)
el4 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/com.sina.news.ui.view.SinaDrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.TextView[6]")
el4.click()

driver.implicitly_wait(8)
sleep(4)
el5 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/com.sina.news.ui.view.SinaDrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.TextView[7]")
el5.click()

driver.implicitly_wait(8)
el6 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]")
el6.click()
driver.implicitly_wait(5)
el7 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/com.sina.news.ui.view.SinaDrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView")
el7.click()
driver.implicitly_wait(5)
el8 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
el8.click()
driver.implicitly_wait(5)
sleep(1)
el9 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[2]")
el9.click()
driver.implicitly_wait(5)
sleep(1)
el10 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/com.sina.news.ui.view.SinaDrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView")
el10.click()
driver.implicitly_wait(5)
el11 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.TextView[3]")
el11.click()
driver.implicitly_wait(5)
el12 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView")
el12.click()

#等待
sleep(3)
#关闭
driver.quit()