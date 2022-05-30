import webdriver_manager
from autoutils.log import Logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators import *
import warnings
import time
import yaml

LOGGER = Logger.get_logger(__name__)
LOGGER.setLevel('DEBUG')


def driver_setup():
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/chromedriver_win32/chromedriver.exe')
    return driver


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


def get_data_login():
    """
    :return: list of dic from yaml file.
    """
    LOGGER.debug('Trying to read username and password.')
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


def get_data_passenger():
    LOGGER.debug('Trying to read data passenger.')
    with open('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/flytoday/data_passenger.yaml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


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
