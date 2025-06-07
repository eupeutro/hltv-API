from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel

class LineupDetails(HLTVBaseModel):
    player_id: str
    nickname: str
    nationality: str
    picture_url: HttpUrl


class RankingStatsDetails(HLTVBaseModel):
    team_id: str
    team_name: str
    placement: int
    hltv_points: int
    logo_url: HttpUrl
    lineup: List[LineupDetails]
    
    

class RankingStats(AuditMixin, HLTVBaseModel):
    start_placement: int
    end_placement: int
    ranking_date: str
    ranking_stats: List[RankingStatsDetails]