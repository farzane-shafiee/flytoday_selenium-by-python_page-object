from statics import *
from locators import *
import yaml
import time


def get_data_hotel():
    LOGGER.debug('Trying to read inputs hotel.')
    with open('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday/data_hotel.yaml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def online_Hotel_test(data_hotel, driverSetup):
    action = ActionChains(driverSetup)
    time.sleep(1)
    hotel_button = driverSetup.find_element('xpath', hotel_button_xpath)
    hotel_button.click()
    LOGGER.debug('Click the hotel.')
    time.sleep(1)
    hotel_city = driverSetup.find_element('xpath', hotelCity_selectBox_xpath)
    hotel_city.click()
    LOGGER.debug('Click the hotel city.')
    action.move_to_element(hotel_city).send_keys(data_hotel.get(0).get('hotelCity')).click().perform()
    time.sleep(1)
    cityList = driverSetup.find_element('xpath', cityList_xpath)
    cities = cityList.find_elements(by=By.CLASS_NAME, value='w-100')
    for city in cities:
        LOGGER.debug('City is reading.')
        if city.text == data_hotel.get(0).get('hotelCity'):
            time.sleep(1)
            action.move_to_element(city).click().perform()
            LOGGER.debug('Select city.')
            break
        else:
            LOGGER.debug('city is out off list.')
    LOGGER.debug('insert hotel city.')
    time.sleep(1)
    datePiker(driverSetup, data_hotel)


def hotel_result_search(driverSetup):
    hotelList = driverSetup.find_element('xpath', hotelList_list_xpath)
    hotels = hotelList.find_elements(by=By.CLASS_NAME, value='itineray-list_itineraryWrapper__KEXFz')
    return hotels


def hotelBooking_assertion(driverSetup):
    time.sleep(20)
    LOGGER.debug('Assertion is Checking...')
    hotels = hotel_result_search(driverSetup)
    assert len(hotels) > 0
