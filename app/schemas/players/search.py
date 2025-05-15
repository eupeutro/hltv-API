from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel



class PlayerSearchResult(HLTVBaseModel):
    id: str
    name: str
    nickname: str
    nationality: str
    flag_url: HttpUrl
    url: HttpUrl

class PlayerSearch(HLTVBaseModel,AuditMixin):
    query: str
    results: Optional[List[PlayerSearchResult]] =None