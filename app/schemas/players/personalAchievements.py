from typing import List, Optional


from pydantic import HttpUrl

from app.schemas.base import AuditMixin,HLTVBaseModel


class Top20Achievement(HLTVBaseModel):
    placement: str
    year: str
    article: HttpUrl

class personalAchievementDetail(HLTVBaseModel):
    major_winner_count: Optional[int] = None
    major_mvp_count: Optional[int] = None
    mvp_winner_count: Optional[int] = None
    mvp_winner: Optional[List[str]] = None
    top_20: Optional[List[Top20Achievement]] = None

class PlayerPersonalAchievements(HLTVBaseModel, AuditMixin):
    id: str
    personal_achievements: Optional[personalAchievementDetail]