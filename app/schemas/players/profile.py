from typing import Optional, List

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel

class PlayerProfile(HLTVBaseModel,AuditMixin):
    id : str
    url: HttpUrl
    nickname: str
    name: str
    age: int
    nationality: str
    rating:Optional[float]
    current_team: Optional[str]
    current_team_url: Optional[HttpUrl]
    image_url: Optional[HttpUrl]
    social_media: Optional[List[str]]