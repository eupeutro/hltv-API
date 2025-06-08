from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel


class TeamSearchPlayersDetails(HLTVBaseModel):
    id: str
    nickname: str
    name: str
    nationality: str
    profile_url: HttpUrl

class TeamSearchResult(HLTVBaseModel):
    id: str
    name: str
    country: str
    url: HttpUrl
    team_logo_url: HttpUrl
    lineup: Optional[List[TeamSearchPlayersDetails]]



class TeamSearch(HLTVBaseModel, AuditMixin):
    query: str
    results: Optional[List[TeamSearchResult]]