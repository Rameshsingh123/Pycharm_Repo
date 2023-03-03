from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class Loginpage:
# locators

    chrome = "C:\Drivers\chromedriver_win32 110\chromedriver"
    URL = "https://demotibilians.tibilprojects.com/#/authentication/login"
    email = "admin@tibilsolutions.com"
    password = "tibil@123"
    textbox_username_xpath = "//input[@placeholder='Email Address']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[normalize-space()='Login']"
    AR_element="//a[normalize-space()='Awards & Recognition']"
    element_img = "//a[@id='menu-1']//img[@class='rounded-circle']"
    imgxpath = "/html[1]/body[1]/app-root[1]/app-dashboard[1]/app-header[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[2]/li[1]/a[1]/img[1]"
    element_signout_Xpath = "//i[@class='fa fa-sign-out']"
# constructor
    def __init__(self,driver):
        self.driver = driver
# actions methods

# username

    def setUserName(self,username):
        usernametxt = self.driver.find_element(By.XPATH,self.textbox_username_xpath)
        usernametxt.send_keys(username)


#  password
    def setPassword(self,password):
        passwordtxt=self.driver.find_element(By.XPATH,self.textbox_password_xpath)
        passwordtxt.send_keys(password)

# LOGIN
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
# Move cursor on img
    def signout(self):
         action = ActionChains(self.driver)
         element = self.driver.find_element(By.XPATH,self.imgxpath)
         action.move_to_element(element)
         action.perform()
# click signout
         self.driver.find_element(By.XPATH,self.element_signout_Xpath).click()
