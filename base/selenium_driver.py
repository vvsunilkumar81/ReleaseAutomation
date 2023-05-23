from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utility.custom_logger as cl
import logging
import time
import os
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.support.select import Select

"""
Selenium Driver 
 1.Optimizing the Selenium web driver methods 
 2.This class needs to be inherited by all the page classes
 3.14 reusable methods written and those are generic across the pages
  1.screenshot 2.gettitle 3.getByType 4.getElement 5.getElementList6.elementClick 7.sendKeys 
  8.clearField9.getText10.isElementPresent11.isElementDisplayed12.elementPresenceCheck13.waitForElement14.webScroll
"""


class SeleniumDriver(AbstractEventListener):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 20

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def is_visible(self, locator="", locatorType="id", element=None):

        try:
            if locator:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator, locatorType))
                return bool(element)
            else:
                self.log.info("Element not present with locator: " + locator +" locatorType: " + locatorType)
            return False
        except:
                print("Element not found")
        return False

    def screenShot(self, resultMessage):

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred while taking screenshot")

    def getTitle(self):
        return self.driver.title


    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
        except:
            self.log.info("Unable to display element " + locator + " and  locatorType: " + locatorType)
        return element

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)

        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                time.sleep(2)
                element.click()
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)

        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)

    def selectValueFromDropdown(self, data, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty

                element = self.getElement(locator, locatorType)
                element.click()
                time.sleep(5)
                Select (element.select_by_visible_text(data))
                element.click()

        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)

    def clearField(self, locator="", locatorType="id"):

        element = self.getElement(locator, locatorType)
        element.clear()



    def getText(self, locator="", locatorType="id", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                text = element.text
            if len(text) == 0:
                text = element.get_attribute("value")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")

        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element:
                isDisplayed = element.is_displayed()

            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType):

        try:
            elementList = self.driver.find_elements(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(locatorType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(locatorType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def dateSelection(self, value, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)

            action = ActionChains(self.driver)
            action.click(on_element=element)
            action.send_keys_to_element(element, value)
            action.perform()
            self.log.info("Date selected " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def selectvaluefromdropdown(self, value, locator="", locatorType="id"):

        try:
            if locator:  # This means if locator is not empty
                actions = ActionChains(self.driver)
                element = self.getElement(locator, locatorType)
                element.click()
                time.sleep(1)
                resultSet = self.driver.find_element_by_xpath("//div[@id='menu-']/div/ul")
                options = resultSet.find_elements_by_tag_name("li")
                for option in options:
                    if option.text == value:
                        option.click()
                        time.sleep(1)
                        break

        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def selectvaluefromlargedropdown(self, value, locator="", locatorType="id", element=None):

        try:
            if locator:
                s = self.driver.find_element_by_xpath(locator)
                self.driver.execute_script("arguments[0].click();", s)
                time.sleep(1)
                self.driver.execute_script("document.querySelector('.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded').scrollTop=200");
                time.sleep(3)
                self.driver.execute_script("document.querySelector('.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded').scrollBy(0,2500)");
                time.sleep(3)
                self.driver.execute_script("document.querySelector('.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded').scrollBy(0,2500)");
                time.sleep(3)
                self.driver.execute_script("document.querySelector('.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded').scrollBy(0,2500)");
                time.sleep(3)
                resultSet = self.driver.find_element_by_xpath("//div[@id='menu-']/div/ul")
                options = resultSet.find_elements_by_tag_name("li")
                for option in options:
                    if option.text == value:
                        option.click()
                        time.sleep(1)
                        break
                        element.click()
                    else:
                        self.log.info("value is not selected: " + value)

        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def selectvaluefrommultilist(self, value, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                element.click()
                time.sleep(1)
                resultSet = self.driver.find_element_by_xpath("//div[@id='menu-']/div/ul")
                options = resultSet.find_elements_by_tag_name("li")
                for option in options:
                    if option.text == value:
                        option.click()
                        time.sleep(1)
                        break
                        element.click()
                    else:
                        self.log.info("value is not selected: " + value)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def webScroll(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
