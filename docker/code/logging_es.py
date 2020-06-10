from cmreslogging.handlers import CMRESHandler
from datetime import datetime
import logging
import sys





def send_log(message, level='info'):
    from cmreslogging.handlers import CMRESHandler
    handler = CMRESHandler(hosts=[{'host': 'es01', 'port': 9200}],
                            auth_type=CMRESHandler.AuthType.NO_AUTH,
                            es_index_name="my_python_index")
    log = logging.getLogger("PythonTest")
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    if level=='info':
        log.info(str(message))
    else:
        log.error(str(message))
    

#log.debug()
#log.info()
#log.warning()
#log.error()
#log.critical()
#send_log('123456789')