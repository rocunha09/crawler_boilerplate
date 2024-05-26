# crawler_boilerplate
This project is the materialization of a latent need that runs through the day-to-day activities of many companies or their management and technology layers.

With the aim of facilitating and speeding up the construction and execution of crawlers, removing the friction of project setup and thus moving directly to the value layer, which is the construction of the routine itself, this project was created and will be improved and maintained.

The technologies initially chosen are 
* Python;
* Selenium;
* Browsers: Chrome, Firefox, Opera, Edge;
* Mode: simple (local use) and advanced (Provides for the use of the crawler with scalability and cloud deployment, and others options).

If you, the user of this project, have any new ideas for improvement or correction, I would be grateful to read the open issues and try to implement them.

---
## Prerequisites

###  Create an .env file
```txt
FIREFOX_WIN_BINARY_PATH=<path to browser>
GECKODRIVER_WIN_DRIVER_PATH="resources\\win_drivers\\firefox\\geckodriver.exe"

CHROME_WIN_BINARY_PATH=""
CHROME_WIN_DRIVER_PATH="resources\\win_drivers\\chrome\\chromedriver.exe"

EDGE_WIN_BINARY_PATH=""
EDGE_WIN_DRIVER_PATH="resources\\win_drivers\\edge\\msedgedriver.exe"

OPERA_WIN_BINARY_PATH=""
OPERA_WIN_DRIVER_PATH="resources\\win_drivers\\opera\\operadriver.exe"
```

**obs.: Drivers tested in this project so far**
- [x] firefox webdriver (gecko): 126.0 (64 bits)
- [ ] opera webdriver: 2.1.4342 (64 bits)
- [ ] chrome webdriver: 125.0.6422.77 (64 bits)
- [ ] edge webdriver:  125.0.2535.67 (64 bits)

### Create a virtual environment to set the stage for the project
1. creating enviroment
```bash
python -m venv venv
```
2. activating enviroment
```bash
./venv/Scripts/activate
```

### Install dependencies
```bash
pip install requirements.txt
```

---
## Using the project
### Setup new browser/enviroment
To add new settings for environments and browsers follow the steps:
* Save the desired browser driver in resources/drivers
* Register in .env the path of the desired browser and the path created for the driver.
* Create a method in the DriverFactory class to create the desired driver with the desired settings following the established pattern.
* Register in Enum EBrowsers the desired browser and the name of the method created in DriverFactory

Now just call the start method in main() with the desired browser

### Using Setups to run your Scripts



---

## More Information

### Drivers
* Firefox: https://github.com/mozilla/geckodriver/releases
* Opera: https://github.com/operasoftware/operachromiumdriver/releases
* Google: https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip
* Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH#downloads