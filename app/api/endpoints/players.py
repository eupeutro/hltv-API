from typing import Optional

from fastapi import APIRouter

from app.services.players.profile import HLTVPlayerProfile

router = APIRouter()

@router.get("/{player_id}/profile")
def get_player_profile(player_id: str):
    hltv = HLTVPlayerProfile(player_id = player_id)
    player_info = hltv.get_player_profile()
    
    return player_info