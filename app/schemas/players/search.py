from typing import Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel



class PlayerSearchResult(HLTVBaseModel):
    id: str
    name: str
    nickname: str
    nationality: str
    url: HttpUrl

class PlayerSearch(HLTVBaseModel,AuditMixin):
    query: str
    results: list[PlayerSearchResult]