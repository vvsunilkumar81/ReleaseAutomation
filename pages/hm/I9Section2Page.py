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

    continuebutton = "continueBtn"
    docType = "documentType"
    docTypeATitle = "docTypeA0Title"
    docANum = "docTypeA0DocNum"
    docTypeAExpDate = "docTypeA0DocExpDate"
    empStartdate = "empStartDate"
    saveandContinue = "p2_saveAndContinueBtn"
    ipEmpRep = "i9EmprRepTitle"
    saveandContinue_1 = "s2_saveAndContinueBtn"
    saveandContinue_2 = "p2_saveAndContinueBtn"
    signanadseal = "signandseal"

    def completeI9Section2USCitizen(self, docANum,docExpDate,empStartDate,sec2reptitle):
        self.elementClick(self.continuebutton)
        time.sleep(1)
        self.driver.find_element_by_name("documentType").click()
        self.driver.find_element_by_id("docTypeA0Title").click()
        self.driver.find_element_by_id("docTypeA0DocNum").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Document Number'])[1]/following::*[name()='svg'][1]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Document Number #1 List A'])[1]/following::*[name()='svg'][1]").click()
        self.driver.find_element_by_id("docTypeA0DocNum").click()
        self.driver.find_element_by_id("docTypeA0DocNum").clear()
        self.driver.find_element_by_id("docTypeA0DocNum").send_keys(docANum)
        self.driver.find_element_by_css_selector(
            "button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw > svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.css-vubbuv > path").click()
        self.driver.find_element_by_id("docTypeA0DocExpDate").click()
        self.driver.find_element_by_id("docTypeA0DocExpDate").click()
        self.driver.find_element_by_id("docTypeA0DocExpDate").clear()
        self.driver.find_element_by_id("docTypeA0DocExpDate").send_keys("01/01/2024")
        self.driver.find_element_by_id("empStartDate").click()
        self.driver.find_element_by_id("empStartDate").clear()
        self.driver.find_element_by_id("empStartDate").send_keys("05/06/2023")
        self.driver.find_element_by_id("p2_saveAndContinueBtn").click()
        self.driver.find_element_by_id("i9EmprRepTitle").click()
        self.driver.find_element_by_id("i9EmprRepTitle").clear()
        self.driver.find_element_by_id("i9EmprRepTitle").send_keys("QA")
        self.driver.find_element_by_id("s2_saveAndContinueBtn").click()
        self.driver.find_element_by_id("p2_saveAndContinueBtn").click()
        self.driver.find_element_by_id("signandseal").click()
        self.driver.find_element_by_id("p2_saveAndContinueBtn").click()
