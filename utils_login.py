from selenium.webdriver.common.action_chains import ActionChains
from statics import LOGGER
from locators import *
import yaml
import time


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


def login_assertion(data, index, driverSetup):
    elements = driverSetup.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data.get(index).get("username")}')
    assert actual_result == data.get(index).get("username")
    LOGGER.debug('--------------------- ')