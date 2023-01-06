# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from steamCrawler import settings
import pymongo

class SteamcrawlerPipeline:
    def __init__(self):
        self.mongo_con = pymongo.MongoClient(f'mongodb://{settings.MONGODB_USERNAME}:{settings.MONGODB_PASSWORD}@{settings.MONGODB_HOST}:{settings.MONGODB_PORT}/'
                                            )
        self.mongo_db = self.mongo_con[settings.MONGODB_DB]
        self.collection = self.mongo_db[settings.MONGODB_COLLECTION]
        
    def process_item(self, item, spider):
        if not item:
            raise DropItem(f"Missing data{item}!")

        else:
            self.collection.insert_one(dict(item))

        return item
