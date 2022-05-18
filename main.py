import sys
import unittest

sys.path.insert(0, 'C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday')

from statics import *
from selenium.webdriver.chrome.options import Options

current_driver = None


class TestCase(unittest.TestCase):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    def test_login(self):
        data = get_data()
        LOGGER.debug('Inputs read completely.')
        for index in range(len(data)):
            driverSetup = setup()
            login_test(driverSetup, data, index)
            login_assertion(driverSetup, data, index)

    def test_hotel(self):
        data = get_data()
        LOGGER.debug('Inputs read completely.')
        for index in range(len(data)):
            setup()
            login_test()
            online_Hotel_Booking_test()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
