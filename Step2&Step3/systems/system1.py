from flask import Flask, url_for
from flask import request
from flask import render_template
import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

# Create the web app with a `static` directory for static files
app = Flask(__name__, static_url_path='/static')
context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# ip = '210.26.48.81'
# port = '9201'
ip = '121.43.234.160'
port = 9200

es = Elasticsearch(
    [ip],
    scheme="http",
    port=port,
    http_auth=('wbliu20', '731126'),
    ssl_context=context
)
# home page
# the `/` is the root of your web app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['get'])
def search():
    keywords = request.args.get('keywords')
    # Include the keywords in a query object (JSON)
    query = {
        "from": 0, "size": 10,
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": [
                    "Title",
                    "Description",
                    "Tags"
                ]
            }
        }
    }

    # Send a search request with the query to server
    res = es.search(index="wbliu20_team_project", body=query)
    hits = res["hits"]["total"]["value"]
    return render_template('results.html', keywords=keywords, hits=hits, docs=res["hits"])
