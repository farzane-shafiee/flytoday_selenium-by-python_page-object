import time
import unittest
import warnings

from selenium import webdriver
from LoginTests.utils import login_assertion, get_data
from LoginTests.statics import LOGGER
from .locators import *
from selenium.webdriver.chrome.options import Options


class Test(unittest.TestCase):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    def setup(self):
        """
        :return: Open browser by URL or exception None.
        """
        self.driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe',
                                       chrome_options=self.chrome_options)
        try:
            self.driver.get('https://betademo.flytoday.ir/')
            warnings.simplefilter('ignore', ResourceWarning)
            LOGGER.debug('Open the browser ...')
        except Exception as exc:
            LOGGER.debug(f'Error exception is: {exc}')

    def tear_down(self):
        """
        :return: Close browser.
        """
        self.driver.close()
        # self.driver.quit()

    def test_login(self):
        """
        Several user login.
        :return:
            Login done.
        """
        data = get_data()
        LOGGER.debug('Inputs read completely.')
        for index in range(len(data)):
            self.setup()
            time.sleep(2)
            self.driver.find_element('xpath',
                                     entry_button_xpath).click()  # login or register button
            LOGGER.debug('Click the "login or register" button.')
            time.sleep(2)
            username = self.driver.find_element('name',
                                                username_textbox_name)
            username.click()
            username.send_keys(data.get(index).get('username'))
            LOGGER.debug('Send keys username.')
            time.sleep(3)
            self.driver.find_element('xpath',
                                     continue_button_xpath).click()
            LOGGER.debug('Click the "continue" button.')
            time.sleep(3)
            password = self.driver.find_element('xpath',
                                                password_textbox_xpath)
            password.click()
            password.send_keys(data.get(index).get('password'))
            LOGGER.debug('Send keys password.')
            self.driver.find_element('xpath',
                                     login_button_xpath).click()  # Login button
            time.sleep(2)
            LOGGER.debug('Click the "login" button.')
            login_assertion(data, index, driver=self.driver)
            self.tear_down()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
