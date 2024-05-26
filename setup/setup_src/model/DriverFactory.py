from setup.setup_src.utils.EBrowser import EBrowser
from setup.setup_env import get_env

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

class DriverFactory:
    @staticmethod
    def create_driver(browser):
        try:
            for browser_tup in EBrowser:
                if browser_tup.value[0] == browser:
                    return eval(browser_tup.value[1])()
        except:
            raise ValueError('Browser not supported')
    
    @staticmethod
    def create_firefox_driver():
        options = FirefoxOptions()
        options.binary_location = get_env('FIREFOX_WIN_BINARY_PATH') 
        
        service = FirefoxService(executable_path=get_env('GECKODRIVER_WIN_DRIVER_PATH') )

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