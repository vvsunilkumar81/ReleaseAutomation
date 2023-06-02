from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class DigitalSignature(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    edit_link_xpath="//label[normalize-space()='Edit']/parent::button"
    canvas = "//div[@id='DrawSignCanvas']/div/div/div/canvas[4]"
    submit_button_xpath = "//div[ @class ='full-width'] // button[1]"
    drawsignsubmit="DrawSignSubmitButton"
    saveandcontinue="p2_saveAndContinueBtn"

    def drawsignature(self):

           actions = ActionChains(self.driver)
           canvas = self.driver.find_element(By.XPATH, self.canvas)
           actions.move_to_element(canvas)
           actions.click_and_hold(canvas)
           actions.move_by_offset(40,-10)
           actions.move_by_offset(40,10)
           actions.move_by_offset(40,-10)
           actions.move_by_offset(245,10)
           actions.release().perform()
           time.sleep(5)
           self.elementClick(self.drawsignsubmit)
           time.sleep(5)
           self.elementClick(self.saveandcontinue)

           time.sleep(5)



5

