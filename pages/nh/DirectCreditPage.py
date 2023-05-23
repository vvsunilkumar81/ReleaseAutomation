from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class DirectCreditPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    bankname = "field4158"
    bankaccount="field4160"
    dropdownfield = "field19970"
    dropdownfield2 = "field1810"
    saveAndContinue = "p1_saveAndContinueBtn"
    completebtn = "p3_submitBtn"
    confirmCheck = "signandseal"

    def completeTask(self, value1, value2,value3,value4):
        self.sendKeys(value1, self.bankname)
        time.sleep(5)
        self.sendKeys(value2, self.bankaccount)
        time.sleep(5)

        dropdown = self.driver.find_element(By.ID, self.dropdownfield)
        dropdown.click()
        time.sleep(2)
        Select(dropdown).select_by_visible_text(value3)
        time.sleep(1)
        dropdown2 = self.driver.find_element(By.ID, self.dropdownfield2)
        dropdown2.click()
        time.sleep(2)
        Select(dropdown2).select_by_visible_text(value4)
        time.sleep(1)
        self.elementClick(self.saveAndContinue)
        time.sleep(5)
        self.elementClick(self.confirmCheck)
        time.sleep(5)
        self.elementClick(self.completebtn)
        time.sleep(5)
