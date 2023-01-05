# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    oriprice = scrapy.Field()
    saleprice = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    