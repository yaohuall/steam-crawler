from bson import ObjectId
from pydantic import BaseModel, validator
from typing import List, Optional, Dict
from datetime import date, datetime

class Game(BaseModel):
    id: str
    name: str
    steam_appid: int
    price_overview: Optional[Dict]
    genres: Optional[Dict]
    release_date: Optional[Dict]
    crawl_date: Optional[Dict]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "game name",
                "genres": "game category"
            }
        }

    