from typing import Optional

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
    current_team: Optional[str] = None
    current_team_url: Optional[HttpUrl] = None
    image_url: Optional[HttpUrl] = None
    social_media: Optional[list[str]] = None