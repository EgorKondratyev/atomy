import logging.config
import yaml
import logging


logger = logging.getLogger('__main__')
with open(r'path', 'r') as obj:
    logging.config.dictConfig(yaml.safe_load(obj))
