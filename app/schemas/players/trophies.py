from typing import Optional, List

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel


class trophiesDetails(HLTVBaseModel):
    tournament_id: str
    tournament_name: str
    tournament_url: HttpUrl
    tournament_img_url: HttpUrl


class PlayerTrophies(HLTVBaseModel,AuditMixin):
    id: str
    trophy_count: Optional[int] = None
    trophies: Optional[List[trophiesDetails]]= None