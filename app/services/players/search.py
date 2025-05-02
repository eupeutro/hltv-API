from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_country_name_from_flag_url



@dataclass
class HLTVPlayerSearch(HLTVBase):
    query: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        self.URL = f"https://www.hltv.org/search?term={self.query}"
        self.response["query"] = self.query
        self.page_data = self.__fetch_json()
        
    

    def __fetch_json(self) -> dict:
        res = self.make_request(self.URL)
        return res.json()

    def __parse_search_results(self) -> list:

        results = []    

        players = self.page_data[0].get("players", [])


        for player in players:
            id = player.get("id")
            name = f"{player.get('firstName', '')} {player.get('lastName', '')}".strip()
            nickname = player.get("nickName")
            flag_url = player.get("flagUrl")
            nationality = extract_country_name_from_flag_url(flag_url)
            url= f"https://www.hltv.org/{player.get('location','')}"

            results.append({

                "id": str(id),
                "name": name,
                "nickname": nickname,
                "nationality": nationality,
                "flag_url": flag_url,
                "url": url
            })
        
        return results
        
    def search_players(self) -> dict:

        self.response["query"] = self.query
        self.response["results"] = self.__parse_search_results()

        return self.response