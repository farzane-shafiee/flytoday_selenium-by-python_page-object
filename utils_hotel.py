from statics import *
from locators import *
import yaml
import time


def hotel_search(data_hotel, driverSetup):
    driverSetup.implicitly_wait(20)
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
    LOGGER.debug('Search hotel is completed.')
    # time.sleep(20)


def hotel_result_search(driverSetup):
    hotelList = driverSetup.find_element('xpath', hotelList_list_xpath)
    hotels = hotelList.find_elements(by=By.CLASS_NAME, value='itineray-list_itineraryWrapper__KEXFz')
    return hotels


def hotel_booking_assertion(driverSetup):
    LOGGER.debug('Assertion is Checking...')
    hotels = hotel_result_search(driverSetup)
    assert len(hotels) > 0


def adding_adult(driverSetup):
    element = driverSetup.find_element('xpath', '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]'
                                                '/div[2]/div/div[2]/div[2]/button[1]')
    element.click()


def adding_child(driverSetup):
    element = driverSetup.find_element('xpath', '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]'
                                                '/div[2]/div/div[3]/div[2]/button[1]')
    element.click()


def adding_room(driverSetup):
    element = driverSetup.find_element('xpath', '//button[@data-test="addRoomBtn"]')
    element.click()


def passenger_list(driverSetup):
    list = driverSetup.find_element('xpath', passengerTable_table_xpath)
    passengerList = list.find_elements(by=By.CLASS_NAME, value='add-passenger_row__FrB_E')
    return passengerList


def select_passenger(driverSetup):
    passengerList = passenger_list(driverSetup)
    passengerList[0].click()


def insert_passenger(driverSetup):
    action = ActionChains(driverSetup)
    data_passenger = get_data_passenger()
    name = driverSetup.find_element('id', name_input_id)
    lastName = driverSetup.find_element('id', lastName_input_id)
    email = driverSetup.find_element('id', email_input_id)
    mobile = driverSetup.find_element('id', mobile_input_id)

    action.move_to_element(name).click().send_keys(data_passenger.get(0).get('name')).click().perform()
    action.move_to_element(lastName).click().send_keys(data_passenger.get(0).get('lastName')).click().perform()
    action.move_to_element(email).click().send_keys(data_passenger.get(0).get('email')).click().perform()
    action.move_to_element(mobile).click().send_keys(data_passenger.get(0).get('mobile')).click().perform()


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
    driverSetup.find_element('xpath', selectHotel_button_xpath).click()
    LOGGER.debug('Hotel is selected.')

    time.sleep(3)
    driverSetup.switch_to.window(driverSetup.window_handles[1])
    driverSetup.execute_script("window.scrollBy(0,200)")
    # time.sleep(3)
    # scroll_to_find_element(driverSetup, ['xpath', selectRoom_button_xpath], 7000)
    time.sleep(2)
    driverSetup.find_element('xpath', selectRoom_button_xpath).click()
    LOGGER.debug('Room is Selected.')
    time.sleep(2)
    driverSetup.find_element('xpath', selectReserv_button_xpath).click()
    LOGGER.debug('Reserv is selected.')
    time.sleep(2)
    driverSetup.find_element('xpath', showPassengerModal_button_xpath).click()
    time.sleep(1)

    select_passenger(driverSetup) if len(passenger_list(driverSetup)) > 0 else insert_passenger(driverSetup)
    driverSetup.find_element('xpath', continueHotel_button_xpath).click()
    LOGGER.debug('Adding passenger is successful.')
    time.sleep(5)
    driverSetup.find_element('xpath', rulseConfirm_checkbox_xpath).click()
    driverSetup.find_element('xpath', continueHotel_button_xpath).click()
    LOGGER.debug('Confirm and payment is completed.')
    time.sleep(5)
