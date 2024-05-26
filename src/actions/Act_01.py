'''
THIS ACTION IS A SIMPLE TEST

SEARCH CAT PHOTOS AT GOOGLE
'''
from main import driver, time
from src.pages.Google import Google

def Act_01_01():
    try:
        google_page = Google('https://www.google.com')
        google_page.set_text_search("cat photos")
        google_page.search()
        time.sleep(5)
    except Exception as e:
        print(f'erro: {e}')
    finally:
         driver.quit()