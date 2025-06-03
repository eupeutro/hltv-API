from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel, AuditMixin

class CoachDetails(HLTVBaseModel):
    id: str
    nickname: str

class LineupDetails(HLTVBaseModel):
    id: str
    nickname: str


class TeamProfileDetails(HLTVBaseModel):
    name: str
    valve_ranking: Optional[int]
    world_ranking: Optional[int]
    weeks_in_top30_for_core: Optional[int]
    average_player_age: Optional[float]
    lineup: List[LineupDetails]
    coach: List[CoachDetails]
    logo_url: HttpUrl
    social_media: Optional[List[HttpUrl]]

class TeamProfile(HLTVBaseModel, AuditMixin):
    id: str
    team_profile: Optional[TeamProfileDetails]