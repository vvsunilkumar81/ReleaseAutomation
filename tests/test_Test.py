import pytest

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
    def test_login_hm(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        self.driver.get(self.appurl)
        time.sleep(5)
        print("title of Login Page" + self.driver.title)
        lp.logintsonboard(self.appurl, "autMondayMayrelo", "QAtest234#")
        time.sleep(10)
        assert "Onboard home | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Landing Page")

    def test_DirectCredit(self):
        nhtasks = NHMyTasksPage(self.driver)
        ds=DigitalSignature(self.driver)
        ci = ConflictInterestPage(self.driver)
        print(self.driver.title)
        nhtasks.clickTask("Conflict of Interest")
        time.sleep(5)
        print(self.driver.title)
        ci.completeTask("Yes")
        time.sleep(5)
        print(self.driver.title)


