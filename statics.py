from autoutils.log import Logger
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from locators import *
import warnings
import yaml
import time

LOGGER = Logger.get_logger(__name__)
LOGGER.setLevel('DEBUG')


def driver_setup():
    driver = webdriver.Chrome('D:/Farzan/chromedriver_win32/chromedriver.exe')
    return driver


def get_data_login():
    """
    :return: list of dic from yaml file.
    """
    LOGGER.debug('Trying to read inputs.')
    with open('D:/Farzan/flytoday/data_login.yaml', 'r') as file:
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
    # data = get_data()
    LOGGER.debug('Inputs read completely.')
    time.sleep(2)
    driverSetup.find_element('xpath',
                             entry_button_xpath).click()  # login or register button
    LOGGER.debug('Click the "login or register" button.')
    time.sleep(2)
    username = driverSetup.find_element('name',
                                        username_textbox_name)
    username.click()
    username.send_keys(data.get(index).get('username'))
    LOGGER.debug('Send keys username.')
    time.sleep(3)
    driverSetup.find_element('xpath',
                             continue_button_xpath).click()
    LOGGER.debug('Click the "continue" button.')
    time.sleep(3)
    password = driverSetup.find_element('xpath',
                                        password_textbox_xpath)
    password.click()
    password.send_keys(data.get(index).get('password'))
    ee = data.get(3).get('password')
    print(ee)
    LOGGER.debug('Send keys password.')
    driverSetup.find_element('xpath',
                             login_button_xpath).click()  # Login button
    time.sleep(2)
    LOGGER.debug('Click the "login" button.')


def get_data_hotel():
    LOGGER.debug('Trying to read inputs hotel.')
    with open('D:/Farzan/flytoday/data_hotel.yaml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def datePiker(driverSetup, data_hotel):
    element = driverSetup.find_element('xpath', '//*[@id="__next"]/div/div[3]/div/div/div/div[2]/div[2]/div/div/'
                                                  'div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]')
    days = element.find_elements_by_class_name('month_flexDayStyle__Sp81_')
    print(days)
    LOGGER.debug('Read date piker list.')
    for day in days:
        print(day.text)
        if day.text == data_hotel.get(0).get('startDate'):
            day.click()
            time.sleep(5)
        # if y.text == data_hotel.get(0).get('endDate'):
        #     y.click()
    time.sleep(5)
    print("ok")
    # words = elements[0].text.split('\n')
    # for index in elements:
    #     if words[index] == data_hotel.get(0).get('startDate'):
    #         elements[index].click()
    #         break


def online_Hotel_Booking_test(data_hotel, driverSetup):
    action = ActionChains(driverSetup)
    time.sleep(3)
    hotel_button = driverSetup.find_element('xpath', hotel_button_xpath)
    hotel_button.click()
    print(hotel_button_xpath)
    LOGGER.debug('Click the hotel.')
    time.sleep(3)
    hotel_city = driverSetup.find_element('xpath', hotelCity_selectBox_xpath)
    hotel_city.click()
    LOGGER.debug('Click the hotel city.')
    action.move_to_element(hotel_city).send_keys(data_hotel.get(0).get('hotelCity')).click().perform()
    # hotel_city.send_keys(data_hotel.get(0).get('hotelCity'))
    # hotel_city.click()
    time.sleep(5)
    print(data_hotel.get(0).get('hotelCity'))
    city = driverSetup.find_element('xpath', '//*[@id="__next"]/div/div[3]/div/div/div/div[2]/div[1]'
                                             '/div/button/div[2]/div[2]/div[3]/div[1]')
    action.move_to_element(city).click().perform()
    LOGGER.debug('insert hotel city.')
    time.sleep(10)
    datePiker(driverSetup, data_hotel)


def login_assertion(data, index, driverSetup):
    elements = driverSetup.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data.get(index).get("username")}')
    assert actual_result == data.get(index).get("username")
    LOGGER.debug('--------------------- ')