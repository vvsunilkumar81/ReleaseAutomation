import pytest

from pages.common.HomePage import HomePage
from pages.common.LoginPage import TSLoginPage
from resources import tsconfig as utils
import configparser
import time

from utility.datagenerator import DataGenerator
from utility.teststatus import TestStatus


@pytest.mark.usefixtures("test_setup")
class TestIQA():
    # Static  properties
    config = configparser.ConfigParser()
    config.read(utils.configfilepath)
    state = 'Alabama'
    jobworkflow = config.get('iqa', 'bws_simple_wokflow')
    hm = config.get('iqa', 'hmusername')
    admin = config.get('iqa', 'admin_user')
    adminpassword = config.get('iqa', 'admin_password')
    rec = config.get('iqa', 'recusername')
    clientname = config.get('iqa', 'client_name')
    hmpassword = config.get('iqa', 'hmpassword')
    nhpassword = config.get('iqa', 'nh_password')
    appurl = config.get('iqa', 'appurl')
    # The soap and rest services URIs
    config.read(utils.ipfilepath)
    gkip = config.get("iqa", "gk_ip")
    gkurl = gkip + utils.gktoken_resource_path
    queryul = gkip + utils.query_resource_path
    updateuserurl = gkip + utils.updateUser_resource_path
    getpasswordurl = gkip + utils.getPassword_resource_path
    b2Ourl = config.get("iqa", "b_o_ip") + ":" + config.get("iqa", "b_o_port") + utils.b2O_resource_path
    b2Ofilepath = utils.b_o_filepath
    b2Ooutputfile = utils.b_o_filepath_output
    testName = utils.whoami()
    test = DataGenerator()
    testdata_job = test.getdata(utils.testdata_filepath, testName, jobworkflow)
    print(type(testdata_job[0]))

    @pytest.mark.smoke
    def test_BtoO(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        lp.soaputil.sendPayload(self.b2Ofilepath, self.clientname, self.testdata_job[4], self.jobworkflow, self.hm,
                                self.rec,
                                self.state, self.testdata_job[2], self.testdata_job[0], self.testdata_job[1],
                                self.testdata_job[3],
                                self.b2Ofilepath,
                                self.b2Ooutputfile, self.b2Ourl)
        lp.restutil.password_reset_sequence(self.clientname, self.admin, self.adminpassword, self.testdata_job[2],
                                            self.nhpassword,
                                            self.gkurl
                                            , self.queryul, self.updateuserurl, self.getpasswordurl)
        ts.mark("Pass", "B-O is passed")
        self.driver.get(self.appurl)
        time.sleep(1)
        assert "Login | Infinite Brassring Platform", "Login page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Login page")

    def test_login_onboard(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        lp.logintsonboard(self.appurl, self.hm, self.hmpassword)
        time.sleep(5)
        assert "Onboard home | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Landing Page")

    def test_logout_onboard(self):
        home = HomePage(self.driver)
        ts = TestStatus(self.driver)
        home.logoutfromts()
        time.sleep(1)
        assert "Login | Infinite Brassring Platform", "Login page displayed" in self.driver.title
        ts.mark("Pass", "User is successfully logout from the application")

    def test_login_nh(self):
        lp = TSLoginPage(self.driver)
        ts = TestStatus(self.driver)
        lp.logintsonboard(self.appurl, self.testdata_job[2], self.nhpassword)
        time.sleep(5)
        assert "Onboard home | Onboard Manager | Infinite BrassRing Platform", "Home page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Landing Page")

    def test_logout_onboard_nh(self):
        home = HomePage(self.driver)
        ts = TestStatus(self.driver)
        home.logoutfromts()
        time.sleep(1)
        assert "Login | Infinite Brassring Platform", "Login page displayed" in self.driver.title
        ts.mark("Pass", "User is successfully logout from the application")
