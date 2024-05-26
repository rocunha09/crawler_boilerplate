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
FIREFOX_BINARY_PATH=<path_to_your_firefox_browser>
GECKODRIVER_PATH="resources\\drivers\\firefox\\geckodriver.exe"
```

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