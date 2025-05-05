from typing import Optional

from fastapi import APIRouter,HTTPException

from app.schemas.players.profile import PlayerProfile
from app.schemas.players.search import PlayerSearch
from app.schemas.players.Achievements import PlayerAchievements

from app.services.players.profile import HLTVPlayerProfile
from app.services.players.search import HLTVPlayerSearch
from app.services.players.achievements import HLTVPlayerAchievements


router = APIRouter()

@router.get("/search/{player_name}",  response_model = PlayerSearch)
def search_players(player_name: str):
 
     hltv = HLTVPlayerSearch(query= player_name)
     found_players = hltv.search_players()
     return found_players
  

@router.get("/{player_id}/profile", response_model=PlayerProfile,response_model_exclude = None)
def get_player_profile(player_id: str):
    hltv = HLTVPlayerProfile(player_id = player_id)
    player_info = hltv.get_player_profile()
    return player_info

@router.get("/{player_id}/achievements", response_model=PlayerAchievements)
def get_player_achievements(player_id: str):
    hltv = HLTVPlayerAchievements(player_id=player_id)
    player_achievements = hltv.get_player_achievements()
    return player_achievements