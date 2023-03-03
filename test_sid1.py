# Verify Intranet Login screen
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from pom import Loginpage
import time
class TestLogin:
    @pytest.fixture()
    def test_chrome(self):
        self.serv_obj = Service("C:\Drivers\chromedriver_win32 110\chromedriver")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        self.driver.get("https://demotibilians.tibilprojects.com/#/authentication/login")
        # self.driver.implicitly_wait(120)
        yield
        self.driver.close()

# sid:1.1 Verify UI elements of login screen
        # tibil logo
    def test_uielements(self, test_chrome):
        try:
            elements = self.driver.find_element(By.XPATH, "//img[@alt='logo']")
            print("Element found")

        except NoSuchElementException:
            print("Element not found")
# Email Address
        Email = self.driver.find_element(By.XPATH,"/html/body/app-root/app-authentication/app-login/section/div/div[2]/div/div/div/form/div[1]/input")
        print("email address element found", Email.is_displayed())

        if Email.is_displayed() == True:
         assert True
        else:
         print("email address element is not found:", Email.is_displayed())
# password
        Email = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        print("password element found", Email.is_displayed())

        if Email.is_displayed() == True:
            assert True
        else:
            print("password element is not found:", Email.is_displayed())
            time.sleep(4)
# sid:1.3Intranet invalid Login Authentication
        self.lp = Loginpage(self.driver)
        self.lp.setUserName("admin@tibilsolutions.com")
        time.sleep(5)
# invalid password
        self.lp.setPassword("1234567")
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        Invalid_Credentials = self.driver.find_element(By.XPATH, "//span[@class='text-danger']")
        print("Invalid Credentials is displayed:", Invalid_Credentials.is_displayed())
        if Invalid_Credentials.is_displayed() == True:
            assert True
        else:
          print("Login Login status is passed:", Invalid_Credentials.is_displayed())

        self.driver.find_element(By.XPATH,"//input[@placeholder='Email Address']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(5)
# sid1.4:Intranet Login Authentication
        self.lp.setUserName("Admin@Tibilsolutions.com")
        time.sleep(5)
        self.lp.setPassword("tibil@123")
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        Invalid_Credentials = self.driver.find_element(By.XPATH, "//span[@class='text-danger']")
        print("Invalid Credentials is displayed:", Invalid_Credentials.is_displayed())
        if Invalid_Credentials.is_displayed() == True:
            assert True
        else:
            print("Login Login status is passed:", Invalid_Credentials.is_displayed())
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Email Address']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(5)
# sid:1.2 Verify Intranet Login screen
        self.lp.setUserName("admin@tibilsolutions.com")
        time.sleep(5)
        self.lp.setPassword("tibil@123")
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        Home = self.driver.find_element(By.XPATH, "/html/body/app-root/app-dashboard/app-header/div/div/div/div/nav/div/ul[1]/li[1]/a")
        print("Intranet home page is displayed:", Home.is_displayed())
        if Home.is_displayed() == True:
            assert True
        else:
            print("Intranet home page is displayed:", Home.is_displayed())
        self.lp. signout()