from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

    saveandcontinue = "saveAndContinueBtn"
    firstname = "firstName"
    lastname = "lastName"
    middlename = "middleInitial"
    ssn = "socialSecurityNumber"
    address = "address"
    city = "city"
    state = "state"
    zip = "zipCode"
    claimexempt="claimExemptFromWithHolding"
    checkbox="//input[@type='checkbox']"
    nrastatus="nonResidentAlienStatus"
    maritalstatus="maritalStatus"
    confirmCheck="confirmCheck"
    success="successBtn"

    def completeTaskWithClaimExemptFromWithHolding(self, fname,lname,mname,ssn,address,city,state,zip,maritalstatus):
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.sendKeys(fname,self.firstname)
        self.sendKeys(lname, self.lastname)
        self.sendKeys(mname, self.middlename)
        self.sendKeys(ssn, self.ssn)
        self.sendKeys(address, self.address)
        self.sendKeys(city, self.city)
        dropdown = self.driver.find_element(By.ID, self.state)
        dropdown.click()
        time.sleep(2)
        Select(dropdown).select_by_visible_text(state)
        time.sleep(1)
        self.sendKeys(zip, self.zip)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.claimexempt,"name")
        time.sleep(1)
        self.elementClick(self.checkbox, "xpath")
        time.sleep(1)

        dropdown = self.driver.find_element(By.ID, self.maritalstatus)
        dropdown.click()
        time.sleep(2)
        Select(dropdown).select_by_visible_text(maritalstatus)
        time.sleep(1)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.confirmCheck)
        time.sleep(2)
        self.elementClick(self.success)
        time.sleep(5)

