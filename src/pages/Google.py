from src.enum.ETypeIdentify import ETypeIdentify
from src.pages.AWebPage import AWebPage
from main import Keys, time

class Google(AWebPage):
    input_search = None
    text_search = ""
    
    def __init__(self, url):
        super().__init__(url)
        self.set_search_field()
        
    def set_search_field(self):
        time.sleep(1)
        self.input_search = self.set_web_element("textarea", ETypeIdentify.TAG)
        
        
    def set_text_search(self, text):
        if self.input_search != None:
            self.input_search.clear()
            time.sleep(1)
            self.input_search.send_keys(text)
        else:
            raise ValueError('element not found')
    
    def get_text_search(self):
        if self.input_search != None:
            self.input_search.get_attribute("value")
        else:
            raise ValueError('element not found')
        
        return self.input_search
    
    
    def search(self):
        self.input_search.send_keys(Keys.ENTER)
    
    