import logging.config
import yaml
import logging


logger = logging.getLogger('__main__')
# C:\python\bots\TelegramBot\log\config.yml
# /root/atomy/log/config.yml
with open(r'/root/atomy/log/config.yml', 'r') as obj:
    logging.config.dictConfig(yaml.safe_load(obj))
