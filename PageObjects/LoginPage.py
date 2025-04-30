from selenium import webdriver
import time
class Login:
    username_textbox_id = "Email"
    password_textbox_id = "Password"
    login_btn_xpath="//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element('id',self.username_textbox_id).clear()
        #time.sleep(5)
        self.driver.find_element('id',self.username_textbox_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element('id',self.password_textbox_id).clear()
        #time.sleep(5)
        self.driver.find_element('id',self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element('xpath',self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element('link text',self.link_logout_text).click()