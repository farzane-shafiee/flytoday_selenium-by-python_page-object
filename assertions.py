from statics import *
from utils_hotel import hotel_result_search


def login_assertion(data_login, index, driverSetup):
    elements = driverSetup.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data_login.get(index).get("username")}')
    assert actual_result == data_login.get(index).get("username")
    LOGGER.debug('------------------------------------------------ ')


def hotel_search_assertion(driverSetup):
    LOGGER.debug('Assertion is Checking...')
    hotels = hotel_result_search(driverSetup)
    assert len(hotels) > 0


def hotel_booking_assertion(driverSetup):
    assert driverSetup.find_element('xpath', '(// *[text() = "دریافت واچر"])[1]') is True
