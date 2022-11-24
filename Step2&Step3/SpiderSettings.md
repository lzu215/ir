```
FEED_EXPORT_ENCODING = 'utf-8'

ELASTICSEARCH_SERVERS = 'http://wbliu20:731126@210.26.48.81:9201'
ELASTICSEARCH_INDEX = 'wbliu20_team_project'
ELASTICSEARCH_TYPE = '_doc'


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/16.1 Safari/605.1.15'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'minecraft.pipelines.MinecraftPipeline': 300,
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
}
```
+ new: 'http://wbliu20:731126@210.26.48.81:9201'
+ old: 'http://wbliu20:731126@121.43.234.160:9200'