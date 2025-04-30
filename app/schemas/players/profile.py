from typing import Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel

class PlayerProfile(HLTVBaseModel,AuditMixin):
    id : str
    url: HttpUrl
    nickname: str
    name: str
    age: Optional[int]
    nationality: Optional[str]
    rating:Optional[float]
    current_team: str
    current_team_url: HttpUrl
    image_url: Optional[HttpUrl]
    social_media: Optional[list[str]]