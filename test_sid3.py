from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pom import Loginpage
import time
class TestLogin:
    @pytest.fixture()
    def test_login(self):
        self.serv_obj = Service("C:\Drivers\chromedriver_win32 110\chromedriver")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        self.driver.get("https://demotibilians.tibilprojects.com/#/authentication/login")
        self.lp = Loginpage(self.driver)
        self.lp.setUserName("admin@tibilsolutions.com")
        time.sleep(2)
        self.lp.setPassword("tibil@123")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(7)
        # self.driver.implicitly_wait(120)
        # wait=WebDriverWait(driver,10)
        yield
        self.driver.close()
# 3.1 Admin User wants to move from Homepage to staff Directory
    def test_staffdrirectoy(self,test_login):
            action = ActionChains(self.driver)
            element = self.driver.find_element(By.XPATH,"//body/app-root/app-dashboard[@class='ng-star-inserted']/app-header/div[@class='header-classic fixed-top navbar-light wow fadeInDown']/div[@class='container']/div[@class='row']/div[@class='col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12']/nav[@class='navbar navbar-expand-lg navbar-classic d-flex align-items-center']/div[@id='navbar-classic']/ul[@class='navbar-nav ml-auto mt-2 mt-lg-0 mr-3']/li[2]/a[1]")
            action.move_to_element(element)
            action.perform()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"//a[normalize-space()='Staff Directory']").click()
            time.sleep(2)
# 3.2 Admin User wants to add employee
    def test_addemployee(self,test_login):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH,
                                           "//body/app-root/app-dashboard[@class='ng-star-inserted']/app-header/div[@class='header-classic fixed-top navbar-light wow fadeInDown']/div[@class='container']/div[@class='row']/div[@class='col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12']/nav[@class='navbar navbar-expand-lg navbar-classic d-flex align-items-center']/div[@id='navbar-classic']/ul[@class='navbar-nav ml-auto mt-2 mt-lg-0 mr-3']/li[2]/a[1]")
        action.move_to_element(element)
        action.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Staff Directory']").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Employee']").click()
        time.sleep(5)
# 3.1 Add the employee details
    def test_addempdetails(self,test_login):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH,
                                           "//body/app-root/app-dashboard[@class='ng-star-inserted']/app-header/div[@class='header-classic fixed-top navbar-light wow fadeInDown']/div[@class='container']/div[@class='row']/div[@class='col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12']/nav[@class='navbar navbar-expand-lg navbar-classic d-flex align-items-center']/div[@id='navbar-classic']/ul[@class='navbar-nav ml-auto mt-2 mt-lg-0 mr-3']/li[2]/a[1]")
        action.move_to_element(element)
        action.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Staff Directory']").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Employee']").click()
        time.sleep(5)
        # self.driver.find_element(By.ID, "firstName").send_keys("park")
        # self.driver.find_element(By.ID, "middleName").send_keys("jm")
        # self.driver.find_element(By.ID, "lastName").send_keys("testing")
        # self.driver.find_element(By.ID, "email").send_keys("testing@tibilsolutions.com")
        # self.driver.find_element(By.ID, "tibilID").send_keys("TIBIL777")
        # self.driver.find_element(By.XPATH,"//ng-select[@id='designation']//span[@class='ng-arrow-wrapper']").click()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'Software Engineer Trainee')]").click()
        self.driver.find_element(By.XPATH, "//ng-select[@placeholder='Select Skills']//span[@class='ng-arrow-wrapper']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/ng-dropdown-panel/div/div[2]/div[1]/input").click()
        time.sleep(3)


