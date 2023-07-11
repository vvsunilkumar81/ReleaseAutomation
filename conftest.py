import contextlib
import sys

import pytest
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from resources import tsconfig as utils
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
import logging

from utility.datagenerator import DataGenerator

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser that the automation will run in")
    parser.addoption("--log.enable", action="append", default="firefox", help="browser that the automation will run in")


def pytest_configure(config):
    """Disable the loggers."""
    for name in config.getoption("--log-enable", default=[]):
        logger = logging.getLogger(name)
        logger.propagate = False


@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--ignore-certificate-errors')
        driverService = Service(utils.ffdriver_path)
        driver = webdriver.Firefox(service=driverService, options=opts)
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument('--ignore-certificate-errors')
        driverService = Service(utils.chromedriver_path)
        driver = webdriver.Chrome(service=driverService, options=opts)
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    print("Test completed")



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Talent Suite Onboard Automation Report"
