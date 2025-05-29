from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_country_name_from_flag_url,extract_from_url

@dataclass
class HLTVTeamSearch(HLTVBase):
    query: str
    
    def __post_init__(self) -> None:
        self.URL = f"https://www.hltv.org/search?term={self.query}"
        self.page_data = self.__fetch_json()
    
    def __fetch_json(self) -> dict:
        res = self.make_request(self.URL)
        return res.json()
    
    def __parse_search_results(self) -> list:

        results = []

        teams = self.page_data[0].get("teams",[])

        for team in teams:
            id = team.get("id")
            name = team.get("name")
            country = team.get("countryName")
            url = f"https://www.hltv.org{team.get('location')}"
            team_logo_url = team.get("teamLogoDay")
            
            lineup = []
            for player in team .get("players", []):
                id = extract_from_url(player.get("location"), "id")

                player_data = {
                    "id": id,
                    "nickname": player.get("nickName"),
                    "name": f"{player.get('firstName', '')} {player.get('lastName', '')}".strip(),
                    "nationality": extract_country_name_from_flag_url(player.get("flagUrl")),
                    "profile_url": f"https://www.hltv.org{player.get('location')}"
                }
                lineup.append(player_data)
            
            results.append({
                "id": str(id),
                "name":name,
                "country": country,
                "url": url,
                "team_logo_url": team_logo_url,
                "lineup": lineup
            })

        return results
    
    def search_teams(self) -> dict:

        self.response["query"] = self.query
        self.response["results"] = self.__parse_search_results()

        return self.response


