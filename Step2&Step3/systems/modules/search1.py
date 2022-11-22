# Imports

from core import getES, config, configs


# Config

config(
    page_size = 10
)


# Functions

def execute(keywords, start):
    # Include the keywords in a query object (JSON)
    query = {
        "from": start, "size": configs.search1.page_size,
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
    res = getES.search(index="wbliu20_team_project", body=query)
    hits = res["hits"]
    return hits

