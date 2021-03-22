import json
import os
from blogster.settings import BASE_DIR

json_dir = os.path.join(BASE_DIR, 'infodata/jsondata')

helpcenterjson_data=open('{}/helpcenter.json'.format(json_dir))
hc_json= json.load(helpcenterjson_data)