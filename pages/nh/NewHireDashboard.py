from selenium import webdriver
from selenium.webdriver.common.by import By

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class NewHireDashboard(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    noForm_task_xpath="//a[contains(text(), 'No Form')]"
    gen_task_xpath="//a[contains(text(),'Confidentiality Agreement')]"
    dd_task_xpath="//a[contains(text(),'Direct Deposit Form')]"








