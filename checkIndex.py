"""
elasticsearch的版本需要是7.12.0
"""
import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# new
# ip = '210.26.48.81'
# port = '9201'
# old
ip = '121.43.234.160'
port = '9200'

es = Elasticsearch(
    [ip],
    http_auth=('wbliu20', '731126'),  # 在这里输入账户名和密码
    scheme="http",
    port=port,
    ssl_context=context,
)

res = es.indices.get(index='wbliu20_team_project')
print(res)
