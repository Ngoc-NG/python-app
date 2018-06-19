import os.path
from app.utils import load_app_config

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(ROOT_PATH, "conf")
CONFIG_FILE = os.getenv("CONFIG_FILE", 'application.json')
config_file_path = os.path.join(CONF_DIR, CONFIG_FILE)

# load config or rise exception
app_config = load_app_config(config_file_path)

app_ip = app_config['app']['ip']
app_version = app_config['app']['version']
app_log_config_path = app_config['app']['log_config_path']
app_log_level = app_config['app']['log_level']
