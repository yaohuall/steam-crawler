import datetime
import scrapy
from scrapy.http import FormRequest
from SteamCrawler.items import SteamcrawlerItem

class SteamspiderSpider(scrapy.Spider):
    name = 'steamSpider'
    allowed_domains = ['store.steampowered.com']

    def start_requests(self):
        params = {
            'cc': 'TW',
            'l': 'tchinese',
            'clanAccountID': '41316928',
            'clanAnnouncementGID': '3016840454305565994',
            'flavor': 'popularpurchaseddiscounted', # sale category: popularpurchaseddiscounted, contenthub_topsellers, topwishlisted
            'start': '0',
            'count': '10', # numbers of games
            'tabuniqueid': '6',
            'sectionuniqueid': '13268',
            'return_capsules': 'true',
            'origin': 'https://store.steampowered.com',
            'bForceUseSaleTag': 'true',
            'strContentHubType': 'specials',
            'strTabFilter': '',
            'bRequestFacetCounts': 'true',
        }
        url = 'https://store.steampowered.com/saleaction/ajaxgetsaledynamicappquery?'

        yield scrapy.FormRequest(url = url, formdata=params, callback = self.parse, dont_filter = True)

    def parse(self, response):
        # data: dict_keys(['success', 'appids', 'store_item_keys', 'faceting', 'multifaceting', 'match_count', 'solr_index', 'possible_has_more'])
        data = response.json()
        app_ids = data['appids']

        for app_id in app_ids:
            app_url = f'https://store.steampowered.com/api/appdetails?appids={app_id}'
            yield scrapy.Request(url = app_url, callback = self.parse_content, dont_filter = True, meta={'app_id':str(app_id)})

    def parse_content(self, response):
        crawl_date = datetime.datetime.today()
        item = SteamcrawlerItem()

        game_id = response.meta['app_id']
        game_data = response.json()
        game = game_data[game_id]['data']
        name = game['name']
        steam_appid = game['steam_appid']
        price_overview = game['price_overview']
        genres = game['genres']
        release_date = game['release_date']

        item = SteamcrawlerItem()
        item['name'] = name
        item['steam_appid'] = steam_appid
        item['price_overview'] = price_overview
        item['genres'] = genres
        item['release_date'] = release_date
        item['crawl_date'] = crawl_date

        yield item
