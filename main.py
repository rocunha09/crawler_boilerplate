from setup.setup_src.utils.EBrowser import EBrowser
from setup.setup_selenium_browser import start
import time

driver, Keys, By = start(EBrowser.FIREFOX.value[0])

from src import run

def main():
    try:
        run()
        
        
        
        
        
        '''
        driver.get('https://www.google.com')

        textarea = driver.find_element(By.TAG_NAME, "textarea")
        
        textarea.send_keys("fotos de gatos")
        
        time.sleep(1)
        
        textarea.send_keys(Keys.ENTER)
        
        time.sleep(1)
        
        '''

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == "__main__":
    main()
