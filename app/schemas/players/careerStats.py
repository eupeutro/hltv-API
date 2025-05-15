from typing import Optional, List

from app.schemas.base import HLTVBaseModel, AuditMixin


class PlayerCareerStatsDetails (HLTVBaseModel):
    total_kills: Optional[float] = None
    headshot_percentage: Optional[float] = None
    total_deaths: Optional[float] = None
    kd_ratio: Optional[float] = None
    damage_per_round: Optional[float] = None
    maps_played: Optional[int] = None
    rounds_played: Optional[int] = None
    kills_per_round: Optional[float] = None
    assists_per_round: Optional[float] = None
    saved_by_teammate_per_round: Optional[float] = None
    saved_teammates_per_round: Optional[float] = None
    rating_1_0: Optional[float] = None

class PlayerCareerStats (HLTVBaseModel, AuditMixin):
    id: str
    stats: Optional[PlayerCareerStatsDetails] = None