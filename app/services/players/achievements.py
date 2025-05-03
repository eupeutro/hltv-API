from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim, extract_from_url
from app.utils.xpath import Players

@dataclass
class HLTVPlayerAchievements(HLTVBase):
    player_id: str

    def __post_init__(self) -> None:
        
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who#tab-achievementBox"
        self.URL = url
        self.page = self.request_url_page()
        #self.raise_exception_if_not_found(xpath=Players.Profile.URL)
        print(self.page)

    def parse_player_achievements(self) -> list:

        achievements = self.page.xpath("//table[contains(@class, 'achievement-table')]//tr[contains(@class, 'team')]")
        print(achievements)