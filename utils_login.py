from selenium.webdriver.common.action_chains import ActionChains
from statics import LOGGER
from locators import *


def login_test(data_login, index, driverSetup):
    """
    Several user login.
    :return:
        Login done.
    """
    driverSetup.implicitly_wait(30)
    action = ActionChains(driverSetup)
    driverSetup.find_element('xpath', entry_button_xpath).click()
    LOGGER.debug('Click the "login or register" button.')
    username = driverSetup.find_element('name', username_textbox_name)
    action.move_to_element(username).click().send_keys(data_login.get(index).get('username')).click().perform()
    LOGGER.debug('Send keys username.')
    driverSetup.find_element('xpath', continue_button_xpath).click()
    LOGGER.debug('Click the "login next" button.')
    password = driverSetup.find_element('xpath', password_textbox_xpath)
    action.move_to_element(password).click().send_keys(data_login.get(index).get('password')).click().perform()
    LOGGER.debug('Send keys password.')
    driverSetup.find_element('xpath', login_button_xpath).click()  # Login button
    LOGGER.debug('Click the "login" button.')