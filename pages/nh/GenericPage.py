from selenium import webdriver
from selenium.webdriver.common.by import By

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from pages.nh.DigitalSignature import DigitalSignature
from utility.teststatus import TestStatus


class GenericPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)
        self.dg = DigitalSignature(driver)

    saveandContinue_button_css = "#p1_saveAndContinueBtn"
    relocation_date_css = "# field115"
    dd_task_xpath = "//a[contains(text(),'Direct Deposit Form')]"

    def saveandContinue(self):
        try:
            self.elementClick(self.saveandContinue_button_css, locatorType="css")
            time.sleep(2)
            self.log.info("Navigating to Digital Signature page")
            self.log.info("Page title is" + "-" + self.driver.title)
            return self.dg
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
