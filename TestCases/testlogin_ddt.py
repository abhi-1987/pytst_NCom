import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLUtils
class Test_02_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/testdata.xlsx"
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_TestLogin_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.obj = Login(self.driver)
        self.rows = XLUtils.getrowcount(self.path,'Sheet1')
        #self.cols = XLUtils.getcolcount(self.path,'Sheet1')
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd = XLUtils.readData(self.path,'Sheet1',r,2)
            self.obj.setPassword(self.user)
            self.obj.setPassword(self.pwd)
            self.obj.clickLogin()
            time.sleep(10)
            self.obj.clickLogout()



