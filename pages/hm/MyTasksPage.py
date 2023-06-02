from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utility.custom_logger as cl
import logging
import time

from base.basepage import BasePage


class MyTasksPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    nh_task_xpath = "//a[@class='title']/a"
    applauncher="span.app-launcher-icon"
    adminapp="#app-item-TSADMIN > div.app-circle"

    def click_newhiretask(self, task_name):
        self.log.info("Get the newhire task name")
        taskname = self.getText(locator=self.nh_task_xpath, locatorType='xpath')
        if (taskname == task_name):
            self.elementClick(self.nh_task_xpath, locatorType="xpath")
        else:
            self.log.info("task is not found")

    def clickTask(self, taskname):
        self.log.info("User now click on task"+" "+taskname)
        task_name = self.driver.find_element(By.PARTIAL_LINK_TEXT, taskname)
        task_name.click()
        time.sleep(10)

    def clickAdmin(self):
        self.log.info("click app launcher")
        self.elementClick(self.applauncher,"css")
        time.sleep(5)
        self.elementClick(self.adminapp,"css")
        time.sleep(5)

