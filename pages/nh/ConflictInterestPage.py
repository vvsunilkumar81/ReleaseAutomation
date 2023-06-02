from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from pages.nh.DigitalSignature import DigitalSignature
from utility.teststatus import TestStatus


class ConflictInterestPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)


    dropdownfield = "field174"
    saveAndContinue = "p1_saveAndContinueBtn"
    completebtn = "p3_submitBtn"
    confirmCheck = "signandseal"

    def completeTask(self, value1):
        ds = DigitalSignature(self.driver)
        dropdown = self.driver.find_element(By.ID, self.dropdownfield)
        dropdown.click()
        time.sleep(2)
        Select(dropdown).select_by_visible_text(value1)
        time.sleep(1)
        self.elementClick(self.saveAndContinue)
        time.sleep(5)
        ds.drawsignature()
        time.sleep(5)
        self.elementClick(self.confirmCheck)
        time.sleep(5)
        self.elementClick(self.completebtn)
        time.sleep(5)

