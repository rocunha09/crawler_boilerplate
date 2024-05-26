from dotenv import load_dotenv
import os

def get_env(key):
    # get actual path
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)

    # path to parent dir, getting .env file
    dotenv_path = os.path.join(parent_dir, '.env')
    load_dotenv(dotenv_path)
    
    return os.getenv(key)
