from typing import Optional

from fastapi import APIRouter,HTTPException

from app.schemas.players.profile import PlayerProfile
from app.schemas.players.search import PlayerSearch
from app.schemas.players.teamAchievements import PlayerTeamAchievements
from app.schemas.players.personalAchievements import PlayerPersonalAchievements
from app.schemas.players.trophies import PlayerTrophies
from app.schemas.players.stats import PlayerStats
from app.schemas.players.careerStats import PlayerCareerStats

from app.services.players.profile import HLTVPlayerProfile
from app.services.players.search import HLTVPlayerSearch
from app.services.players.teamAchievements import HLTVPlayerTeamAchievements
from app.services.players.personalAchievements import HLTVPlayerPersonalAchievements
from app.services.players.trophies import HLTVPlayersTrophies
from app.services.players.stats import HLTVPlayerStats
from app.services.players.careerStats import HLTVPlayerCareerStats

router = APIRouter()

@router.get("/search/{player_name}",  response_model = PlayerSearch, response_model_exclude_none=True)
def search_players(player_name: str):
 
     hltv = HLTVPlayerSearch(query= player_name)
     found_players = hltv.search_players()
     return found_players
  

@router.get("/{player_id}/profile", response_model=PlayerProfile,response_model_exclude = None)
def get_player_profile(player_id: str):
    hltv = HLTVPlayerProfile(player_id = player_id)
    player_info = hltv.get_player_profile()
    return player_info

@router.get("/{player_id}/team_achievements", response_model=PlayerTeamAchievements, response_model_exclude_none=True)
def get_player_team_achievements(player_id: str):
    hltv = HLTVPlayerTeamAchievements(player_id=player_id)
    player_team_achievements = hltv.get_player_team_achievements()
    return player_team_achievements

@router.get("/{player_id}/personal_achievements", response_model = PlayerPersonalAchievements, response_model_exclude_none=True)
def get_player_personal_achievements(player_id: str):
    hltv = HLTVPlayerPersonalAchievements(player_id=player_id)
    player_personal_achievements = hltv.get_player_personal_achievements()
    return player_personal_achievements

@router.get("/{player_id}/trophies", response_model = PlayerTrophies, response_model_exclude_none=True)
def get_player_trophies(player_id: str):
    hltv = HLTVPlayersTrophies(player_id=player_id)
    player_trophies = hltv.get_player_trophies()
    return player_trophies

@router.get("/{player_id}/stats", response_model = PlayerStats, response_model_exclude_none=True)
def get_player_stats(player_id: str):
    hltv = HLTVPlayerStats(player_id=player_id)
    player_stats = hltv.get_player_stats()
    return player_stats

@router.get("/{player_id}/career_stats", response_model = PlayerCareerStats, response_model_exclude_none=True)
def get_player_career_stats(player_id: str):
    hltv = HLTVPlayerCareerStats(player_id=player_id)
    player_career_stats = hltv.get_player_career_stats()
    return player_career_stats