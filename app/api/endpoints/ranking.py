from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.ranking.stats import RankingStats

from app.services.ranking.stats import HLTVRankingStats

router = APIRouter()

@router.get("/stats/start_placement/{start_placement}/end_placement/{end_placement}", response_model = RankingStats, response_model_exclude_none = True)
def get_ranking_stats(start_placement: int, end_placement: int):
    hltv = HLTVRankingStats(start_placement = start_placement, end_placement = end_placement)
    ranking_stats = hltv.get_ranking_stats()
    return ranking_stats