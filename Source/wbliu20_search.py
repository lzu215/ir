"""
elasticsearch的版本需要是7.12.0
"""
import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

es = Elasticsearch(
    ['121.43.234.160'],
    http_auth=('username', 'password'),  # 在这里输入账户名和密码
    scheme="http",
    port=9200,
    ssl_context=context,
)

print("Welcome to Whatever Search Engine!")
print("Please enter your query: ", end='')
keywords = input()
print("Please choose your option to sort the result \n"
      "(0. BM25 1. Review_counts 2. Stars 3. Review_counts+Stars*10): ", end='')
option = int(input())
scripts = {0: "BM25",
           1: "doc['review_count'].value",
           2: "doc['stars'].value",
           3: "doc['review_count'].value+doc['stars'].value*10"}

query1 = {
    "query": {
        "match": {
            "name": keywords
        }
    }
}
query2 = {
  "query": {
    "script_score": {
      "query": {
          "match": {
              "name": keywords
          }
      },
      "script": {
        "source": scripts[option]
      }
    }
  }
}

res = es.search(index="wbliu20_yelp", body=query2 if option else query1)
print("Find %d results:" % res['hits']['total']['value'])
print("----------------")
i = 1
for hit in res['hits']['hits']:
    print("%d (Score:%.2f): %s" % (i, hit["_score"], hit["_source"]["name"]))
    i += 1
