# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from steamCrawler import settings
import psycopg2

class SteamcrawlerPipeline:
    def __init__(self):
        self.connect = psycopg2.connect(
                        host=settings.POSTGRES_HOST, 
                        port=settings.POSTGRES_PORT, 
                        user=settings.POSTGRES_USERNAME, 
                        password=settings.POSTGRES_PASSWORD, 
                        database=settings.POSTGRES_DATABASE,
                        options=settings.POSTGRES_OPTIONS
                    )

    def process_item(self, item, spider):
        return item
