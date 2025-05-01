from dataclasses import dataclass
import requests

from app.services.base import HLTVBase




@dataclass
class HLTVPlayerSearch(HLTVBase):
    query: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        self.URL = f"https://www.hltv.org/search?term={self.query}"
        self.response["query"] = self.query
        self.page_data = self.__fetch_json()
        
    

    def __fetch_json(self) -> dict:
        res = requests.get(self.URL, headers={"User-Agent": "Mozilla/5.0"})
        res.raise_for_status()
        return res.json()

    def __parse_search_results(self) -> list:

        results = []    

        players = self.page_data[0].get("players", [])


        for player in players:
            id = player.get("id")
            name = trim(result.xpath(Players.Search.NAME))
            nickname = extract_nickname_from_name(name)
            nationality = trim(result.xpath(Players.Search.NATIONALITY))
            url= f"https://www.hltv.org/{result.xpath(Players.Search.URL)}"

            results.append({

                "id": id,
                "name": name,
                "nickName": nickname,
                "nationality": nationality,
                "url": url
            })
        
        return results
        
    def search_players(self) -> dict:

        self.response["query"] = self.query
        self.response["results"] = self.__parse_search_results()

        return self.response