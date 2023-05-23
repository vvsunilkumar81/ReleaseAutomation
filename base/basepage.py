"""
Base Page class implementation
 1.It implements methods which are common to all the pages throughout the application
 2.This class needs to be inherited by all the page classes
 3.This should not be used by creating object instances
"""
from utility.datagenerator import DataGenerator
from utility.util import Util
from utility.soaputil import SoapUtil
from utility.restutil import RestUtil
from base.selenium_driver import SeleniumDriver


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
         Constructor of BasePage class returns: None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        # calling Util
        self.util = Util()
        # calling Soap Util methods
        self.soaputil = SoapUtil()
        # calling Rest util methods
        self.restutil = RestUtil()
        self.data=DataGenerator()

        # calling Excel


def verifyPageTitle(self, titleToVerify):
    """
        Verify the page Title
        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
    try:
        actualTitle = self.getTitle()
        return self.util.verifyTextContains(actualTitle, titleToVerify)
    except:
        self.log.error("Failed to get page title")
        return False

