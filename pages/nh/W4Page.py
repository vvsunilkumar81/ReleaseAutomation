from selenium import webdriver
from selenium.webdriver.common.by import By

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class W4Page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    gender_select_id="field133"
    submit_button_css="button[label='Submit']"
    relocation_date_css=""#field115"
    dd_task_xpath="//a[contains(text(),'Direct Deposit Form')]"








