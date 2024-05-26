from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def start():
    # Configurar opções do Firefox
    options = Options()
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" 
    
    # Configurar o serviço do geckodriver
    service = FirefoxService(executable_path="geckodriver.exe")

    # Iniciar o WebDriver do Firefox
    driver = webdriver.Firefox(service=service, options=options)
    
    return driver, Keys, By

def main():
    driver, Keys, By = start()
    try:
        # Abrir o Google
        driver.get('https://www.google.com')

        # Verificar o título da página
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        
        textarea.send_keys("fotos de gatos")
        
        time.sleep(1)
        
        textarea.send_keys(Keys.ENTER)
        
        time.sleep(1)

    finally:
        # Fechar o navegador
        driver.quit()

if __name__ == "__main__":
    main()