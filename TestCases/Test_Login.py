import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen

class Test_01_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_HomepageTitle(self,setup):
        self.logger.info("***************Test Case 1********************")
        self.logger.info("******************Start*******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title=="nopCommerce demo store. Login":
            assert True
        else:
            assert False

    def test_TestLogin(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.obj = Login(self.driver)
        self.obj.setUsername(self.username)
        self.obj.setPassword(self.password)
        self.obj.clickLogin()
        #time.sleep(5)
        act_title = self.driver.title
        # if act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\"+"test_TestLogin.png")
        #     self.driver.close()
        #     self.logger.error("*******Failed***********")
        #     assert False


