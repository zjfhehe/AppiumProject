from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput

class Actions():
    def touch_xy(self,driver,x,y):
        touch_xy=ActionChains(driver)
        touch_xy.w3c_actions=ActionBuilder(driver,mouse=PointerInput(interaction.POINTER_TOUCH,"touch"))
        touch_xy.w3c_actions.pointer_action.move_to(x,y)
        touch_xy.w3c_actions.pointer_action.pointer_down()
        touch_xy.w3c_actions.pointer_action.pause(0.1)
        touch_xy.w3c_actions.pointer_action.release()
        touch_xy.perform()

    def touch_element(self,driver,element):
        touch_element = ActionChains(driver)
        touch_element.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        touch_element.w3c_actions.pointer_action.move_to(element)
        touch_element.w3c_actions.pointer_action.pointer_down()
        touch_element.w3c_actions.pointer_action.pause(0.1)
        touch_element.w3c_actions.pointer_action.release()
        touch_element.perform()

    def move_xy_to_xy(self,driver,x1,y1,x2,y2):
        move_xy_to_xy = ActionChains(driver)
        move_xy_to_xy.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        move_xy_to_xy.w3c_actions.pointer_action.move_to(x1,y1)
        move_xy_to_xy.w3c_actions.pointer_action.pointer_down()
        move_xy_to_xy.w3c_actions.pointer_action.pause(0.1)
        move_xy_to_xy.w3c_actions.pointer_action.move_to(x2, y2)
        move_xy_to_xy.w3c_actions.pointer_action.release()
        move_xy_to_xy.perform()

    def move_xy_to_element(self,driver,x,y,element):
        move_xy_to_element = ActionChains(driver)
        move_xy_to_element.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        move_xy_to_element.w3c_actions.pointer_action.move_to(x, y)
        move_xy_to_element.w3c_actions.pointer_action.pointer_down()
        move_xy_to_element.w3c_actions.pointer_action.pause(0.1)
        move_xy_to_element.w3c_actions.pointer_action.move_to(element)
        move_xy_to_element.w3c_actions.pointer_action.release()
        move_xy_to_element.perform()

    def move_element_to_element(self,driver,ele1,ele2):
        move_element_to_element = ActionChains(driver)
        move_element_to_element.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        move_element_to_element.w3c_actions.pointer_action.move_to(ele1)
        move_element_to_element.w3c_actions.pointer_action.pointer_down()
        move_element_to_element.w3c_actions.pointer_action.pause(0.1)
        move_element_to_element.w3c_actions.pointer_action.move_to(ele2)
        move_element_to_element.w3c_actions.pointer_action.release()
        move_element_to_element.perform()

    def move_element_to_xy(self,driver,ele,x,y):
        move_element_to_xy = ActionChains(driver)
        move_element_to_xy.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        move_element_to_xy.w3c_actions.pointer_action.move_to(ele)
        move_element_to_xy.w3c_actions.pointer_action.pointer_down()
        move_element_to_xy.w3c_actions.pointer_action.pause(0.1)
        move_element_to_xy.w3c_actions.pointer_action.move_to(x,y)
        move_element_to_xy.w3c_actions.pointer_action.release()
        move_element_to_xy.perform()