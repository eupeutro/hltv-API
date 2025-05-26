from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel, AuditMixin

class prizeDetails(HLTVBaseModel):
    prize: int
    club_share: int

class vrsDetails(HLTVBaseModel):
    vrs_date: str
    points_before_event: int
    points_after_event: int
    points_acquired: int
    placement_before_event: int
    placement_after_event: int

class coachDetails(HLTVBaseModel):
    id: str
    nickname: str

class lineupDetails(HLTVBaseModel):
    id: str
    nickname: str
    event_stats: HttpUrl


class eventTeamStatsDetails(HLTVBaseModel):
    team_placement: str
    qualify_method: str
    lineup: List[lineupDetails]
    coach: Optional[List[coachDetails]]
    vrs: Optional[List[vrsDetails]]
    prize: Optional[List[prizeDetails]]



class EventTeamStats(HLTVBaseModel, AuditMixin):
    event_id: str
    team_id: str
    stats: List[eventTeamStatsDetails]