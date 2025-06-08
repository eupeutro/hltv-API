from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import HLTVBaseModel,AuditMixin


class TeamAchievementsDetails(HLTVBaseModel):
    id: str
    tournament_name: str
    placement: str
    team_event_stats: HttpUrl

class TeamAchievements  (HLTVBaseModel, AuditMixin):
    id: str
    team_achievements: Optional[List[TeamAchievementsDetails]]