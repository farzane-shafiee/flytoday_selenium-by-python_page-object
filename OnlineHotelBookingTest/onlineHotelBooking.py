import unittest
import sys
sys.path.insert(0, 'D:/Farzan/flytoday')
from LoginTests.login import *


class TestCase_OnlineHotelBooking(unittest.TestCase):
    def test_onlineHotelBooking(self):
        TestCase_Login.test_login()


if __name__ == '__main__':
    unittest.main()
