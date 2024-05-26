from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from setup.setup_env import FIREFOX_BINARY_PATH, GECKODRIVER_PATH

def start():
    # setup firefox options
    options = Options()
    options.binary_location = FIREFOX_BINARY_PATH 
    
    # setup geckodriver service
    service = FirefoxService(executable_path=GECKODRIVER_PATH)

    # initializing firefox
    driver = webdriver.Firefox(service=service, options=options)
    
    return driver, Keys, By