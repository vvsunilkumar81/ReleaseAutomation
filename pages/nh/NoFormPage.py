from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class NoFormPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    gender="field133"
    extendeddict="field2895"
    completebtn="submitButton"
    extendedstr="field2958"

    def completeTask(self,value1,value2,value3):
        extended_custom = self.driver.find_element(By.ID,self.extendeddict)
        extended_custom.click()
        time.sleep(2)
        Select(extended_custom).select_by_visible_text(value1)
        time.sleep(1)
        genderfield = self.driver.find_element(By.ID, self.gender)
        genderfield.click()
        time.sleep(2)
        Select(genderfield).select_by_visible_text(value2)
        time.sleep(1)
        self.sendKeys(value3, self.extendedstr)
        self.elementClick(self.completebtn)
        time.sleep(5)














