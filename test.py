# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def do():
#     driver = webdriver.Chrome('C:\\Users\\f.shafiee\\Downloads\\chromedriver_win32\\chromedriver.exe')
#     driver.get('https://betademo.flytoday.ir/')
#
#     time.sleep(5)
#
#     element = driver.find_element(by=By.X, '//*[@id="back-to-top-anchor"]/header/div/div[2]/button[2]')
#     print(element.text)
#
#     # elements = driver.find_elements(by=By.XPATH, value='//span[@class="me-2"]')
#     # for element in elements:
#     #     if 'ورود' in element.text:
#     #         element.click()
#
#     time.sleep(10)
#
#
# if __name__ == '__main__':
#     do()
