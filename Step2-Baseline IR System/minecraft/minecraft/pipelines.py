# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MinecraftPipeline:
    def process_item(self, item, spider):
        description = ''.join(item['Description'])
        item['Description'] = description
        views = int(item['Views'].replace(",", ""))
        item['Views'] = views
        downloads = int(item['Downloads'].replace(",", ""))
        item['Downloads'] = downloads
        tags = ', '.join(item['Tags'])
        item['Tags'] = tags
        return item
