from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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
    canvas_xpath = "//body//div//canvas[1]"
    submit_button_xpath = "//div[ @class ='full-width'] // button[1]"

    def drawsignature(self):

        try:
            self.elementClick(self.edit_link_xpath,locatorType="xpath")
            actionChains = ActionChains(self.driver)
            element=self.driver.find_element(By.XPATH,"//button/label")
            actionChains.move_to_element(element).click().perform()
            actions = ActionChains(self.driver)
            maxwidth = int(self.canvas_xpath.attr("width").toInteger())
            actions.moveToElement(self.canvas_xpath.firstElement(), 100, 40)
            actions.clickAndHold(self.canvas_xpath.firstElement())
            actions.moveByOffset(40, -10)
            actions.moveByOffset(40, 10)
            actions.moveByOffset(40, -10)
            actions.moveByOffset(maxwidth - 10, 10)
            actions.release(on_element=self.canvas_xpath.firstElement())
            actions.perform()
            time.sleep(5)
            self.elementClick(self.submit_button_xpath, locatorType="xpath")

        except:
            self.log.info("Not logout")
