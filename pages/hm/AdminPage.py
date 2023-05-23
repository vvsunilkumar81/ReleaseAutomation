from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utility.custom_logger as cl
import logging
import time,re

from base.basepage import BasePage


class AdminPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    sidenav = "span.nav-side-control"
    applauncher = "span.app-launcher-icon"
    adminapp = "#app-item-TSADMIN > div.app-circle"
    searchemailHistory = "//div[contains(text(),'Search Email History')]"
    filterbutton = "filterButton"
    toField = "to"
    applybutton = "applyButton"
    sent="//button[contains(text(),'SENT')]"
    emailbody="//div[@id='emailDetails']/div[2]/div/p[2]"
    continueButton="//button[contains(text(),'Continue')]"
    emailclosebutton="#customized-dialog-title > button > svg"
    secretqn1="ChlgQId1"
    secretans1="ChlgAnswer1"
    secretqn2= "ChlgQId2"
    secretans2 = "ChlgAnswer2"
    secretqn3 = "ChlgQId3"
    secretans3 = "ChlgAnswer3"


    continueBtn="// button[contains(name(), 'continueBtn')]"



    def clickSearchMailHistory(self):
        self.log.info("click side naviation bar")
        self.elementClick(self.sidenav, "css")
        time.sleep(5)
        self.elementClick(self.searchemailHistory, "xpath")
        time.sleep(5)

    def searchUser(self, username):
        self.log.info("click on Filter")
        self.elementClick(self.filterbutton)
        time.sleep(5)
        self.sendKeys(username, self.toField)
        time.sleep(5)
        self.elementClick(self.applybutton)
        time.sleep(5)
        self.elementClick(self.sent,"xpath")
        time.sleep(5)
        url=self.getText(self.emailbody,"xpath")
        test=url.split('\n')
        reseturl=test[2]
        print(type(reseturl))
        self.elementClick(self.emailclosebutton,"css")
        time.sleep(5)
        return reseturl

    def createPasswordWithThreeQuestions(self,password,ans1,ans2,ans3):

        newpwd=self.driver.find_element(By.NAME,"newPassword")
        newpwd.click()
        newpwd.send_keys(password)
        confirmpwd=self.driver.find_element(By.NAME,"confirmPassword")
        confirmpwd.click()
        confirmpwd.send_keys(password)
        continueButton=self.driver.find_element(By.NAME, "continueButton")
        continueButton.click()
        time.sleep(5)
        secretqn1= self.driver.find_element(By.ID,self.secretqn1)
        secretqn1.click()
        time.sleep(5)
        Select(secretqn1).select_by_index(1)
        time.sleep(1)
        self.driver.find_element(By.ID,self.secretans1).click()
        self.driver.find_element(By.ID,self.secretans1).clear()
        self.driver.find_element(By.ID,self.secretans1).send_keys(ans1)
        secretqn2 = self.driver.find_element(By.ID, self.secretqn2)
        secretqn2.click()
        time.sleep(5)
        Select(secretqn2).select_by_index(1)
        time.sleep(5)
        self.driver.find_element(By.ID, self.secretans2).click()
        self.driver.find_element(By.ID, self.secretans2).clear()
        self.driver.find_element(By.ID, self.secretans2).send_keys(ans2)
        secretqn3 = self.driver.find_element(By.ID, self.secretqn3)
        secretqn3.click()
        time.sleep(5)
        Select(secretqn3).select_by_index(1)
        time.sleep(1)
        self.driver.find_element(By.ID, self.secretans3).click()
        self.driver.find_element(By.ID, self.secretans3).clear()
        self.driver.find_element(By.ID, self.secretans3).send_keys(ans3)
        self.elementClick(By.XPATH,self.continueButton)
        time.sleep(5)



