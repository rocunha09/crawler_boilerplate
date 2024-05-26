from src.enum.EBrowser import EBrowser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
#from selenium.webdriver.opera.service import Service as OperaService
#from selenium.webdriver.opera.options import Options as OperaOptions


from setup.setup_env import FIREFOX_PATH, FIREFOX_DRIVER_PATH, CHROME_PATH, CHROME_DRIVER_PATH, EDGE_PATH, EDGE_DRIVER_PATH, OPERA_PATH, OPERA_DRIVER_PATH

def start(browser):
    driver = DriverFactory.create_driver(browser)
    return driver

class DriverFactory:
    @staticmethod
    def create_driver(browser):
        if browser == EBrowser.FIREFOX:
            return DriverFactory.create_firefox_driver()
        elif browser == EBrowser.CHROME:
            return DriverFactory.create_chrome_driver()
        elif browser == EBrowser.EDGE:
            return DriverFactory.create_edge_driver()
        elif browser == EBrowser.OPERA:
            return DriverFactory.create_opera_driver()
        else:
            raise ValueError('Browser not supported')
    
    @staticmethod
    def create_firefox_driver():
        # setup firefox options
        options = FirefoxOptions()
        options.binary_location = FIREFOX_PATH 
        
        # setup geckodriver service
        service = FirefoxService(executable_path=FIREFOX_DRIVER_PATH)

        # initializing firefox
        driver = webdriver.Firefox(service=service, options=options)
    
        return driver, Keys, By

    @staticmethod
    def create_chrome_driver():
        pass

    @staticmethod
    def create_edge_driver():
        pass

    @staticmethod
    def create_opera_driver():
        pass