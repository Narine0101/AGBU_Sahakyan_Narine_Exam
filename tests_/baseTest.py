import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener



class BaseTestWithoutLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()


class BaseTestWithLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

        self.loginPageObj.click_to_continue_button()
        time.sleep(7)
        self.loginPageObj.click_to_signin_button()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
