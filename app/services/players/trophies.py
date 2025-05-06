from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim, extract_from_url
from app.utils.xpath import Players

@dataclass
class HLTVPlayersTrophies(HLTVBase):
    player_id: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who#tab-trophiesBox"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath = Players.Profile.URL)

    def __parse_player_trophies(self) -> list:

        tournament_name = self.get_all_by_xpath(Players.Trophies.TOURNAMENT_NAME)
        tournament_img_url = self.get_all_by_xpath(Players.Trophies.TROPHY_IMG_URL)
        tournament_url = self.get_all_by_xpath(Players.Trophies.TOURNAMENT_URL)
        tournament_id = [extract_from_url(url, "id") for url in tournament_url]

        trophies = []

        for name, img_url, url, tid in zip(tournament_name, tournament_img_url, tournament_url, tournament_id):
            trophy ={
                "tournament_name": name if tournament_name else None,
                "tournament_img_url": f"https://www.hltv.org{img_url}" if tournament_img_url else None,
                "tournament_url": f"https://www.hltv.org{url}" if tournament_url else None,
                "tournament_id": tid if tournament_id else None
            }
            trophies.append(trophy)

        return trophies
    
    def get_player_trophies(self) -> dict:
       
       
        trophies = self.__parse_player_trophies()
        self.response["id"] = self.player_id
        self.response["trophy_count"] = len(trophies)
        self.response["trophies"] = trophies
        
        return self.response