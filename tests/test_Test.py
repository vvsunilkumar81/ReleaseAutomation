import pytest

from pages.common.HomePage import HomePage
from pages.common.LoginPage import TSLoginPage
from pages.hm.AdminPage import AdminPage
from pages.hm.CreateNewHirePage import CreateNewHirePage
from pages.hm.I9Section2Page import I9Section2Page
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
class TestSmoke():
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
    test = DataGenerator()
    testName = utils.whoami() + test.getCurrTime()


    @pytest.mark.nh
    def test_Relogin_hmandSearchNewhire(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        homepage = HomePage(self.driver)
        self.driver.get(self.appurl)
        time.sleep(5)
        print("title of Login Page" + self.driver.title)
        lp.logintsonboard(self.appurl, self.hm, "QAtest1@")
        time.sleep(5)
        assert "Onboard home | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Landing Page")
        homepage.click_newhire("AutLastWednesdayMayertt", "AutFirstWednesdayMayertt")

    def test_CompleteSection2(self):
        ts = TestStatus(self.driver)
        myTasks = MyTasksPage(self.driver)
        i9sec2 = I9Section2Page(self.driver)
        ts.mark("Pass", "User is navigated to Onboard Task page")
        myTasks.clickTask("I-9 Section 2")
        time.sleep(5)
        i9sec2.completeI9Section2USCitizen("U.S. Passport","1234567", "01/01/2025", "06/02/2023")
        myTasks.clickTask("E-Verify")
        time.sleep(5)
