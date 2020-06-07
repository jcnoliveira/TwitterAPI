import logging
import sys
from cmreslogging.handlers import CMRESHandler
handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="my_python_index")
log = logging.getLogger("PythonTest")
log.setLevel(logging.DEBUG)
log.addHandler(handler)

log.debug('debug message')
log.info('info message')
log.warning('warn message')
log.error('error message')
log.critical('critical message')

