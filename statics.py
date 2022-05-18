from autoutils.log import Logger
from selenium import webdriver
from locators import *
import warnings
import yaml
import time

LOGGER = Logger.get_logger(__name__)
LOGGER.setLevel('DEBUG')


def driver_setup():
    driver = webdriver.Chrome('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/chromedriver_win32/chromedriver.exe')
    return driver


def get_data():
    """
    :return: list of dic from yaml file.
    """
    LOGGER.debug('Trying to read inputs.')
    with open('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday/csv.yaml', 'r') as file:
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


def login_test(driverSetup, data, index):
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
    LOGGER.debug('Send keys password.')
    driverSetup.find_element('xpath',
                             login_button_xpath).click()  # Login button
    time.sleep(2)
    LOGGER.debug('Click the "login" button.')
    # global current_driver
    # current_driver = driverSetup
    # tear_down(driverSetup)


def online_Hotel_Booking_test(driverSetup):
    driverSetup.find_element('xpath', hotel_button_xpath).click()


def login_assertion(data, index, driverSetup):
    elements = driverSetup.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data.get(index).get("username")}')
    assert actual_result == data.get(index).get("username")
    LOGGER.debug('--------------------- ')