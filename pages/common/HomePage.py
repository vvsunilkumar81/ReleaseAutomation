from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    usermenu_link_cssselector = "a[id='swfCoreUserMenuControl']"
    logout_link_cssselector = "a[id='swfCoreUserMenuControl_logout']"
    logout_link_css_newui = "button#logoutBtn"
    mytasks = "h1.ob-h1>label"
    logout = "logoutBtn"
    usermenu_css = "span.user-menu-icon"
    logout_xpath = "//span[contains(text(),'Log Out')]"
    change_filters = "changeFilter"
    newhireName = "newHireName"
    applyfilter = "applyFilterBtn1"
    name_begin_search = "nameBeginsSearch"
    nh_name_css = "div.col-sm-3 a a"
    nh_name_xpath = "//a[@class='newHire']/a"
    nh_task_xpath = "//a[@class='title']/a"
    create_newhire = "createNewHireBtn"

    def get_tasks(self):
        if self.is_visible(self.mytasks, "css"):
            return self.getText(self.mytasks, "css")

    def click_newhire(self, lname=None, fname=None):
        nhlname = lname + "," + " " + fname
        nhname_linktext = lname + " " + fname
        try:
            self.log.info("Click on Newhire filter ")
            self.elementClick(self.change_filters)
            time.sleep(5)
            self.log.info("Enter Newhire name" + nhlname)
            self.sendKeys(lname,self.newhireName)
            self.elementClick(self.name_begin_search)
            self.elementClick(self.applyfilter)
            time.sleep(5)
            nhname_exp = self.driver.find_element(By.PARTIAL_LINK_TEXT, lname)
            print(nhname_exp.get_attribute("text"))
            nhname_exp.click()
            time.sleep(10)
            self.ts.markFinal("Verification of Newhire name", "Pass", "Fetched the required newhire")
        except:
            self.log.info("newhire name not found " + nhname_linktext)

    def logoutfromts(self):
        try:
            self.log.info("Click on User menu ")
            self.elementClick(self.usermenu_css, locatorType="css")
            time.sleep(5)
            self.log.info("Click on Logout menu ")
            self.elementClick(self.logout_xpath, locatorType="xpath")
            time.sleep(5)
            self.log.info("Getting Driver title")
            title = self.getTitle()
            return title
        except:
            self.log.info("Not logout")

    def clicknewhirelink(self):
        self.log.info("Click on newhirename link to navigate to newhire tasks page ")
        self.elementClick(self.nh_name_xpath, locatorType="xpath")

    def clicknewhiretaskname(self, task):
        self.log.info("Click on newhirename link to navigate to newhire tasks page ")
        self.elementClick(self.nh_name_xpath, locatorType="xpath")

    def clickCreateNewhire(self):
        self.log.info("Click on createnewhire button to navigate to Create Newhire page ")
        self.elementClick(self.create_newhire)
        time.sleep(2)

