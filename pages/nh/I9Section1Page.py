from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from utility.teststatus import TestStatus


class I9Section1Page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ts = TestStatus(driver)

    continuebutton = "btncontinue"
    firstname = "nhfirstname"
    lastname = "nhlastname"
    middlename = "nhmiddleinitial"
    otherlastname="nhotherlastnames"
    dob="nhdateofbirth"
    ssnavailable="ssnAvailable"
    ssn = "nhssn"
    address = "nhstreetaddr"
    aptno="nhaptmtno"
    city = "nhcity"
    state = "state"
    teleno="nhtelnumber"
    zip = "nhzipcode"
    saveandcontinue="btnsaveandcontinue"
    citizenship="citizenshipStatus"
    checkbox="translatorChecked"
    signanadseal="signandseal"
    success="btnsuccess"

    def completeI9Section1USCitizen(self, fname,lname,mname,othername,ssn,address,aptno,city,teleno):
        self.elementClick(self.checkbox,"name")
        time.sleep(1)
        self.elementClick(self.continuebutton)
        time.sleep(1)
        self.sendKeys(fname,self.firstname)
        self.sendKeys(lname, self.lastname)
        self.sendKeys(mname, self.middlename)
        self.sendKeys(othername, self.otherlastname)
        self.sendKeys("04/30/1981", self.dob)
        time.sleep(1)
        self.elementClick(self.ssnavailable,"name")
        time.sleep(1)

        self.sendKeys(ssn, self.ssn)
        self.sendKeys(address, self.address)
        self.sendKeys(aptno, self.aptno)
        self.sendKeys(city, self.city)

        self.sendKeys(teleno, self.teleno)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.continuebutton)
        time.sleep(1)
        self.elementClick(self.citizenship,"name")
        time.sleep(1)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.saveandcontinue)
        time.sleep(5)
        self.elementClick(self.signanadseal)
        time.sleep(2)
        self.elementClick(self.success)
        time.sleep(5)

