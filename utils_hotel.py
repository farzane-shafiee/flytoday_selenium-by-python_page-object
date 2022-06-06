from statics import *
from locators import *
import time


def hotel_search(data_hotel, driverSetup):
    driverSetup.implicitly_wait(30)
    action = ActionChains(driverSetup)
    hotel_button = driverSetup.find_element('xpath', hotel_button_xpath)
    hotel_button.click()
    LOGGER.debug('Click the hotel.')
    hotel_city = driverSetup.find_element('xpath', hotelCity_selectBox_xpath)
    hotel_city.click()
    LOGGER.debug('Click the hotel city.')
    action.move_to_element(hotel_city).send_keys(data_hotel.get(0).get('hotelCity')).click().perform()
    cityList = driverSetup.find_element('xpath', cityList_xpath)
    cities = cityList.find_elements(by=By.CLASS_NAME, value='w-100')
    for city in cities:
        LOGGER.debug('City is reading.')
        if city.text == data_hotel.get(0).get('hotelCity'):
            action.move_to_element(city).click().perform()
            LOGGER.debug('Select city.')
            break
        else:
            LOGGER.debug('city is out off list.')
    LOGGER.debug('insert hotel city.')
    datePiker(driverSetup, data_hotel)
    LOGGER.debug('Search hotel is completed.')


def hotel_result_search(driverSetup):
    hotelList = driverSetup.find_element('xpath', hotelList_list_xpath)
    hotels = hotelList.find_elements(by=By.CLASS_NAME, value='itineray-list_itineraryWrapper__KEXFz')
    return hotels


def adding_adult(driverSetup):
    element = driverSetup.find_element('xpath', '(//*[@data-test="addQuantity"])[1]')
    element.click()


def adding_child(driverSetup):
    element = driverSetup.find_element('xpath', '(//*[@data-test="addQuantity"])[2]')
    element.click()


def adding_room(driverSetup):
    element = driverSetup.find_element('xpath', '//button[@data-test="addRoomBtn"]')
    element.click()


def passenger_list(driverSetup):
    list = driverSetup.find_element('xpath', passengerTable_table_xpath)
    passengerList = list.find_elements(by=By.CLASS_NAME, value='add-passenger_row__FrB_E')
    return passengerList


def select_passenger(driverSetup):
    driverSetup.find_element('xpath', showPassengerModal_button_xpath).click()
    LOGGER.debug('Former passenger modal is show.')
    driverSetup.find_element('xpath', selectPassenger_button_xpath).click()


def insert_passenger(driverSetup, data_passenger):
    driverSetup.implicitly_wait(30)
    action = ActionChains(driverSetup)
    name = driverSetup.find_element('id', name_input_id)
    lastName = driverSetup.find_element('id', lastName_input_id)
    email = driverSetup.find_element('id', email_input_id)
    mobile = driverSetup.find_element('id', mobile_input_id)
    time.sleep(1)
    action.move_to_element(name).click().send_keys(data_passenger.get('passenger').get('name')).click().perform()
    LOGGER.debug('Name is insert.')
    action.move_to_element(lastName).click().send_keys(data_passenger.get('passenger').get('lastName')).click().perform()
    LOGGER.debug('Last name is insert.')
    action.move_to_element(email).click().send_keys(data_passenger.get('passenger').get('email')).click().perform()
    LOGGER.debug('Email is insert.')
    action.move_to_element(mobile).click().send_keys(data_passenger.get('passenger').get('mobile')).click().perform()
    LOGGER.debug('Mobile is insert.')


def payment_success(driverSetup):
    driverSetup.find_element('id', paymentSuccess_button_id).click()


def payment_failed(driverSetup):
    driverSetup.find_element('id', paymentFailed_button_id).click()


def scroll_to_find_element(driverSetup, locator, pixel):
    for i in range(10):
        try:
            driverSetup.find_element(locator[0], locator[1])
            LOGGER.debug(f'The element "{locator}" found.')
        except:
            driverSetup.execute_script(f"window.scrollBy(0,{str(pixel)})")
            time.sleep(1)
    raise Exception(f'The element "{locator}" cannot be found.')


def hotel_booking(driverSetup):
    driverSetup.implicitly_wait(40)
    driverSetup.find_element('xpath', selectHotel_button_xpath).click()
    LOGGER.debug('Hotel is selected.')

    time.sleep(2)
    driverSetup.switch_to.window(driverSetup.window_handles[1])
    driverSetup.execute_script("scroll(0,200)")
    # scroll_to_find_element(driverSetup, ['xpath', selectRoom_button_xpath], 7000)
    driverSetup.find_element('xpath', selectRoom_button_xpath).click()
    LOGGER.debug('Room is Selected.')
    driverSetup.find_element('xpath', selectReserv_button_xpath).click()
    LOGGER.debug('Details is read and selected.')
    data_passenger = get_data_passenger()
    # insert_passenger(driverSetup, data_passenger) if data_passenger.get('passenger').get('number_passenger') == '0' \
    #     else select_passenger(driverSetup)
    if data_passenger.get('passenger').get('number_passenger') == '0':
        insert_passenger(driverSetup, data_passenger)
        LOGGER.debug('Passenger is insert.')
    elif data_passenger.get('passenger').get('number_passenger') == '1':
        select_passenger(driverSetup)
        LOGGER.debug('Passenger is selected.')

    driverSetup.find_element('xpath', continueHotel_button_xpath).click()
    LOGGER.debug('Adding passenger is successful.')
    driverSetup.find_element('xpath', rulseConfirm_checkbox_xpath).click()
    driverSetup.find_element('xpath', continueHotel_button_xpath).click()
    LOGGER.debug('Confirm and payment is completed.')
    time.sleep(3)
