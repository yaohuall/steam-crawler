import os 
import json
from bson.json_util import dumps
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://root:123456@127.0.0.1:27017')
database = client.crawlers
games_collection = database.games

async def retrieve_games():
    games = []
    cursor = games_collection.find()
    for game in await cursor.to_list(length=100):
        game = json.loads(dumps(game))
        # add object id string type
        game['id'] = game['_id']['$oid']
        games.append(game)
    return games
