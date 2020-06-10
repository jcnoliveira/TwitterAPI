from cmreslogging.handlers import CMRESHandler
from datetime import datetime
import logging
import sys






from cmreslogging.handlers import CMRESHandler
handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="TwitterApi")
log = logging.getLogger("PythonLog")
log.setLevel(logging.INFO)
log.addHandler(handler)


#log.debug()
#log.info()
#log.warning()
#log.error()
#log.critical()
log.info("This is an info statement that will be logged into elasticsearch")