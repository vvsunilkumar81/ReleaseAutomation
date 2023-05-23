import utility.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from pages.common.HomePage import HomePage


class NoTemplatePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.hm = HomePage(driver)

    boolean_field_id = "checkBox9469"
    listbox_id = "field1690"
    listboxvalue_xpath = "/ul[@class='MuiList-root']//li"
    nh_task_xpath = "//a[@class='title']/a"
    radiobutton_id = "radio1692_2"
    textbox_id = "field1737"
    int_id = "field22101"
    selectbox_id = "field1690"
    multiselect_id = "field11251"
    multi_select_icon_open = "svg.MuiSelect-iconOpen"
    multi_select_icon_close = "svg.MuiSelect-iconOutlined"
    success_button_xpath = "//button[@label='Submit']"
    save_finish_later = "saveAndFinishLaterBtn"
    date_completed = "input#mui-12"
    text_field_css = "input#field205"
    due_date = "input#mui-11"
    successbutton_css = "button.btn-success"

    def click_newhiretask(self, task_name):
        self.log.info("Click on newhire task to navigate to task page")
        self.log.info("Get the newhire task name")
        taskname = self.getText(locator=self.nh_task_xpath, locatorType='xpath')
        if (taskname == task_name):
            self.elementClick(self.nh_task_xpath, locatorType="xpath")
        else:
            self.log.info("task is not found")

    def completeNoTemplateTask(self):
        self.elementClick(self.boolean_field_id)
        time.sleep(1)
        self.selectvaluefromdropdown("WebServices", self.listbox_id)
        time.sleep(2)
        self.elementClick(self.radiobutton_id)
        time.sleep(1)
        self.webScroll("down")
        time.sleep(1)
        self.selectvaluefromdropdown("WebServices", self.multiselect_id)
        time.sleep(1)
        self.selectvaluefromdropdown("Python", self.multiselect_id)
        time.sleep(1)
        #self.elementClick(self.multi_select_icon_close, locator="css")
        time.sleep(1)
        self.sendKeys("ICICI", self.textbox_id)
        time.sleep(2)
        self.sendKeys("5", self.int_id)
        time.sleep(2)
        self.elementClick(self.success_button_xpath, locatorType="xpath")
        time.sleep(2)
        return self.hm
