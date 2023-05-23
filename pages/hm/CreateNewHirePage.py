from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from selenium.webdriver.support.select import Select
from pages.common.HomePage import HomePage


class CreateNewHirePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home=HomePage(driver)
    username = "userName"
    hireLocale = "hireLocale"
    firstname = "firstName"
    lastname = "lastName"
    emailid = "primaryEmailAddress"
    startdate = "empStartDate"
    reqno = "RequisitionNumber"
    country = "field131"
    state = "field130"
    ssn_css = "#field176"
    zip = "field21"
    saveprofile_id = "profileSaveButton"


    def completecreatenewhire(self, nhusername, nhlocal, nhfname, nhlname, nhemail,reqnumber, zip, nh_country,
                              nh_state):
        self.sendKeys(nhusername, self.username)
        time.sleep(2)
        nhlocale=self.driver.find_element(By.ID,self.hireLocale)
        nhlocale.click()
        time.sleep(2)
        Select(nhlocale).select_by_visible_text(nhlocal)
        time.sleep(1)
        self.sendKeys(nhfname, self.firstname)
        time.sleep(1)
        self.sendKeys(nhlname, self.lastname)
        time.sleep(1)
        self.sendKeys(nhemail, self.emailid)
        time.sleep(1)
        self.sendKeys("04/30/2023",self.startdate)
        time.sleep(1)
        reqNumber=self.driver.find_element(By.NAME,self.reqno)
        reqNumber.click()
        time.sleep(1)
        self.sendKeys(reqnumber, self.reqno,"name")
        time.sleep(1)
        nhCountry = self.driver.find_element(By.ID,self.country)
        nhCountry.click()
        time.sleep(2)
        Select(nhCountry).select_by_visible_text(nh_country)
        time.sleep(1)
        nhState = self.driver.find_element(By.ID,self.state)
        nhState.click()
        time.sleep(2)
        Select(nhState).select_by_visible_text(nh_state)
        time.sleep(1)
        self.sendKeys(zip, self.zip)
        self.elementClick(self.saveprofile_id)
        time.sleep(20)



