import string, requests
import random
import xml.dom.minidom as md
from selenium.webdriver.common.by import By
import utility.custom_logger as cl
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.basepage import BasePage

import utility.teststatus as TS
from pages.common.HomePage import HomePage


class TSLoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    username = "userName"
    password = "password"
    Login= "loginBtn"

    def enterUserName(self, username):
        self.sendKeys(username, self.username)

    def enterPassword(self, password):
        self.sendKeys(password, self.password)

    def clickLoginButton(self):
        self.elementClick(self.Login)

    def login(self, username="", password=""):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator=self.home.newhire_name_css, locatorType="css")
        return result

    def verifyLoginFailed(self):
        result = self.getText(locator=self.error_mgs_xpath,locatorType="xpath")
        return result

    def getTitle(self):
        return self.driver.title()

    def logintsonboard(self, url=None, username=None, password=None):
        try:
            self.login(username, password)
            time.sleep(2)
            self.log.info("Navigating to TS Homepage")
            self.log.info("Page title is" + "-" + self.driver.title)
            return self.home
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)