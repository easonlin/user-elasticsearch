import logging
from logging import config
from logging import LoggerAdapter

class CustomAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        return '(TRACEID:%s) %s' % (self.extra.get('trace_id'), msg), kwargs


def load_logger(config_file):
    config.fileConfig(config_file)


def get_adpater(logger):
    adpater = CustomAdapter(logger=logger, extra={})
    return adpater


def set_trace_id(logger, trace_id):
    if logger.extra:
        logger.extra['trace_id'] = trace_id
    else:
        logger.extra  = {'trace_id': trace_id}
SYS_APPENGINE_CONFIG_FILE = 'config.ini'
config_file = SYS_APPENGINE_CONFIG_FILE
load_logger(config_file)
logger = logging.getLogger(__name__)
logger.info('{"vid"="eason_test01"}')
logger.info('{"vid"="eason_test02"}\n')
logger.info('@cee: {"vid"="eason_test03"}\n')
