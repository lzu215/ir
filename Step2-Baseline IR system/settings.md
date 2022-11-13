```
FEED_EXPORT_ENCODING = 'utf-8'
ELASTICSEARCH_SERVERS = ['210.26.48.81']
ELASTICSEARCH_PORT = 9201
ELASTICSEARCH_USERNAME = 'wbliu20'
ELASTICSEARCH_PASSWORD = '731126'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'
ELASTICSEARCH_INDEX = 'wbliu20/project'
ELASTICSEARCH_TYPE = '_doc'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/16.1 Safari/605.1.15'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'minecraft.pipelines.MinecraftPipeline': 300,
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
}
```