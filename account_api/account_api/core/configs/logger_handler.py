import logging.config
import json
import os

config_file_path = os.path.join(os.path.dirname(__file__), 'logging_config.json')
with open(config_file_path, 'r') as f:
    config = json.load(f)
logging.config.dictConfig(config)

logger = logging.getLogger('account_api')
