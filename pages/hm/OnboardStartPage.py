import utility.custom_logger as cl
import logging
import time

from base.basepage import BasePage
from pages.common.HomePage import HomePage


class OnboardStartPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.home = HomePage(driver)

    date_completed_xpath = "//div[@class='form-Input'][0]/div/input"
    text_field_css = "input#field205"
    due_date_xpath = "//div[@class='form-Input'][1]/div/input"
    submit = "submitBtn"

    def completeOBStartTask(self):

         self.elementClick(self.submit)
         time.sleep(5)

