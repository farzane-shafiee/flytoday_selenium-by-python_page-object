import sys
import unittest

sys.path.insert(0, 'D:/Farzan/flytoday')
from utils_hotel import *
from statics import *
from utils_login import *
from selenium.webdriver.chrome.options import Options

current_driver = None


class TestCase(unittest.TestCase):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    def test_login(self):
        data = get_data_login()
        LOGGER.debug('Inputs read completely.')
        for index in range(len(data)):
            driverSetup = setup()
            login_test(data, index, driverSetup)
            login_assertion(data, index, driverSetup)

    def test_hotel(self):
        # data_login = get_data_login()
        # LOGGER.debug('Inputs read completely.')
        # for index in range(len(data_login)):
        driverSetup = setup()
        # login_test(data_login, index, driverSetup)
        data_hotel = get_data_hotel()
        online_Hotel_test(data_hotel, driverSetup)
        hotelBooking_assertion(driverSetup)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
