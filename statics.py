from lib2to3.pgen2 import driver
from autoutils.log import Logger
from selenium import webdriver
import warnings

LOGGER = Logger.get_logger(__name__)
LOGGER.setLevel('DEBUG')

def setup():
        """
        :return: Open browser by URL or exception None.
        """
        driver = webdriver.Chrome('D:\Farzan\chromedriver_win32\chromedriver.exe')
        try:
            driver.get('https://betademo.flytoday.ir/')
            warnings.simplefilter('ignore', ResourceWarning)
            LOGGER.debug('Open the browser ...')
            return driver
        except Exception as exc:
            LOGGER.debug(f'Error exception is: {exc}')
         
            
def tear_down(driver):
        """
        :return: Close browser.
        """
        driver.close()
        # self.driver.quit()