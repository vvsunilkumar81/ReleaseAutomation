import pytest

from pages.common.LoginPage import TSLoginPage
from resources import tsconfig as utils
import configparser

from utility.datagenerator import DataGenerator
from utility.teststatus import TestStatus


@pytest.mark.usefixtures("test_setup")
class TestSmoke():
    # Static  properties
    config = configparser.ConfigParser()
    config.read(utils.configfilepath)
    state = 'Alabama'
    jobworkflow = config.get('newui', 'wf_notemplate')
    hm = config.get('newui', 'hmusername')
    admin = config.get('newui', 'admin_user')
    adminpassword = config.get('newui', 'admin_password')
    rec = config.get('newui', 'recusername')
    clientname = config.get('newui', 'client_name')
    hmpassword = config.get('newui', 'password')
    nhpassword = config.get('newui', 'nh_password')
    appurl = config.get('newui', 'client_URL')
    # The soap and rest services URIs
    config.read(utils.ipfilepath)
    gkip = config.get("newui", "gk_ip")
    gkurl = gkip + utils.gktoken_resource_path
    queryul = gkip + utils.query_resource_path
    updateuserurl = gkip + utils.updateUser_resource_path
    getpasswordurl = gkip + utils.getPassword_resource_path
    b2Ourl = config.get("newui", "b_o_ip") + ":" + config.get("newui", "b_o_port") + utils.b2O_resource_path
    b2Ofilepath = utils.b_o_filepath_smoke
    b2Ooutputfile = utils.b_o_filepath_smoke_output
    testName = utils.whoami()

    test = DataGenerator()
    testdata_job = test.getdata(utils.testdata_filepath, testName,jobworkflow)
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
                                utils.b_o_filepath_smoke_output, self.b2Ourl)
        lp.restutil.password_reset_sequence(self.clientname, self.admin, self.adminpassword, self.testdata_job[2],
                                            self.nhpassword,
                                            self.gkurl
                                            , self.queryul, self.updateuserurl, self.getpasswordurl)
        ts.mark("Pass","B-O is passed")
        self.driver.get(self.appurl)
        assert "Login | Infinite Brassring Platform","Login page displayed" in self.driver.title
        ts.mark("Pass", "User is being navigated to Login page")

    def test_logintoapplication(self):
            lp = TSLoginPage(self.driver)
            ts = TestStatus(self.driver)
            lp.logintsonboard(self.appurl, self.hm, self.hmpassword)


