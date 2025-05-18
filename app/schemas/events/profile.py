from typing import List, Optional
 
from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel, AuditMixin

class EventEvpsDetails(HLTVBaseModel):
    id: str
    nickname: str
    event_stats: HttpUrl

class EventMvpDetail(HLTVBaseModel):
    id: str
    nickname: str
    event_stats: HttpUrl

class EventTeamDetail(HLTVBaseModel):
    id: str
    name: str


class EventProfileDetail(HLTVBaseModel):
    name: str
    start_date: str
    end_date: str
    team_count: int
    prize_pool: str
    location: str
    location_flag_url: HttpUrl
    mvp: List[EventMvpDetail]
    evps: List[EventEvpsDetails]
    teams: List[EventTeamDetail]
class EventProfile(HLTVBaseModel,AuditMixin):
    id: str
    event_profile: EventProfileDetail