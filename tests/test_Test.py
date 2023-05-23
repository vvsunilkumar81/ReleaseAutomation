import pytest

from pages.common.HomePage import HomePage
from pages.common.LoginPage import TSLoginPage
from pages.hm.AdminPage import AdminPage
from pages.hm.CreateNewHirePage import CreateNewHirePage
from pages.hm.MyTasksPage import MyTasksPage
from pages.hm.OnboardStartPage import OnboardStartPage
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
        admin = AdminPage(self.driver)
        home = HomePage(self.driver)
        time.sleep(5)
        reseturl="https://stagingts.brassring.com/ibp/core/app/redirect/stgTestclient/?uri=kx%3alogin%253aautTuesdayMayxdbg%253arst%253ad34b5cfd-f763-4ac6-804a-411f49d733fd"

        print(reseturl)
        self.driver.get(reseturl)
        admin.createPasswordWithThreeQuestions("QAtest234#", "testone", "testtwo", "testthree")
        time.sleep(5)

