from lib2to3.pgen2 import driver
import sys
import time
import unittest

sys.path.insert(0, 'D:/Farzan/flytoday')
import warnings
from selenium import webdriver
from statics import LOGGER, setup
from locators import *
from selenium.webdriver.chrome.options import Options
from LoginTests.utils import login_assertion, get_data


class TestCase_Login(unittest.TestCase):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    def test_login(self):
        """
        Several user login.
        :return:
            Login done.
        """

        data = get_data()
        LOGGER.debug('Inputs read completely.')
        for index in range(len(data)):
            driver = setup()
            time.sleep(2)
            driver.find_element('xpath',
                                entry_button_xpath).click()  # login or register button
            LOGGER.debug('Click the "login or register" button.')
            time.sleep(2)
            username = driver.find_element('name',
                                           username_textbox_name)
            username.click()
            username.send_keys(data.get(index).get('username'))
            LOGGER.debug('Send keys username.')
            time.sleep(3)
            driver.find_element('xpath',
                                continue_button_xpath).click()
            LOGGER.debug('Click the "continue" button.')
            time.sleep(3)
            password = driver.find_element('xpath',
                                           password_textbox_xpath)
            password.click()
            password.send_keys(data.get(index).get('password'))
            LOGGER.debug('Send keys password.')
            driver.find_element('xpath',
                                login_button_xpath).click()  # Login button
            time.sleep(2)
            LOGGER.debug('Click the "login" button.')
            login_assertion(data, index, driver)
            return driver
            # self.tear_down()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
