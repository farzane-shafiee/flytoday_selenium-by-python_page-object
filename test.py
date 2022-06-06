import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def do():
    driver = webdriver.Chrome('C:/Users/f.shafiee/Desktop/FlyToday/flytoday/chromedriver_win32/chromedriver.exe')
    driver.get('https://betademo.flytoday.ir/')

    time.sleep(5)

    element = driver.find_element('xpath', '//div[@class="tabs_text__6YpmA"] [text()="هتل"]')
    element.click()
    # print(element.text)

    # elements = driver.find_elements(by=By.XPATH, value='//span[@class="me-2"]')
    # for element in elements:
    #     if 'ورود' in element.text:
    #         element.click()

    time.sleep(10)


if __name__ == '__main__':
    do()
