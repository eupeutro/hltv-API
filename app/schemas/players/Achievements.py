from typing import Optional
from typing import List

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel


class AchievementDetail(HLTVBaseModel):
    id: str
    name: str
    
class AchievementDetails(HLTVBaseModel):
    placement: str
    team: AchievementDetail
    tournament: AchievementDetail
    player_stats_url: HttpUrl

class PlayerAchievements(HLTVBaseModel, AuditMixin):
    id: str
    achievements: List[AchievementDetails]