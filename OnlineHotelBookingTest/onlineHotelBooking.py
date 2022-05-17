from lib2to3.pgen2 import driver
import sys
import unittest
sys.path.insert(0, 'D:/Farzan/flytoday')
from LoginTests.login import TestCase_Login
from selenium import webdriver
from locators import *


class TestCase_OnlineHotelBooking(unittest.TestCase):
    def test_onlineHotelBooking(self):
        driver = TestCase_Login.test_login()
        driver.find_element('xpath', hotel_button_xpath).click()


if __name__ == '__main__':
    unittest.main()
