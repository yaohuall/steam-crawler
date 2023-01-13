from typing import List
from fastapi import APIRouter, HTTPException, status
from models.schemas import Game
from database.connection import retrieve_games

router = APIRouter(tags=["Game"])

@router.get("/", response_model=List[Game])
async def retrieve_all_games():
    games = await retrieve_games()
    return games
