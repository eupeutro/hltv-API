from typing import Optional

from fastapi import APIRouter

from app.schemas import players as schemas
from app.services.players.profile import HLTVPlayerProfile


router = APIRouter()

@router.get("/{player_id}/profile", response_model=schemas.PlayerProfile,response_model_exclude=None)
def get_player_profile(player_id: str):
    hltv = HLTVPlayerProfile(player_id = player_id)
    player_info = hltv.get_player_profile()
    
    return player_info