from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel, AuditMixin

class prizeDetails(HLTVBaseModel):
    prize: Optional[int]
    club_share: Optional[int]

class vrsDetails(HLTVBaseModel):
    vrs_date: Optional[str]
    points_before_event: Optional[int]
    points_after_event: Optional[int]
    points_acquired: Optional[int]
    placement_before_event: Optional[int]
    placement_after_event: Optional[int]

class coachDetails(HLTVBaseModel):
    id: str
    nickname: str

class lineupDetails(HLTVBaseModel):
    id: str
    nickname: str
    event_stats: HttpUrl


class eventTeamStatsDetails(HLTVBaseModel):
    team_placement: str
    prize: Optional[List[prizeDetails]]
    vrs: Optional[List[vrsDetails]]
    qualify_method: Optional[str]
    lineup: List[lineupDetails]
    coach: Optional[List[coachDetails]]
    
    



class EventTeamStats(HLTVBaseModel, AuditMixin):
    event_id: str
    team_id: str
    stats: eventTeamStatsDetails