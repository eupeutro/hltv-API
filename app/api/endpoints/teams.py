from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.teams.search import TeamSearch
from app.schemas.teams.profile import TeamProfile

from app.services.teams.search import HLTVTeamSearch
from app.services.teams.profile import HLTVTeamProfile

router = APIRouter()

@router.get("/search/{team_name}", response_model=  TeamSearch, response_model_exclude_none=True)
def search_teams(team_name : str):
    hltv = HLTVTeamSearch(query = team_name)
    found_teams = hltv.search_teams()
    return found_teams

@router.get("/profile/{team_id}", response_model = TeamProfile, response_model_exclude_none= True)
def get_team_profile(team_id : str):
    hltv = HLTVTeamProfile (team_id = team_id)
    team_profile = hltv.get_team_profile()
    return team_profile