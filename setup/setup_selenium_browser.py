from setup.setup_src.model.DriverFactory import DriverFactory

def start(browser):
    return DriverFactory.create_driver(browser)
