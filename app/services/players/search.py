from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_country_name_from_flag_url



@dataclass
class HLTVPlayerSearch(HLTVBase):
    """
    A class for searching players on HLTV and retrieving search results.

    Args:
        query (str): The search query for finding players on HLTV.
    """

    query: str

    def __post_init__(self) -> None:
        """
        Initialize the HLTVPlayerSearch class by setting up the search URL.
        """

        HLTVBase.__init__(self)
        self.URL = f"https://www.hltv.org/search?term={self.query}"
        self.response["query"] = self.query
        self.page_data = self.__fetch_json()
        
    
    def __fetch_json(self) -> dict:
        """
        Makes a GET request to the HLTV search URL and returns the JSON response.

        Returns:
            dict: Raw JSON data returned from the HLTV search endpoint.
        """

        res = self.make_request(self.URL)
        return res.json()

    def __parse_search_results(self) -> list:
        """
        Parses the list of players from the HLTV search results.

        Extracted data includes:
            - id: Unique HLTV player ID
            - name: Full name (first + last)
            - nickname: In-game nickname
            - nationality: Country derived from flag URL
            - flag_url: URL to the player's country flag
            - url: Link to the player profile page

        Returns:
            list: A list of dictionaries, each representing a player.
        """

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

                "id": id,
                "name": name,
                "nickname": nickname,
                "nationality": nationality,
                "flag_url": flag_url,
                "url": url
            })
        
        return results
        
    def search_players(self) -> dict:
        """
        Retrieves and parses player search results based on the provided query.

        Returns:
            dict: A dictionary containing the original search query and a list of results.
        """
        
        self.response["query"] = self.query
        self.response["results"] = self.__parse_search_results()

        return self.response