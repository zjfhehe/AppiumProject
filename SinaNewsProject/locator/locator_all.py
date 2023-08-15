from appium.webdriver.common.appiumby import AppiumBy

authorize_yes_locator=(AppiumBy.XPATH,"//android.widget.Button[1]")
top_article_two_locator=(AppiumBy.XPATH,"(//android.widget.RelativeLayout[@content-desc='ft_1'])[2]")
article_follow_locator=(AppiumBy.XPATH,"//android.widget.TextView[6][@text='关注']")
article_unfollow_locator=(AppiumBy.XPATH,"//android.widget.TextView[@text='已']")
article_unfollow_yes_locator=(AppiumBy.XPATH,"//android.widget.Button[1]")
hotlist_locator=(AppiumBy.XPATH,"//android.widget.RelativeLayout[@content-desc='ct_news_hotlist']")
video_tab_locator=(AppiumBy.XPATH,"//android.widget.LinearLayout/android.widget.TextView[@text='视频']")
video_content_one_locator=(AppiumBy.XPATH,'//android.widget.RelativeLayout[@content-desc="ft_101"][1]')
video_likes_locator=(AppiumBy.XPATH,'//android.widget.LinearLayout[3]/android.widget.ImageView[1]')


