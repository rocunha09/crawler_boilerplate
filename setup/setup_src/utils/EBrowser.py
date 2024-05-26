from enum import Enum

class EBrowser(Enum):
    FIREFOX = ('firefox', 'DriverFactory.create_firefox_driver')
    CHROME = ('chrome', 'DriverFactory.create_chrome_driver')
    EDGE = ('edge', 'DriverFactory.create_edge_driver')
    OPERA = ('opera', 'DriverFactory.create_opera_driver')