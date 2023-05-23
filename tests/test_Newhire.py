import pytest

from pages.common.HomePage import HomePage
from pages.common.LoginPage import TSLoginPage
from pages.hm.AdminPage import AdminPage
from pages.hm.CreateNewHirePage import CreateNewHirePage
from pages.hm.MyTasksPage import MyTasksPage
from pages.hm.OnboardStartPage import OnboardStartPage
from pages.nh.DigitalSignature import DigitalSignature
from pages.nh.GenericPage import GenericPage
from pages.nh.NewHireDashboard import NewHireDashboard
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
        lp.logintsonboard(self.appurl, self.hm, "QAtest1@")
        time.sleep(10)
        assert "Onboard home | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Landing Page")

    def test_CreateNewhire(self):
        homepage = HomePage(self.driver)
        createnhpage = CreateNewHirePage(self.driver)
        ts = TestStatus(self.driver)
        print("title of home page" + self.driver.title)
        homepage.clickCreateNewhire()
        print("title of Create Newhire" + self.driver.title)
        assert "HM Create NewHire | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        time.sleep(10)
        createnhpage.completecreatenewhire(self.testdata_job[2], "English(US)", self.testdata_job[0],
                                           self.testdata_job[1], self.testdata_job[3], "8648378",
                                           "12345", "United States", "Maryland")

        assert homepage.isElementPresent(homepage.mytasks, "css") == True
        ts.mark("Pass", "User is being navigated to Home Page")
        homepage.click_newhire(self.testdata_job[1], self.testdata_job[0])
        ts.mark("Pass", "User is navigated to Onboard Tasks")

    def test_CompleteObStartTask(self):
        ts = TestStatus(self.driver)
        myTasks = MyTasksPage(self.driver)
        obStart = OnboardStartPage(self.driver)
        ts.mark("Pass", "User is navigated to Onboard Task page")
        myTasks.clickTask("Onboard Start")
        time.sleep(10)
        obStart.completeOBStartTask()

    def test_Admin(self):
        ts = TestStatus(self.driver)
        myTasks = MyTasksPage(self.driver)
        admin = AdminPage(self.driver)
        myTasks.clickAdmin()
        ts.mark("Pass", "User is navigated to Admin App")
        admin.clickSearchMailHistory()
        time.sleep(10)

    def test_resetPassword(self):
        admin = AdminPage(self.driver)
        home = HomePage(self.driver)
        reseturl = admin.searchUser(self.testdata_job[2])
        time.sleep(10)
        home.logoutfromts()
        time.sleep(10)
        print(reseturl)
        self.driver.get(reseturl)
        admin.createPasswordWithThreeQuestions("QAtest234#", "testone", "testtwo", "testthree")
        time.sleep(5)
