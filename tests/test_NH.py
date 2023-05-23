import pytest
from selenium.webdriver import ActionChains

from pages.common.HomePage import HomePage
from pages.common.LoginPage import TSLoginPage
from pages.hm.AdminPage import AdminPage
from pages.hm.CreateNewHirePage import CreateNewHirePage
from pages.hm.MyTasksPage import MyTasksPage
from pages.hm.OnboardStartPage import OnboardStartPage
from pages.nh.ConflictInterestPage import ConflictInterestPage
from pages.nh.DigitalSignature import DigitalSignature
from pages.nh.DirectCreditPage import DirectCreditPage
from pages.nh.GenericPage import GenericPage
from pages.nh.NHMyTasksPage import NHMyTasksPage
from pages.nh.NewHireDashboard import NewHireDashboard
from pages.nh.NoFormPage import NoFormPage
from resources import tsconfig as utils
import configparser
import time

from utility.datagenerator import DataGenerator
from utility.teststatus import TestStatus


@pytest.mark.usefixtures("test_setup")
class TestNH():
    # Static  properties
    config = configparser.ConfigParser()
    config.read(utils.configfilepath)
    state = 'Alabama'
    hm = config.get('stage', 'hmusername')
    password = config.get('stage', 'hmpassword')
    rec = config.get('stage', 'recusername')
    clientname = config.get('stage', 'client_name')
    nhpassword = config.get('stage', 'nh_password')
    appurl = config.get('stage', 'client_URL')

    @pytest.mark.nh
    def test_login_nh(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        self.driver.get(self.appurl)
        time.sleep(5)
        print("title of Login Page" + self.driver.title)
        lp.logintsonboard(self.appurl, "autTuesdayMaygpmu", "QAtest234#")
        time.sleep(10)
        print(self.driver.title)
        nhtasks = NHMyTasksPage(self.driver)
        CITask = ConflictInterestPage(self.driver)
        print(self.driver.title)
        nhtasks.clickTask("Conflict of Interest")
        time.sleep(5)
        print(self.driver.title)
        CITask.completeTask("No")
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("//[@id='DrawSignCanvas']/div[1]/div/div/canvas[4]")

        # click the item
        action.move_to_element(element)
        action.clickAndHold()
        action.moveByOffset(40, -10)
        action.moveByOffset(40, 10)
        action.moveByOffset(40, -10)
        action.moveByOffset(100, - 10, 10)
        action.release()
        action.build()
        action.perform()


