from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
import unittest
from SinaNewsProject.base.mybase import DC_base
class Case01(DC_base):
    def setUp(self) -> None:
        self.desired_capabilities={}
        DC_base.setUp(self)
    def test_case(self):

        el1 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.Button[2]")
        el1.click()

        TouchAction(self.driver).press(x=593, y=1722).wait(300).move_to(x=457, y=604).release().perform()

        sleep(3)
        # 授权允许
        el2 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.Button[1]")
        el2.click()

        TouchAction(self.driver).press(x=593, y=1722).wait(300).move_to(x=457, y=604).release().perform()
        TouchAction(self.driver).press(x=593, y=1722).wait(300).move_to(x=457, y=604).release().perform()
        TouchAction(self.driver).press(x=193, y=1722).wait(300).move_to(x=757, y=1722).release().perform()

        sleep(2)
        # 找置顶文章,点击置顶第二条
        el3 = self.driver.find_element(AppiumBy.XPATH,
                                  value="(//android.widget.RelativeLayout[@content-desc='ft_1'])[2]")
        el3.click()

        # 点击关注
        el4 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.TextView[6][@text='关注']")
        # el4=driver.find_element(AppiumBy.XPATH,value="//android.widget.TextView[@text,'关注']")
        el4.click()

        sleep(4)

        # 点击取消关注
        el5 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.TextView[@text='已']")
        el5.click()

        el6 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.Button[1]")
        el6.click()
        sleep(1)
        # 左滑退出
        TouchAction(self.driver).press(x=193, y=1722).wait(300).move_to(x=757, y=1722).release().perform()

        # 点击热榜
        el7 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.RelativeLayout[@content-desc='ct_news_hotlist']")
        el7.click()

        # 点击视频子导航
        el8 = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.LinearLayout/android.widget.TextView[@text='视频']")
        el8.click()

        # 点击第一条
        el9 = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.RelativeLayout[@content-desc="ft_101"][1]')
        el9.click()

        sleep(5)
        # 点击赞图标
        '''
        el10=driver.find_element(AppiumBy.XPATH,
                                 value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.ImageView[1]')
        el10.click()
    
        '''

        el10 = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.LinearLayout[3]/android.widget.ImageView[1]')
        el10.click()

        sleep(3)
    def tearDown(self) -> None:
        DC_base.tearDown(self)

if __name__=="__main__":
    unittest.main()