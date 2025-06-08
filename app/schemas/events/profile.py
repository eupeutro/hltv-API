from typing import List, Optional
 
from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel, AuditMixin

class EventEvpsDetails(HLTVBaseModel):
    id: str
    nickname: str
    event_stats: HttpUrl

class EventMvpDetail(HLTVBaseModel):
    id: Optional[str]
    nickname: Optional[str]
    event_stats: Optional[HttpUrl]

class EventTeamDetail(HLTVBaseModel):
    id: str
    name: str
    team_placement: str


class EventProfileDetail(HLTVBaseModel):
    name: str
    start_date: str
    end_date: str
    team_count: int
    prize_pool: int
    location: str
    location_flag_url: HttpUrl
    mvp: Optional[List[EventMvpDetail]]
    evps: Optional[List[EventEvpsDetails]]
    teams: List[EventTeamDetail]
class EventProfile(HLTVBaseModel,AuditMixin):
    id: str
    event_profile: EventProfileDetail