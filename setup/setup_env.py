from dotenv import load_dotenv
import os

# get actual path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

# path to parent dir, getting .env file
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

# setup of env variables of .env file
FIREFOX_BINARY_PATH = os.getenv('FIREFOX_BINARY_PATH')
GECKODRIVER_PATH = os.getenv('GECKODRIVER_PATH')