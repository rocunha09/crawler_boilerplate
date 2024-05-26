from setup.setup_selenium_browser import start
import time

def main():
    driver, Keys, By = start()
    try:
        driver.get('https://www.google.com')

        textarea = driver.find_element(By.TAG_NAME, "textarea")
        
        textarea.send_keys("fotos de gatos")
        
        time.sleep(1)
        
        textarea.send_keys(Keys.ENTER)
        
        time.sleep(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
