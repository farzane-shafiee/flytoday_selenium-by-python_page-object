"""
Login
"""
entry_button_xpath = '//span[@class="me-2"] [text()="ورود"]'
username_textbox_name = 'emailOrMobile'
continue_button_xpath = '//button[@type="primary"] [text()="ادامه"]'
password_textbox_xpath = '//*[@id="__next"]/div/div[2]/div[2]/form/div/div[2]/div/input'
login_button_xpath = '//button[@type="primary"] [text()="ورود"]'

"""
Booking Hotel Online
"""
hotel_button_xpath = '//div[@class="tabs_text__6YpmA"] [text()="هتل"]'
hotelCity_selectBox_xpath = '//button[@data-test="hotelCitySelectBox"]'
cityList_xpath = '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div/button/div[2]/div[2]/div[3]'
month_list_xpath = '/html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div[2]' \
                   '/div/div[2]/div[2]/div[2]'
daysList_className = 'month_flexDayStyle__Sp81_'
confirmDatePiker_button_xpath = '//button[@class="button_primaryBtn__L9gAL footer_closeButton__AdqEJ"] [text()="تایید"]'
searchButton_button_xpath = '//button[@class="button_primaryBtn__L9gAL search-button"]'
hotelList_list_xpath = '//*[@id="__next"]/div/div[2]/div[2]/div/div/div/div[2]'
