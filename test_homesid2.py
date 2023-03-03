from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from pom import Loginpage
import time


class TestLogin:


    def test_login(self):
        # self.lp = Loginpage(self.driver)
        # u=self.lp.login.url()
        self.serv_obj = Service(Loginpage.chrome)
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        self.driver.get(Loginpage.URL)
        self.driver.find_element(By.XPATH, Loginpage.textbox_username_xpath).send_keys(Loginpage.email)
        self.driver.find_element(By.XPATH, Loginpage.textbox_password_xpath).send_keys(Loginpage.password)
        self.lp = Loginpage(self.driver)
        self.lp.clickLogin()
        time.sleep(10)

    # sid:2.1 Verify embed YouTube video

        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(10)
        # video = self.driver.find_element(By.XPATH, "//iframe[@class='ng-tns-c85-0']")
        # print("embed youtube video is found", video.is_displayed())
        #
        # if video.is_displayed() == True:
        #     assert True
        # else:
        #     print("embed YouTube video is not found:", video.is_displayed())
# clicking on the embed YouTube video
#         self.driver.find_element(By.XPATH, "//iframe[@class='ng-tns-c85-0']").click()
#         time.sleep(5)
#         self.driver.find_element(By.XPATH, "//iframe[@class='ng-tns-c85-0']").click()
#         time.sleep(5)
# clicking add news button
        self.driver.find_element(By.XPATH, "//body//app-root//app-dashboard//section//app-home//section//div//div//div//div//div//div//button[@type='button']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("TESTING")
        time.sleep(5)
        self.driver.find_element((By.XPATH, "/html[1]/body[1]/modal-container[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")).click()
        time.sleep(15)
        driver.close()


        # self.driver.find_element(By.XPATH,"//textarea[@placeholder='Description starts here']").send_keys("testing")
        # time.sleep(6)


