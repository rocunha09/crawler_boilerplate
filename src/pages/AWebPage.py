from abc import ABC, abstractmethod
from src.enum.ETypeIdentify import ETypeIdentify
from main import driver, Keys, By 

class AWebPage(ABC):
    url = None
    page = None

    def __init__(self, url):
        self.url = url
        
        self.page = driver.get(self.url)
        
    def set_web_element(self, identifier, typeIdentifier):
        el = None
        if typeIdentifier == ETypeIdentify.ID:
            el = driver.find_element(By.ID, identifier)
        elif typeIdentifier == ETypeIdentify.CLASS:
            el = driver.find_element(By.CLASS_NAME, identifier)
        elif typeIdentifier == ETypeIdentify.XPATH:
            el = driver.find_element(By.XPATH, identifier)
        elif typeIdentifier == ETypeIdentify.TAG:
            el = driver.find_element(By.TAG_NAME, identifier)
        else:
            raise ValueError('element not found or invalid identify')
        
        return el