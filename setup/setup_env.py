from dotenv import load_dotenv
import os

# get actual path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

# path to parent dir, getting .env file
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

# setup of env variables of .env file using windows enviroment
FIREFOX_PATH = os.getenv('FIREFOX_WIN_BINARY_PATH')
FIREFOX_DRIVER_PATH = os.getenv('GECKODRIVER_WIN_DRIVER_PATH')

CHROME_PATH = os.getenv('CHROME_WIN_BINARY_PATH')
CHROME_DRIVER_PATH = os.getenv('CHROME_WIN_DRIVER_PATH')

EDGE_PATH = os.getenv('EDGE_WIN_BINARY_PATH')
EDGE_DRIVER_PATH = os.getenv('EDGE_WIN_DRIVER_PATH')

OPERA_PATH = os.getenv('OPERA_WIN_BINARY_PATH')
OPERA_DRIVER_PATH = os.getenv('OPERA_WIN_DRIVER_PATH')