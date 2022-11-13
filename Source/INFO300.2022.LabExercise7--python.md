
# Python for ElasticSearch

Date: October 14, 2022

The following highlights what you need to create such a python program.

## Preparation

On the shell / command line:

```shell
pip3 install elasticsearch
```

## Test Your Connection to TUX-ES Cluster

First, create a ```suwei_search.py``` to test connection to our ElasticSearch cluster with your username and password.

```python
import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

es = Elasticsearch(
    ['121.43234.160'],
    http_auth=('YourUserName', 'YourTuxElasticSearchPassword'),
    scheme="http",
    port=9200,
    ssl_context = context,
)

print(es.info())
```

Then, run the test program on the command line:

```shell
python3 suwei_search.py
```

If you see the following in your output, you are good to go:

```json
{
  'name': 'tux-es1',
  'cluster_name': 'tux-elasticsearch',
  'cluster_uuid': 'g4BhOQajT0KUKcIfE0OO6A',
  'version': {
    'number': '7.3.2',
    'build_flavor': 'oss',
    'build_type': 'deb',
    'build_hash': '1c1faf1',
    'build_date': '2019-09-06T14:40:30.409026Z',
    'build_snapshot': False,
    'lucene_version': '8.1.0',
    'minimum_wire_compatibility_version': '6.8.0',
    'minimum_index_compatibility_version': '6.0.0-beta1'
  },
  'tagline': 'You Know, for Search'
}
```

Note that, in addition to the above, you will get warnings against an unverified certificate because of options ```context.check_hostname = False```
and ```context.verify_mode = ssl.CERT_NONE```. This is okay for now as you can trust our servers at CCI.

## Code to Create an Index and Create a Document

Now you can add the following after the authentication code:

```python
from datetime import datetime
doc = {
    'author': 'Su Wei',
    'text': 'Information Retrieval Systems 2022',
    'timestamp': datetime.now(),
}

# Load the doc to an index as doc #1
res = es.index("suwei_2022_python", id=1, body=doc)

# Show results from server response
print(res['result'])
```

This should index the document and, if successful, return the following result:

```
created
```

## Code to Query and Show Results

Now you can test a search query such as:

```python
# query to search on title and content fields
keywords = "Presidential Election"
query = {
  "from" : 0, "size" : 3,
  "query": {
    "multi_match" : {
      "query": keywords,
      "fields": ["headline", "short_description" ]
    }
  }
}

# issue the query to elastic search
res = es.search(index="news",body=query)
# show the number of hits (matches)
print("Got %d Hits:" % res['hits']['total']['value'])
# show the results with author and title information
for hit in res['hits']['hits']:
    print("%(author)s: %(headline)s" % hit["_source"])
```

## For More

This gives you a starting point to program in Python to create a front end for your ElasticSearch index. There is much more you can do from here:

You want to make this interactive and should ask for user's query input, for example:

```python
print("Please enter your search query: ")
keywords = input()
```

For more about you can do with the Python APIs for ElasticSearch, consults the following references.


## References

+ https://elasticsearch-py.readthedocs.io/en/master/
+ https://elasticsearch-py.readthedocs.io/en/master/api.html
