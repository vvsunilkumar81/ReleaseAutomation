from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class I9Section2Page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    continueBtn = "continueBtn"
    docTypeA = "input[type='radio'][value='A']"
    docTypeAdropdown = "docTypeA0Title"
    docANum = "docTypeA0DocNum"
    docTypeAExpDate = "docTypeA0DocExpDate"
    empStartdate = "empStartDate"
    saveandContinue = "p2_saveAndContinueBtn"
    i9EmpRep = "i9EmprRepTitle"
    saveandContinue_1 = "s2_saveAndContinueBtn"
    saveandContinue_2 = "p2_saveAndContinueBtn"
    signanadseal = "signandseal"

    def completeI9Section2USCitizen(self,docAName, docANum,docExpDate,empStartDate):
        self.elementClick(self.continueBtn)
        time.sleep(5)
        self.elementClick(self.docTypeA,"css")
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, self.docTypeAdropdown)
        dropdown.click()
        time.sleep(2)
        Select(dropdown).select_by_visible_text(docAName)
        time.sleep(2)
        self.sendKeys(docANum,self.docANum)
        time.sleep(5)
        self.elementClick(self.docTypeAExpDate)
        time.sleep(1)
        self.sendKeys(docExpDate,self.docTypeAExpDate)
        time.sleep(2)

        self.elementClick(self.empStartdate)
        time.sleep(1)
        self.sendKeys(empStartDate, self.empStartdate)
        time.sleep(2)
        self.elementClick(self.saveandContinue)
        time.sleep(1)
        self.sendKeys("QA Manager", self.i9EmpRep)
        time.sleep(1)
        self.elementClick(self.saveandContinue_1)
        time.sleep(5)
        self.elementClick(self.saveandContinue_2)
        time.sleep(5)
        self.elementClick(self.signanadseal)
        time.sleep(5)
        self.elementClick(self.saveandContinue_2)
        time.sleep(5)












