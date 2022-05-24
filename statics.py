from autoutils.log import Logger
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from locators import *
import warnings
import yaml
import time

LOGGER = Logger.get_logger(__name__)
LOGGER.setLevel('DEBUG')


def driver_setup():
    driver = webdriver.Chrome('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/chromedriver_win32/chromedriver.exe')
    return driver


def get_data_login():
    """
    :return: list of dic from yaml file.
    """
    LOGGER.debug('Trying to read inputs.')
    with open('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday/data_login.yaml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def get_data_hotel():
    LOGGER.debug('Trying to read inputs hotel.')
    with open('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday/data_hotel.yaml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def setup():
    """
    :return: Open browser by URL or exception None.
    """
    driverSetup = driver_setup()
    try:
        driverSetup.get('https://betademo.flytoday.ir/')
        driverSetup.maximize_window()
        warnings.simplefilter('ignore', ResourceWarning)
        LOGGER.debug('Open the browser ...')
        return driverSetup
    except Exception as exc:
        LOGGER.debug(f'Error exception is: {exc}')


def tear_down(driverSetup):
    """
    :return: Close browser.
    """
    driverSetup.close()
    # DRIVER.quit()


def login_test(data, index, driverSetup):
    """
    Several user login.
    :return:
        Login done.
    """
    action = ActionChains(driverSetup)
    time.sleep(2)
    driverSetup.find_element('xpath',
                             entry_button_xpath).click()  # login or register button
    LOGGER.debug('Click the "login or register" button.')
    time.sleep(2)
    username = driverSetup.find_element('name',
                                        username_textbox_name)
    action.move_to_element(username).click().\
        send_keys(data.get(index).get('username')).click().perform()
    LOGGER.debug('Send keys username.')
    time.sleep(3)
    driverSetup.find_element('xpath',
                             continue_button_xpath).click()
    LOGGER.debug('Click the "continue" button.')
    time.sleep(2)
    password = driverSetup.find_element('xpath',
                                        password_textbox_xpath)
    action.move_to_element(password).click().\
        send_keys(data.get(index).get('password')).click().perform()
    LOGGER.debug('Send keys password.')
    driverSetup.find_element('xpath',
                             login_button_xpath).click()  # Login button
    time.sleep(2)
    LOGGER.debug('Click the "login" button.')


def datePiker(driverSetup, data_hotel):
    action = ActionChains(driverSetup)
    month = driverSetup.find_element(by=By.XPATH, value=month_list_xpath)
    days = month.find_elements(by=By.CLASS_NAME, value=daysList_className)
    LOGGER.debug('Read date piker list.')

    for startDate in days:
        if startDate.text == data_hotel.get(0).get('startDate'):
            action.move_to_element(startDate).click().perform()
            LOGGER.debug('Select start date.')
            break
        else:
            LOGGER.debug('Start date is reading.')

    for endDate in days:
        if endDate.text == data_hotel.get(0).get('endDate'):
            action.move_to_element(endDate).click().perform()
            LOGGER.debug('Select end date.')
            break
        else:
            LOGGER.debug('End date is reading.')
    time.sleep(2)
    driverSetup.find_element('xpath', confirmDatePiker_button_xpath).click()
    driverSetup.find_element('xpath', searchButton_button_xpath).click()
    LOGGER.debug('Search hotel is completed.')
    time.sleep(10)


def online_Hotel_Booking_test(data_hotel, driverSetup):
    action = ActionChains(driverSetup)
    time.sleep(3)
    hotel_button = driverSetup.find_element('xpath', hotel_button_xpath)
    hotel_button.click()
    LOGGER.debug('Click the hotel.')
    time.sleep(3)
    hotel_city = driverSetup.find_element('xpath', hotelCity_selectBox_xpath)
    hotel_city.click()
    LOGGER.debug('Click the hotel city.')
    action.move_to_element(hotel_city).send_keys(data_hotel.get(0).get('hotelCity')).click().perform()
    time.sleep(5)
    cityList = driverSetup.find_element('xpath', cityList_xpath)
    cities = cityList.find_elements(by=By.CLASS_NAME, value='w-100')
    for city in cities:
        LOGGER.debug('City is reading.')
        if city.text == data_hotel.get(0).get('hotelCity'):
            time.sleep(3)
            action.move_to_element(city).click().perform()
            LOGGER.debug('Select city.')
            break
        else:
            LOGGER.debug('city is out off list.')
    LOGGER.debug('insert hotel city.')
    time.sleep(3)
    datePiker(driverSetup, data_hotel)


def login_assertion(data, index, driverSetup):
    elements = driverSetup.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data.get(index).get("username")}')
    assert actual_result == data.get(index).get("username")
    LOGGER.debug('--------------------- ')


def hotelBooking_assertion(data, index, driverSetup):
    pass