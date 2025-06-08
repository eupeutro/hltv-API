from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.teams.search import TeamSearch

from app.services.teams.search import HLTVTeamSearch

router = APIRouter()

@router.get("/search/{team_name}", response_model=  TeamSearch, response_model_exclude_none=True)
def search_teams(team_name : str):
    hltv = HLTVTeamSearch(query= team_name)
    found_teams = hltv.search_teams()
    return found_teams